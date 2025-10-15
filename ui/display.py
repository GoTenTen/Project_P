#display.py
from Project_P.core.battle import *
import time

def choose_action(attacker, team_attacker):
    print(f"C'est au tour de {team_attacker.owner} avec {attacker.name} !\n")
    print("  1 - Attaquer")
    print("  2 - Description des compétences")
    print("  3 - Changer de Pou\n")
    choice = input("Votre choix : ")
    print('')
    return choice


def display_all(text):
    [print(x) for x in text]

def display_action(attacker, team_attacker, display_all):
    choice_action = [f"C'est au tour de {team_attacker.owner} avec {attacker.name} !",
                    "1 - Attaquer",
                    "2 - Description des compétences",
                    "3 - Changer de Pou"]
    display_all(choice_action)

def display_invalid(display_all):
    display_all(["Choix invalide, réessaie."])

def display_starter(random_numb, p1, p2):
    start = []
    display_all([f"Qui commence entre {p1} et {p2} ?\n"])
    match random_numb:
        case 1:
            start = [f"C'est {p1} qui commence !\n"]
        case 2:
            start = [f"C'est {p2} qui commence !\n"]
    display_all(start)

def display_sleep(cas):
    match cas:
        case '1':
            for _ in range(3):
                print(".", end="", flush=True) #Un seul cas, mais comme ça on peut en rajouter et varier si l'on souhaite
                time.sleep(1)
            print("\n")

def display_description(dispaply_all):
    display_all(["\nDescriptions des compétences :\n"])

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
