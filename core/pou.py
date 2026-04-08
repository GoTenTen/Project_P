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
        #Major_status devrait être un dictionnaire seul, pour des soucis de complexité de code inutile, il sera une liste contenant qu'un seul élément 
        self.effects = {"buffs" : [], "debuffs" : [], "major_status" : [], "minor_status" : []}

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
        self.effects["buffs"].append({
            "stat": stat,
            "factor": factor,
            "duration": duration,
            "original": original
        })


    def update_buffs_status(self):
        """À appeler à chaque tour pour diminuer la durée des buffs."""
        expired = []
        events = []

        for effects, data in self.effects.items():
            if not (data):
                continue

            #Parcours de chaque listes  pour enlever 1 à la duration de chaque élément en ayant une
            for effect in data:
                effect["duration"] -= 1

                match effects:
                    case "major_status" | "minor_status":
                        status_ev = self.handle_status(effect["name"], effect)
                        #verif de secu pour ajouter quelque chose de vide
                        if status_ev:
                            events.extend(status_ev)

                    case "buffs":
                        match effect["stat"]:
                            case "regen":
                                self.hp = min(self.hp + effect["amount"], self.max_hp)
                                events.append({"amount": effect["amount"]})
                                
                            case 'atk':
                                if effect["duration"] <= 0:
                                    buff_ev = self.handle_buffs(effect)
                                    if buff_ev:
                                        events.append(buff_ev)
                if effect["duration"] <= 0:
                    if effects not in expired:
                        expired.append((effects, effect))

        # Supprimer les buffs expirés
        for effects, effect in expired:
            self.effects[effects].remove(effect)

        return {
            "events": events,
            "user": self,
        }
    
    def handle_buffs(self, buff):
        #récup le nom du buff
        buff_name = buff.get('stat')

        #Mesure de sécu, on vérifie bien si original est là ainsi que le buff en question, si oui -> on reset
        if buff_name and "original" in buff:
            setattr(self, buff_name, buff["original"])

        return {"type_buff" : buff_name}


    def handle_status(self, status, values):
        status_events = []

        amount = values.get('amount', 0)
        event_data = {
            "status" : status,
        }

        match status:
            case "burn":
                #to do : divise l'attaque par 2
                pass

            case "poison":
                if "toxic_cpt" not in values:
                    values["toxic_cpt"] = 1
                amount = amount*values["toxic_cpt"]
                values["toxic_cpt"] += 1

            case 'sleep':
                if (random.random() < values['chance_to_stop']):
                    values["duration"] = 0
        
        status_damage = int(self.max_hp * amount)
        
        #création des valeurs de bases du dictionnaire sauf cas excpetionnel
        if event_data:
            if amount > 0:
                event_data.setdefault("amount", int(amount))
            if status_damage > 0:
                event_data["turn_damage"] = status_damage
                self.take_damage(status_damage)
            status_events.append(event_data)

        return status_events


    def add_heal(self, stat, amount, duration, skill_name=""):
        '''Heal qui dure sur plusieurs tours'''
        if stat not in ["stat", "hp"]:
                    return
        
        self.effects["buffs"].append({
            "name": "regen",
            "amount": amount,
            "duration": duration,
            "skill_name": skill_name
        })

    def add_status_effect(self, status_name, status_data):
        buff_data= status_data.copy()
        buff_data['type'] = 'status'
        buff_data["name"] = status_name
        if status_name in ["poison", "burn", "sleep"]:
            self.effects["major_status"].append(buff_data)