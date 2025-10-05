#competences.py
import random
import time

class Skill:
    def __init__(self, name, description):
        self.name = name
        self.description = description

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

        for i in range(hits):
            damage, crit = user.deal_damage(target, **self.kwargs)
            total_damage += damage
            crit_txt = " (Critique!)" if crit else ""
            messages.append(f"Coup {i+1}: {damage} dmg{crit_txt}")

        return (
            f"{user.owner} utilise {self.name} !\n"
            + "\n".join(messages)
            + f"\nTotal: {total_damage} dégâts."
        )





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