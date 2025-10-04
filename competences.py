#competences.py
import random

class Competence:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def apply(self, user, target):
        raise NotImplementedError("Cette compétence n'est pas encore définie.")

class TapeFort(Competence):
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
        return f"{user.owner} utilise {self.name} : ATK passe de {before} à {user.atk}."


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
        return f"{user.owner} a frappé {hits} fois et a infligé {total_damage} dégats!"