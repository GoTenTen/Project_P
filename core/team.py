#team.py
import time


class Team:
    def __init__(self, owner_name, pou_list):
        self.owner = owner_name
        self.pous = pou_list
        self.active_index = 0 #index de quel pou est actif dans la liste

    def get_active_pou(self):
        return self.pous[self.active_index]

    def is_alive_team(self):
        return any(pou.hp > 0 for pou in self.pous)

    def can_switch(self, index: int) -> bool:
        # fonction pour verif si le pou choisi est bien "switchable"
        if not (0 <= index < len(self.pous)):
            return False
        if self.pous[index].hp <= 0:
            return False
        return True

    def switch_pou(self, index: int):
        if not self.can_switch(index):
            return False
        self.active_index = index
        return True

    def handle_death_and_switch(self):
        if not self.get_active_pou().is_alive():
            print(f"{self.get_active_pou().name} de {self.get_active_pou().owner} perd connaissance.\n")
            time.sleep(1)
            return {"next_step": "switch_pou"}
        return {"next_step": ""}
