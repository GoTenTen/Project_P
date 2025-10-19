# team_creation.py
from Project_P.core.pou import Pou
from Project_P.data.pou_list import PouModels
from Project_P.core.team import Team
from Project_P.ui.display import *
import random

RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

TAUX_DROP={
    'commun':0.5,
    'rare':0.35,
    'épic':0.1,
    'légendaire':0.05
}

def make_team(basic_list, choice_list, x, choose_list, lenT): #lenT à rajouter -> 1 pour mes tests de comp plus rapide
    if x == '2':
        pou_list = random_team(basic_list, TAUX_DROP, lenT)
        show_more(pou_list,1)
    else:
        pou_list = []
        for z in choose_list:
            pou_list.append(choice_list[z-1])
        show_more(pou_list,2)
    return pou_list


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
            if pou not in random_list and getattr(pou, 'rarity', None) == rara:
                rarity_sort.append(pou)
        if rarity_sort:
            random_list.append(random.choice(rarity_sort))
        else:
            continue
    return random_list
    
def recall_make_team(x):
    if x in ('n', 'non'):
        return {'next_step' : 'NO_RECALL'}
    else:
        return {'next_step' : 'RECALL'}

def create_team(owner_name):
    len_team = 3
    while True:
        display_manager('display_input_create_team', player=owner_name)
        display_manager('display_input', cas=1)
        choice = str(input())
        while choice not in ('1', '2'):
            display_manager('invalid', cas=1)
        break
    basic_list = [Pou.from_model(owner_name, model) for model in PouModels.values()]
    choice_list = random_team(basic_list, TAUX_DROP, len_team)
    match choice:
        case '1':
            len_pool = 5
            while True:
                choose_number = []
                choice_list = random_team(basic_list, TAUX_DROP, len_pool)
                display_manager('show_more', pou_list = choice_list, cas=1)
                while len(choose_number)<len_team:
                    print("\nQuel pou choisissez vous ?\n")
                    x = int(input())
                    if x not in choose_number:
                        choose_number.append(x)   #rajouter des prints
                    else:
                        display_manager('invalid', cas=1)
                        continue
                poupou_list = make_team(basic_list, choice_list, choice, choose_number, len_team)
                print("Voulez vous modifier votre team ?\n")
                confirm = str(input()).lower()
                while confirm not in ('oui', 'o', 'n', 'non'):
                    display_manager('invalid')
                    confirm = str(input()).lower()
                step = recall_make_team(confirm)
                if step['next_step'] == 'NO_RECALL':
                    break
        case '2':
            display_manager('show_more', pou_list=choice_list, cas=1)
            return Team(owner_name,choice_list)
    return Team(owner_name, poupou_list)


