#display.py
from Project_P.core.pou import *
import time



def display_manager(event, **data):
    match event:
        case 'choose_action':
            attacker = data['attacker']
            team_attacker = data['team_attacker']
            cas = data['cas']
            display_action(attacker, team_attacker)
            display_input(cas)
        
        case 'show_team':
            pou_list = data['pou_list']           
            show_team(pou_list)
        
        case 'show_more':
            pou_list = data['pou_list']
            cas = data['cas']          
            show_more(pou_list, cas)
        
        case 'display_text_drop':
            cas = data['cas']
            display_text_drop(cas)
        
        case 'description':
            attacker = data['attacker']       
            display_description(attacker)
        
        case 'invalid':            
            display_invalid()
        
        case 'display_sleep':
            cas = data['cas'] 
            display_sleep(cas)

        case 'display_comp':
            attacker = data['attacker']
            display_comp(attacker)

        case 'display_starter':
            p1, p2 = data['p1'], data['p2']
            display_starter(p1, p2)

        case 'display_sleep':
            cas = data['cas']
            display_sleep(cas)

        case 'display_input':
            cas = data['cas']
            display_input(cas)

        case _:
            print(f'\n event : {event} est inconnu\n')


def display_all(text):
    [print(x) for x in text]


def display_action(attacker, team_attacker):
    choice_action = [f"C'est au tour de {team_attacker.owner} avec {attacker.name} !",
                    "1 - Attaquer",
                    "2 - Description des compétences",
                    "3 - Changer de Pou"]
    display_all(choice_action)

def display_input(cas):
    text = []
    match cas:
        case 1:
            text = 'Que voulez vous faire ?'
        case 2:
            text = 'Votre choix :'
    print(text, end='', flush=True)

def display_invalid():
    display_all(["Choix invalide, réessaie."])


def display_starter(p1, p2):
    start = []
    display_all([f"Qui commence entre {p1} et {p2} ?\n"])
    display_sleep()
    match random.randint(1,2):
        case 1:
            start = [f"C'est {p1} qui commence !\n"]
        case 2:
            start = [f"C'est {p2} qui commence !\n"]
    display_all(start)


def display_sleep():#cas à ajouter si -> match case
    '''match cas:
        case '1':''' #Si on décide d'utiliser plusieurs affichage de ce style, on aura juste à ajouter un case (et ptet modifier le nom de la fonction)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(1)
    print("\n") 


def display_text_drop(cas):
    match cas:
        case 1:
            print("\nLes étoiles se sont alignées... Ou pas...\nVoici ton équipe :\n")
        case 2:
            print("\nLes étoiles se sont alignées... Ou presque...\nVoici ton équipe :\n")
        case 3:
            print("\nLes étoiles se sont alignées ! Regarde moi cette équipe :\n")
        case 4:
            print("\nDios mio abberant le taux de drop guette :\n")


def show_team(pou_list):
    text = [f"- {pou.name}" for pou in pou_list]
    display_all(text)


#Affiche un message différent par rapport à la rareté la plus haute + affiche la team
def show_more(pou_list, cas):
    from Project_P.systems.team_creation import recup_flag 
    cas2 = recup_flag(pou_list)
    match cas:
        case 1: #Ce match est à remplir à la main dans les fonction car c'est si on décide d'une random team ou juste d'une création lambda
            display_text_drop(cas2)
            show_team(pou_list)
        case 2:
            print("\nVoici votre équipe :\n")
            show_team(pou_list)

def display_comp(attacker):
    text = [f"  {i + 1} - {attacker.comp[i].name}" for i in range(4)]
    display_all(text)

def display_description(attacker):
    text = [f"{i+1}. {comp.name} : {comp.description}" for i, comp in enumerate(attacker.comp, start=1)]
    display_all(text)



