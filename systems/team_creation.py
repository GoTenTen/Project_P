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

TAUX_DROP={
    'commun':0.5,
    'rare':0.35,
    'épic':0.1,
    'légendaire':0.05
}

def create_team(owner_name ): #lenT à rajouter
    choice_list = [Pou.from_model(owner_name, model) for model in PouModels.values()]
    lenT = 5
    x = str(input("Voulez vous créer votre propre équipe ou en générer une aléatoirement ?\n\n     1 : Créez votre propre équipe !\n\n     2 : Générer une équipe (En dev)\n\n"))
    while (x != '1') and (x != '2'):
        x = int(input("Veuillez choisir une valeur valide : 1 ou 2.\n"))
    if x == '2':
        pou_list = random_team(choice_list, TAUX_DROP, lenT)
        show_more(pou_list,1)
    else:
        while True:
            pou_list = []
            # Avec enumerate on peut parcourir une liste et récupérer facielemnt à la fois index et valeur
            for i, pou in enumerate(choice_list, 1):
                print(f"{i} : {pou.name} | {RED}Hp : {pou.hp}{RESET} | {BLUE}Atk : {pou.atk}{RESET}")
            while len(pou_list) < lenT:
                c = int(input('Choississez le pou que vous voulez : \n')) - 1
                pou_list.append(choice_list[c])
            show_more(pou_list,2)
            #si 'o' on retourne dans le 'while true' et ça vide la pou_list, si 'n' on break et on renvoie la team comme la fonction se doit de le faire
            confirm = str(input("Voulez vous modifier votre équipe ? (o/n)"))
            if confirm == 'n':
                break
    return Team(owner_name,pou_list)

def show_team(pou_list):
    for pou in pou_list:
        print(f"- {pou.name}")

def show_more(pou_list, cas):
    cas2 = recup_flag(pou_list, TAUX_DROP)
    match cas:
        case 1:
            match cas2:
                case 1:
                    print("\nLes étoiles se sont alignées... Ou pas...\nVoici ton équipe :\n")
                    show_team(pou_list)
                case 2:
                    print("\nLes étoiles se sont alignées... Ou presque...\nVoici ton équipe :\n")
                    show_team(pou_list)
                case 3:
                    print("\nLes étoiles se sont alignées ! Regarde moi cette équipe :\n")
                    show_team(pou_list)
                case 4:
                    print("\nDios mio abberant le taux de drop guette :\n")
                    show_team(pou_list)
        case 2:
            print("\nVoici votre équipe :\n")
            show_team(pou_list)

def recup_flag(pou_list, TAUX_D):
    f = 1
    for pou in pou_list:
        rarity = getattr(pou, 'rarity', None)
        match rarity:
            case 'commun' if TAUX_D.get(rarity, 0) < f:
                f == 0.5
            case 'rare' if TAUX_D.get(rarity, 0) < f:
                f == 0.35
            case 'épic' if TAUX_D.get(rarity, 0) < f:
                f == 0.1
            case 'légendaire' if TAUX_D.get(rarity, 0) < f:
                f == 0.05
    return f


def random_team(pou_list, TAUX_D, lenT):
    random_list = []
    nb_tours = 100
    cpt_tours = 0
    while (len(random_list) < lenT) and cpt_tours < nb_tours:
        cpt_tours += 1
        for pou in pou_list:
            if pou in random_list:
                continue
            else:
                rarity = getattr(pou, 'rarity', None)
                if random.random() < TAUX_D.get(rarity, 0):
                    random_list.append(pou)
                    if (len(random_list) >= lenT) or (nb_tours <= cpt_tours):
                        break
    return random_list



'''
def random_team(pou_list):
    return random.sample(pou_list, 2)
'''



