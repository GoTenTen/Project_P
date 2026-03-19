import random

class bot:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

    def get_action(self, attacker, defender):
        idx = 1
        print(attacker.comp[idx].__class__.__name__)
        return {"attacker": attacker, "defender": defender, "comp_idx": idx}



