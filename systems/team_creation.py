# team_creation.py
from Project_P.core.pou import Pou
from Project_P.data.pou_list import PouModels
from Project_P.core.team import Team
import random

'''
def create_team(owner_name):
    pou_list = [Pou.from_model(owner_name, model) for model in PouModels.values()]
    return Team(owner_name, pou_list)
'''


RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"


TAUX_DROP = {
    "commun" : 0.50,
    "rare" : 0.35,
    "épique" : 0.10,
    "légendaire" : 0.05
}

def create_team(owner_name, len_team=3):
    choice_list = random_team([Pou.from_model(owner_name, model) for model in PouModels.values()])

    while True:
        pou_list = []
        # Avec enumerate on peut parcourir une liste et récupérer facielemnt à la fois index et valeur
        for i, pou in enumerate(choice_list, 1):
            print(f"{i} : {pou.name} | {RED}Hp : {pou.hp}{RESET} | {BLUE}Atk : {pou.atk}{RESET}")
        while len(pou_list) < len_team:
            c = int(input('Choississez le pou que vous voulez : \n')) - 1
            pou_list.append(choice_list[c])
        show_team(pou_list)
        #si 'o' on retourne dans le 'while true' et ça vide la pou_list, si 'n' on break et on renvoie la team comme la fonction se doit de le faire
        confirm = str(input("Voulez vous modifier votre équipe ? (o/n)"))
        if confirm == 'n':
            break
    return Team(owner_name,pou_list)

def show_team(pou_list):
    print("\nPous sélectionnés pour l'équipe :\n")
    for pou in pou_list:
        print(f"- {pou.name}")

def random_team(pou_list, len_pool=5):
    all_names = list(PouModels.keys())

    for name in all_names:
        TAUX_DROP.get(PouModels[name].get("rarity", "commun"), 1)

    return random_list




