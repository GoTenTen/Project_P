import random

class bot:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

    def get_action(self, attacker, defender):
        idx = random.randint(0, 3)
        return {"attacker": attacker, "defender": defender, "comp_idx": idx}
