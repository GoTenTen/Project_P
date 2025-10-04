#class_poukemon.py

class Pou:
    def __init__(self, owner, name, hp, atk, comp_list):
        self.owner = owner
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.comp = comp_list

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp = max(self.hp - amount, 0)