#pou.py
import random

class Pou:
    def __init__(self, owner, name, hp, atk, comp_list, rarity, crit_chance=0.1):
        self.owner = owner
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.base_atk = atk
        self.comp = comp_list
        self.crit_chance = crit_chance
        self.rarity = rarity
        self.active_buffs = {}  # stocke les buffs temporaires

    @classmethod
    def from_model(cls, model_data, owner):
        """Crée un Pou à partir d’un modèle de données."""
        pou = cls(
            owner=owner,
            name=model_data["name"],
            hp=model_data["hp"],
            atk=model_data["atk"],
            comp_list=model_data["skills"],
            rarity=model_data.get("rarity", "commun")  # ✅ Ajouté ici !
        )

        return pou

    def take_damage(self, amount):
        self.hp = max(self.hp - amount, 0)

    def is_alive(self):
        return self.hp > 0

    def heal(self, amount):
        healed = min(amount, self.max_hp - self.hp)
        self.hp += healed
        return f"{self.name} récupère {healed} PV. (PV actuels: {self.hp})"

    def deal_damage(self, target, **kwargs):
        base_multiplier = kwargs.get("multiplier", 1.0)
        crit_chance = kwargs.get("crit_chance", self.crit_chance)
        crit_mult = kwargs.get("crit_mult", 1.25)
        element_bonus = kwargs.get("element_bonus", 1.0)
        flat_bonus = kwargs.get("flat_bonus", 0)
        accuracy = kwargs.get("accuracy", 1)

        # Calcul du critique
        is_crit = random.random() < crit_chance
        if random.random() < accuracy:
            damage = self.atk * base_multiplier * element_bonus + flat_bonus
        else:
            damage = 0
            print("raté!\n")
        if is_crit:
            damage *= crit_mult

        damage = int(damage)
        target.take_damage(damage)
        return damage, is_crit


    def add_buff(self, stat, factor, duration):
        """Applique un buff temporaire sur une statistique."""
        if stat not in ["atk", "hp"]:
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

        for stat, buff in self.active_buffs.items():
            buff["duration"] -= 1
            if buff["duration"] <= 0:
                # Expiration → on restaure la valeur d’origine
                setattr(self, stat, buff["original"])
                expired.append(stat)
                print(f"L’effet sur {stat.upper()} de {self.name} s’est dissipé.")

        # Supprimer les buffs expirés
        for stat in expired:
            del self.active_buffs[stat]

