# team_creation.py
from Project_P.core.pou import Pou
from Project_P.data.pou_list import PouModels
from Project_P.ui.display import display_manager
from Project_P.core.team import Team
import random

TAUX_DROP={
    'commun':0.5,
    'rare':0.35,
    'épic':0.1,
    'légendaire':0.05
}

def create_team(owner_name):
    len_team = 3
    while True:
        display_manager('display_input_create_team', player=owner_name)
        display_manager('display_input', cas=1)
        choice = str(input())
        while choice not in ('1', '2'):
            display_manager('invalid', cas=1)
            choice = str(input())
        break
    basic_list = [Pou.from_model(owner_name, model) for model in PouModels.values()]
    match choice:
        case '1':
            len_pool = 5
            while True:
                choice_list = random_team(basic_list, TAUX_DROP, len_pool)
                poupou_list = create_manual_team(choice_list, len_team)
                if modif_confirm_team():
                    break
        case '2':
            poupou_list = create_random_team(owner_name, basic_list, len_team)
    return Team(owner_name, poupou_list)


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
            case 'rare':
                f = max(f, 2)
            case 'épic':
                f = max(f, 3)
            case 'légendaire':
                f = max(f, 4)
    return f

def create_manual_team(choice_list, lenT):
    res = []
    display_manager('show_more', pou_list = choice_list, cas=1)
    while len(res) < lenT:
        try:
            #Le try sert à éviter les erreurs et englobler TOUTES les situations non précisé, ex ici si il se retrouve à faire int('abc')
            #Il ne va pas exécuter touuuut le bloc d'en dessous et skip jusqu'à 'except ValueError'
            display_manager('display_input', cas=3)
            choose = int(input())
            if 1 <= choose <= len(choice_list):
                if choice_list[choose-1] in res:
                    display_manager('invalid', cas=3)
                else:                                   
                    res.append(choice_list[choose-1])
            else:
                display_manager('invalid', cas=1)
        except ValueError:
            #Ici, après avoir exécuté ce qu'on lui dit de faire donc le displya_manager, il va simplement donner le go au while pour repartir
            #En gros, il vient gérer les cas d'erreur dans la boucle ou il se trouve et va EVITER cette erreur afin de pouvoir réitérer
            display_manager('invalid', cas=1) 
    display_manager('show_more', pou_list=res, cas=2)
    return res


def create_random_team(owner_name, pou_list, lenT):
    random_list = random_team(pou_list, TAUX_DROP, lenT)
    display_manager('show_more', pou_list=random_list, cas=1)
    return random_list


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


def modif_confirm_team():
    display_manager('display_input', cas=4)
    confirm = str(input()).lower()
    while confirm not in ('oui', 'o', 'n', 'non'):
        display_manager('invalid', cas=1)
        confirm = str(input()).lower()
    if confirm in ( 'n', 'non'):
        return True
    else:
        return False