# team_creation.py
from Project_P.core.pou import Pou
from Project_P.data.pou_list import PouModels
from Project_P.core.team import Team
from Project_P.ui.display import *
import random

'''
def create_team(owner_name):
    pou_list = [Pou.from_model(owner_name, model) for model in PouModels.values()]
    return Team(owner_name, pou_list)
'''


RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

TAUX_DROP={
    'commun':0.5,
    'rare':0.35,
    'épic':0.1,
    'légendaire':0.05
}

def create_team(owner_name): #lenT à rajouter -> 1 pour mes tests de comp plus rapide
    #Si tu veux implémenter le taux de drop sur la création de team juste créer une list = random_team(choice_list, TAUX_DROP, et len que tu veux)
    lenT = 3
    basic_list = [Pou.from_model(owner_name, model) for model in PouModels.values()]
    choice_list = random_team([Pou.from_model(owner_name, model) for model in PouModels.values()], TAUX_DROP, lenT)
    x = str(input("Voulez vous créer votre propre équipe ou en générer une aléatoirement ?\n\n     1 : Créez votre propre équipe !\n\n     2 : Générer une équipe (En dev)\n\n"))
    while (x != '1') and (x != '2'):
        x = str(input("Veuillez choisir une valeur valide : 1 ou 2.\n"))
    if x == '2':
        pou_list = random_team(basic_list, TAUX_DROP, lenT)
        show_more(pou_list,1)
    else:
        while True:
            pou_list = []
            # Avec enumerate on peut parcourir une liste et récupérer facielemnt à la fois index et valeur
            for i, pou in enumerate(choice_list, 1):
                print(f"{i} : {pou.name} | {RED}Hp : {pou.hp}{RESET} | {BLUE}Atk : {pou.atk}{RESET}")
            while len(pou_list) < lenT:
                c = int(input('Choississez le pou que vous voulez : \n')) - 1
                while (c < 1) or (c > 5):
                    c = int(input('Veuillez choisir une valeur valide, un chiffre de 1 à 5 : \n')) - 1
                pou_list.append(choice_list[c])
            show_more(pou_list,2)
            #si 'o' on retourne dans le 'while true' et ça vide la pou_list, si 'n' on break et on renvoie la team comme la fonction se doit de le faire
            confirm = str(input("Voulez vous modifier votre équipe ? (o/n)"))
            if confirm == 'n':
                break
    return Team(owner_name,pou_list)


#show_more et recup_flag purement optionnel mais rajoute un petit truc quand tu random_team

#Cette fonction vient déterminer la rareté la plus haute dans la team
def recup_flag(pou_list):
    f = 1
    for pou in pou_list:
        rarity = getattr(pou, 'rarity', None)
        match rarity:
            # Pour chaque pou, on associe un niveau de rareté à un chiffre :
            # commun = 1, rare = 2, épic = 3, légendaire = 4
            # puis on garde la valeur la plus élevée rencontrée avec max(f, valeur)
            case 'commun':
                f = max(f, 1)
            case 'rare':
                f = max(f, 2)
            case 'épic':
                f = max(f, 3)
            case 'légendaire':
                f = max(f, 4)
    return f


def random_team(pou_list, TAUX_D, lenT):#lenT -> variable pour len Team
    random_list = []
    while (len(random_list) < lenT):
        drop_rate = random.random()
        if drop_rate < TAUX_D.get('légendaire', 0):
            rara = 'légendaire'
        elif drop_rate < TAUX_D.get('épic', 0):
            rara = 'épic'
        elif drop_rate < TAUX_D.get('rare', 0):
            rara = 'rare'
        else:
            rara = 'commun'
        rarity_sort = []
        for pou in pou_list:
            if getattr(pou, 'rarity', None) == rara:
                rarity_sort.append(pou)
        random_list.append(random.choice(rarity_sort))
    return random_list
    





'''
def random_team(pou_list):
    return random.sample(pou_list, 2)
'''



