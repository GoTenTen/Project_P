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
    if x == 'n':
        return {'next_step' : 'NO_RECALL'}
    else:
        return {'next_step' : 'RECALL'}
    
'''def check_sub(str_numb):
    str_stack = []
    str_sub = []
    str_res = ''
    for i in str_numb:
        if i in str_stack:
            str_sub.append(i)
        else:
            str_stack.append(i)  Mdr je la laisse pour l'effort jme suis rendu compte que je pouvais faire plus simple je suis deg
    str_res = ''.join(str_stack)
    if len(str_sub)==0:
        return str_res
    else:
        str_sub = ', '.join(str_sub)
        return str_res, str_sub'''


def create_team(owner_name):
    basic_list = [Pou.from_model(owner_name, model) for model in PouModels.values()]
    choice_list = random_team(basic_list, TAUX_DROP, 5)
    poupou_list = []
    choose_number = []
    Taille_Que_Tu_Souhaites_My_Love_T_As_Vu_Pycharm_Je_Respecte_Les_Conventions_Mais_La_J_Imagine_Que_Tu_Vas_Dire_Que_Le_Nom_Est_Beaucoup_Beaucoup_Trop_Long_Et_Si_C_Est_Le_Cas_Je_Comprends = 3
    while True:
        display_manager('display_input', cas=1)
        choice = str(input())
        while choice not in ('1', '2'):
            display_manager('invadlid')
        break
    match choice:
        case '1':
            while True:
                display_manager('show_more', pou_list = choice_list)
                while len(choose_number)<Taille_Que_Tu_Souhaites_My_Love_T_As_Vu_Pycharm_Je_Respecte_Les_Conventions_Mais_La_J_Imagine_Que_Tu_Vas_Dire_Que_Le_Nom_Est_Beaucoup_Beaucoup_Trop_Long_Et_Si_C_Est_Le_Cas_Je_Comprends:
                    print("Quel pou choisissez vous ?\n")
                    x = int(input())
                    if x not in choose_number:
                        choose_number.append(x)   #rajouter des prints
                    else:
                        display_manager('invalid')
                        continue
                poupou_list = make_team(basic_list, choice_list, choice, choose_number, Taille_Que_Tu_Souhaites_My_Love_T_As_Vu_Pycharm_Je_Respecte_Les_Conventions_Mais_La_J_Imagine_Que_Tu_Vas_Dire_Que_Le_Nom_Est_Beaucoup_Beaucoup_Trop_Long_Et_Si_C_Est_Le_Cas_Je_Comprends)
                print("Voulez vous modifier votre team ?\n")
                confirm = str(input())
                step = recall_make_team(confirm)
                if step['next_step'] == ['NO_RECALL']:
                    break
        case '2':
            display_manager('show_more', pou_list=choice_list, cas=1)
            return Team(owner_name,choice_list)
    return Team(owner_name, poupou_list)




'''
def random_team(pou_list):
    return random.sample(pou_list, 2)
'''



