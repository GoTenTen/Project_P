#display.py
from Project_P.core.pou import *
import time



def display_manager(event, **kwargs):
    match event:
        case 'choose_action':
            display_action(kwargs['attacker'], kwargs['team_attacker'])
            display_input(kwargs['cas'])
        
        case 'show_team':
            show_team(kwargs['pou_list'])
        
        case 'show_more':
            show_more(kwargs['pou_list'], kwargs['cas'])
        
        case 'display_text_drop':
            display_text_drop(kwargs['cas'])
        
        case 'description':
            display_description(kwargs['attacker'])
        
        case 'invalid':            
            display_invalid(kwargs['cas'])
        
        case 'display_sleep':
            display_sleep()  # display_sleep(kwargs['cas'])

        case 'display_comp':
            display_comp(kwargs['attacker'])

        case 'display_starter':
            return display_starter(kwargs['player1'], kwargs['player2'], kwargs['player_random'])

        case 'display_input':
            display_input(kwargs['cas'])

        case 'display_skill':
            print(display_skill(kwargs['action']))

        case 'display_show_all_pou_stats':
            display_show_all_pou_stats(kwargs['team'])

        case 'name_player_input':
            return display_name_player_input(kwargs['number_player'])

        case _:
            print(f'\n event : {event} est inconnu\n')


def output(text, end="\n", delay=0):
    print(text, end=end, flush=True)
    if delay > 0:
        time.sleep(delay)

def display_all(text):
    for x in text:
        output(x)


def display_action(attacker, team_attacker):
    choice_action = [f"C'est au tour de {team_attacker.owner} avec {attacker.name} !",
                    "1 - Attaquer",
                    "2 - Description des compétences",
                    "3 - Changer de Pou"]
    display_all(choice_action)

def display_input(cas):
    text = ""
    match cas:
        case 1:
            text = 'Que voulez vous faire ?'
        case 2:
            text = 'Votre choix :'
        case 3:
            text = "Voulez vous créer votre propre équipe ou en générer une aléatoirement ?\n\n     1 : Créez votre propre équipe !\n\n     2 : Générer une équipe (En dev)\n\n"
    output(text, end='')

def display_invalid(cas):
    match cas:
        case 1:
            display_all(["Choix invalide, réessaie."])
        case 2:
            display_all(["Pou mort, choix impossible."])

def display_starter(player1, player2, player_random):
    output(f"Qui commence entre {player1} et {player2} ?\n", delay=2)
    output(f"C'est {player_random} qui commence !\n")


def display_sleep():#cas à ajouter si -> match case
    #match cas:
     #   case '1': #Si on décide d'utiliser plusieurs affichage de ce style, on aura juste à ajouter un case (et ptet modifier le nom de la fonction)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(1)
    print("\n") 


def display_text_drop(cas):
    match cas:
        case 1:
            output("\nLes étoiles se sont alignées... Ou pas...\nVoici ton équipe :\n")
        case 2:
            output("\nLes étoiles se sont alignées... Ou presque...\nVoici ton équipe :\n")
        case 3:
            output("\nLes étoiles se sont alignées ! Regarde moi cette équipe :\n")
        case 4:
            output("\nDios mio abberant le taux de drop guette :\n")


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
            output("\nVoici votre équipe :\n")
            show_team(pou_list)

def display_comp(attacker):
    text = [f"  {i + 1} - {attacker.comp[i].name}" for i in range(4)]
    display_all(text)

def display_description(attacker):
    text = [f"{i+1}. {comp.name} : {comp.description}" for i, comp in enumerate(attacker.comp, start=1)]
    display_all(text)

def display_skill(action):
    match action['type_skill']:
        case 'buff':
            return f"{action['user'].name} de {action['user'].owner} utilise {action['comp_name']} : {action['stat_id']} passe de {action['before']} à {action['stat_value']} !"
        case 'heal':
            return f"{action['user'].name} de {action['user'].owner} utilise {action['comp_name']} : {action['user'].name} récupère {action['amount']} PV. (PV actuels: {action['user_hp']})"
        case 'timed_buff':
            return f"{action['user'].name} de {action['user'].owner} utilise {action['comp_name']} : {action['stat_id']} augmenté pour {action['duration']} tours !"
        case 'timed_heal':
            return f"{action['user'].name} de {action['user'].owner} utilise {action['comp_name']} : régénère {action['amount']} PV par tours, pendant {action['duration']} tours !"
        case 'attack':
            for events in action['events']:
                match events['type_events']:
                    case 'announce':
                        output(f"{action['user'].owner} utilise {events['comp_name']} !")
                    case 'bonus_message':
                        output(f"\n{events['bonus_message']}\n")
                    case 'hits_and_crits':
                        if events['hits'] > 1:
                            output(f"Coup {events['i'] + 1}: {events['damage']} dmg{events['crit_txt']}")
                            time.sleep(1)
                        else:
                            output(events['crit_txt'])
                    case 'self_damage':
                        output(f"Il prend {events['self_damage']} de dégats de contre coup... Tdc va \n")
            return f"{action['user'].name} de {action['user'].owner} à infligé {action['total_damage']} dégâts à {action['target_name']} de {action['target_owner']}."
        case _:
            return f"erreur starfoullah : {action['type_skill']}"


def display_show_all_pou_stats(team):
    output(f"\n    [[{team.owner}]]")
    for pou in team.pous:
        actif = "" if pou.hp > 0 else " (KO)"
        output(f"       - {pou.name}{actif} : {pou.hp}/{pou.max_hp} PV | {pou.atk} ATK")


def display_name_player_input(number_player):
    return input(f"\nVeuillez définir le nom du Joueur {number_player} s\'il vous plait. :  ")


