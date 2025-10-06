#skills.py
import random
import time

class Skill:
    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description
        self.kwargs = kwargs

    def apply(self, user, target):
        raise NotImplementedError("Cette compétence n'est pas encore définie.")


class AttackSkill(Skill):
    def __init__(self, name, description, **kwargs):
        super().__init__(name, description)
        self.kwargs = kwargs  # stocke les paramètres de dégâts

    def apply(self, user, target):
        total_damage = 0
        messages = []
        hits = self.kwargs.get("multi_hit", 1)
        bonus_message = self.kwargs.get("bonus_message", None)

        # message standard
        print(f"{user.owner} utilise {self.name} !")

        # message bonus optionnel
        if bonus_message:
            time.sleep(1)
            print(f"\n{bonus_message}\n")
            time.sleep(1)

        for i in range(hits):
            damage, crit = user.deal_damage(target, **self.kwargs)
            total_damage += damage
            crit_txt = " (Critique!)" if crit else ""
            # Texte différent selon si multi-hit ou non
            if hits > 1:
                print(f"Coup {i + 1}: {damage} dmg{crit_txt}")
                time.sleep(1)
            else:
                print(crit_txt)

        return f"{user.name} de {user.owner} à infligé {total_damage} dégâts à {target.name} de {target.owner}."


class BuffSkill(Skill):
    """Compétence de buff."""
    def apply(self, user, target=None):
        stat = self.kwargs.get("stat", "atk")
        factor = self.kwargs.get("factor", 2.0)
        before = getattr(user, stat)
        setattr(user, stat, int(before * factor))
        return f"{user.owner} utilise {self.name} : {stat.upper()} passe de {before} à {getattr(user, stat)} !"

class TimedBuffSkill(BuffSkill):
    def apply(self, user, target=None):
        stat = self.kwargs.get("stat", "atk")
        factor = self.kwargs.get("factor", 1.5)
        duration = self.kwargs.get("duration", 3)

        user.add_buff(stat, factor, duration)
        return f"{user.name} de {user.owner} utilise {self.name} : {stat.upper()} augmenté pour {duration} tours !"

class HealSkill(Skill):
    """Compétence de soin."""
    def __init__(self, name, description, amount):
        super().__init__(name, description)
        self.amount = amount

    def apply(self, user, target=None):
        return user.heal(self.amount)




"""class TapeFort(Competence):
    def __init__(self):
        super().__init__("Tape Fort", "Une attaque puissante infligeant le double des dégats de l'utilisateur.")

    def apply(self, user, target):
        damage = user.atk * 2
        target.take_damage(damage)
        return f"{user.owner} utilise {self.name} et inflige {int(damage)} dégâts."

class DanseLame(Competence):
    def __init__(self):
        super().__init__("Danse Lame", "L'utilisateur danse pour se donner du courage et voit son attaque doubler.")

    def apply(self, user, target=None):
        before = user.atk
        user.atk *= 2
        return f"{user.owner} utilise {self.name} : son ATK passe de {before} à {user.atk}."

class Heal(Competence):
    def __init__(self):
        super().__init__("Heal", "L'utilisateur se soigne pour récupérer 10 PV..")

    def apply(self, user, target=None):
        heal_amount = min(10, user.max_hp - user.hp)
        user.hp += heal_amount
        return f"{user.owner} utilise {self.name} : il récupère {heal_amount} PV."

class SlapThatAss(Competence):
    def __init__(self):
        super().__init__("Slap That Ass", "Une attaque pleine de vice pouvant frapper les fesses de  l'utilisateur 1 à 5 fois.")

    def apply(self, user, target):
        hits = random.randint(1,5)
        total_damage = 0

        for i in range(hits):
            target.take_damage(user.atk)
            total_damage += user.atk
            print(f"{user.owner} frappe {i + 1} fois!")
            time.sleep(0.8)
        return f"\n{user.owner} a frappé {hits} fois et a infligé {total_damage} dégats!\n"""