#team.py
import time


class Team:
    def __init__(self, owner_name, pou_list):
        self.owner = owner_name
        self.pous = pou_list
        self.active_index = 0 #index de quel pou est actif dans la liste

    def show_all_pou_stats(self):
        print(f"\n    [[{self.owner}]]")
        for pou in self.pous:
            actif = "" if pou.hp > 0 else " (KO)"
            print(f"       - {pou.name}{actif} : {pou.hp}/{pou.max_hp} PV | {pou.atk} ATK")

    def get_active_pou(self):
        return self.pous[self.active_index]

    def is_alive(self):
        return any(pou.hp > 0 for pou in self.pous)

    def switch_pou(self, new_index):
        if 0 <= new_index < len(self.pous) and self.pous[new_index].hp > 0:
            self.active_index = new_index
            print(f"{self.owner} change pour {self.get_active_pou().name} !")
            return True
        else:
            print("Choix invalide ou Pou KO.")
            return False

    def choose_next_pou(self):
        print(f"{self.get_active_pou().owner} choisissez un autre Pou :\n")
        for i, pou in enumerate(self.pous):
            status = "(ACTIF)" if i == self.active_index else ""
            print(f"{i + 1}. {pou.name} {status} - PV: {pou.hp}/{pou.max_hp}")

        while True:
            choix = input("Choisissez un Pou par numéro : ")
            if choix.isdigit():
                idx = int(choix) - 1
                if self.switch_pou(idx):
                    break
            print("Choix invalide, réessayez.")

    def handle_death_and_switch(self):
        if not self.get_active_pou().is_alive():
            print(f"{self.get_active_pou().name} de {self.get_active_pou().owner} perd connaissance.\n")
            time.sleep(1)
            self.choose_next_pou()

    def show_team_status(self):
        print(f"Équipe de {self.owner} :")
        for i, pou in enumerate(self.pous):
            actif = "(ACTIF)" if i == self.active_index else ""
            print(f"  {i + 1}. {pou.name} {actif} - PV: {pou.hp}/{pou.max_hp} ATK: {pou.atk}")
        print("")