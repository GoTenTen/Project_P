# team_creation.py
from Project_P.core.pou import Pou
from Project_P.data.pou_list import PouModels
from Project_P.core.team import Team

'''
def create_team(owner_name):
    pou_list = [Pou.from_model(owner_name, model) for model in PouModels.values()]
    return Team(owner_name, pou_list)
'''

RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"


def create_team(owner_name):
    choice_list = [Pou.from_model(owner_name, model) for model in PouModels.values()]
    x = str(input("Voulez vous créer votre propre équipe ou en générer une aléatoirement ?\n\n     1 : Créez votre propre équipe !\n\n     2 : Générer une équipe (En dev)\n\n"))
    while (x != '1') and (x != '2'):
        x = int(input("Veuillez choisir une valeur valide : 1 ou 2.\n"))
    if x == '2':
        pass
    else:
        while True:
            pou_list = [] * 2
            # Avec enumerate on peut parcourir une liste et récupérer facielemnt à la fois index et valeur
            for i, pou in enumerate(choice_list, 1):
                print(f"{i} : {pou.name} | {RED}Hp : {pou.hp}{RESET} | {BLUE}Atk : {pou.atk}{RESET}")
            while len(pou_list) < 2:
                c = int(input('Choississez le pou que vous voulez : \n')) - 1
                pou_list.append(choice_list[c])
            show_team(pou_list)
            #si 'o' on retourne dans le 'while true' et ça vide la pou_list, si 'n' on break et on renvoie la team comme la fonction se doit de le faire
            confirm = str(input("Voulez vous modifier votre équipe ? (o/n)"))
            if confirm == 'n':
                break
    return pou_list

def show_team(pou_list):
    print("\nPous sélectionnés pour l'équipe :\n")
    for pou in pou_list:
        print(f"- {pou.name}")

def random_team(pou_list):
    pass


player1 = 'test'

create_team(player1)
