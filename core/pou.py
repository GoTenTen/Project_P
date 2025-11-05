#pou.py
import random
from Project_P.data.elem_list import ELEMENT

class Pou:
    def __init__(self, owner, name, hp, atk, speed, comp_list, passive, rarity, elem, color, crit_chance=0.1):
        self.owner = owner
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.base_atk = atk
        self.speed = speed
        self.base_speed = speed
        self.comp = comp_list
        self.passive = passive
        self.crit_chance = crit_chance
        self.rarity = rarity
        self.elem = elem
        self.color = color
        self.flags = {'passive_ignored': False, 'switch_pou': False, 'switched_pou': False}
        self.active_buffs = {}  # stocke les buffs temporaires

    @classmethod
    def from_model(cls, owner, model_data):
        """Crée un Pou à partir d’un modèle de données."""
        pou =  cls(
            owner=owner,
            name=model_data["name"],
            hp=model_data["hp"],
            atk=model_data["atk"],
            speed=model_data["speed"],
            comp_list=model_data["skills"],
            passive=model_data["passive"],
            elem = model_data["elem"],
            rarity=model_data.get("rarity", "commun"),
            color=model_data["color"]
        )
        return pou

    def take_damage(self, amount):
        self.hp = max(self.hp - amount, 0)

    def is_alive(self):
        return self.hp > 0

    def verif_passive(self, call_type, **kwargs):
        """Déclenche un passif si son type correspond."""
        if self.passive:
            # Vérifie le type du passif
            passive_type = self.passive.trigger # ("OnAttack", "OnReceiveDamage"...)
            if call_type == passive_type:
                return self.passive.apply(user=self, **kwargs)

        return None

    def deal_damage(self, target, **kwargs):
        base_multiplier = kwargs.get("multiplier", 1.0)
        crit_chance = kwargs.get("crit_chance", self.crit_chance)
        crit_mult = kwargs.get("crit_mult", 1.25)
        miss = kwargs.get("miss", False)
        elem_mult = ELEMENT.get(self.elem, {}).get(target.elem, 1)
        set_target_hp = kwargs.get("set_target_hp", None)
        self_damage = kwargs.get("self_damage", 0)

        events = []

        # --- Passif d'attaque --- donc "OnAttack
        attack_passive_result = self.verif_passive('OnAttack', target=target, damage=0)
        if attack_passive_result:
            attack_passive_result['trigger'] = self.passive.trigger
            events.append(attack_passive_result)

        elem_efficacity = ''
        match elem_mult:
            case 1.5:
                elem_efficacity = "effective"
            case 0.5:
                elem_efficacity = "not_effective"

        # Calcul du critique
        is_crit = random.random() < crit_chance

        # Calcul des dégâts
        if miss or not target.is_alive():
            damage = 0
        elif set_target_hp is not None:
            damage = target.hp - set_target_hp
        else:
            damage = self.atk * base_multiplier * elem_mult

        # Coup critique
        if is_crit and set_target_hp is None:
            damage *= crit_mult

        damage = int(damage)

        # --- Passif défensif ---
        if damage > 0:
            defense_passive_result = target.verif_passive('OnReceiveDamage', target=target, damage=damage)
            if defense_passive_result and ("damage" in defense_passive_result):
                if not target.flags['passive_ignored']:
                    damage = defense_passive_result["damage"]
                    defense_passive_result['trigger'] = target.passive.trigger
                    events.append(defense_passive_result)
                target.flags['passive_ignored'] = False

        target.take_damage(damage)

        if self_damage > 0 and damage > 0:
            self.take_damage(amount=(self.hp * self_damage))
        return {
            "damage": damage,
            "is_crit": is_crit,
            "elem_efficacity": elem_efficacity,
            "events_passive": events
        }


    def add_buff(self, stat, factor, duration):
        """Applique un buff temporaire sur une statistique."""
        if stat not in ["stat", "atk"]:
            return

        # Applique immédiatement l’effet
        original = getattr(self, stat)
        new_value = original * factor
        setattr(self, stat, int(new_value))

        # Stocke le buff actif
        self.active_buffs[stat] = {
            "factor": factor,
            "duration": duration,
            "original": original
        }


    def update_buffs(self):
        """À appeler à chaque tour pour diminuer la durée des buffs."""
        expired = []
        events = []

        for effect_type, buff in self.active_buffs.items():
            buff["duration"] -= 1
            #Passage à match/case pour rendre l'ajout d'effets (buffs, soins, états spéciaux) plus flexible
            #Ex : new effect -> burn -> case 'burn' et c'est finit, pas de nouveaux param à rentrer ou quoi
            match effect_type:    
                case 'atk':
                    if buff["duration"] <= 0:
                        # Expiration → on restaure la valeur d’origine
                        setattr(self, effect_type, buff["original"])
                        expired.append(effect_type)
                        events.append({
                            "type_buff": "atk",
                        })

                case 'regen':
                    amount = buff['amount']
                    #Pour éviter de dépasser la limite d'hp
                    if self.hp > 0:
                        self.hp = min(self.hp + amount, self.max_hp)
                        if buff["duration"] <= 0:
                            expired.append(effect_type)
                        events.append({
                            "type_buff": "regen",
                            "amount": amount,
                        })
                
                case 'burn':
                    amount = buff['amount']
                    if self.hp > 0:
                        burn_damage = int((self.max_hp * amount)+0.5)
                        self.take_damage(burn_damage)
                        if buff["duration"] <= 0:
                            expired.append(effect_type)
                        events.append({
                            "type_buff": "burned",
                            "amount": amount,
                            "turn_damage" : burn_damage,
                        })

                case 'poison':
                    amount = buff['amount']
                    if 'toxic_cpt' not in buff:
                        buff['toxic_cpt'] = 0
                    cpt = buff['toxic_cpt']
                    if self.hp > 0:
                        poison_damage = int((self.max_hp * amount * cpt)+0.5)
                        buff['toxic_cpt'] += 1
                        self.take_damage(poison_damage)
                        if buff["duration"] <= 0:
                            expired.append(effect_type)
                        events.append({
                            "type_buff": "poisoned",
                            "amount": amount*cpt,
                            "turn_damage" : poison_damage,
                        })

                case 'sleep':
                    if random.random() < buff['chance_to_stop']:
                        expired.append(effect_type)
                    if buff["duration"] <= 0:
                            expired.append(effect_type)
                    events.append({
                            "type_buff": "asleep"
                        })

        # Supprimer les buffs expirés
        for effect_type in expired:
            del self.active_buffs[effect_type]

        return {
            "events": events,
            "user": self,
        }


    def add_heal(self, stat, amount, duration, skill_name=""):
        '''Heal qui dure sur plusieurs tours'''
        if stat not in ["stat", "hp"]:
                    return
        
        self.active_buffs['regen'] = {
            "amount": amount,
            "duration": duration,
            "skill_name": skill_name #sinon je vois pas comment récup le nom de la compétence ici, si tu sais faire modifies
        }

    def add_status_effect(self, status_name, status_data):
        buff_data= status_data.copy()
        buff_data['type'] = 'status'
        self.active_buffs[status_name] = buff_data
