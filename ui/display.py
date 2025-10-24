#display.py
from Project_P.ui.colors import * 
import time
import os
import sys
import re


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

        case 'display_input_create_team':
            output(f"\n{BOLD}{kwargs['player']}{RESET}, voulez vous créer votre propre équipe ou en générer une aléatoirement ?\n\n     1 : Créez votre propre équipe !\n     2 : Générer une équipe (En dev)\n")

        case 'display_skill':
            display_all(display_skill(kwargs['action']), delay=1)

        case 'display_passive':
            output(display_passive(user=kwargs['user'], action=kwargs['action']))

        case 'display_update_buff':
            output(display_update_buff(kwargs['update_buff']))

        case 'display_show_all_pou_stats':
            display_show_all_pou_stats(kwargs['team'])

        case 'display_name_player':
            output(f"\nVeuillez définir le nom du Joueur {kwargs['number_player']} s\'il vous plait. :  ", end="")

        case 'display_ask_next_pou':
            return ask_next_pou(kwargs['team'])

        case 'display_ask_next_pou_more':
            output(f"\n{BOLD}{kwargs['team'].owner}{RESET} envoie {BOLD}{kwargs['team'].get_active_pou().name}{RESET} au combat!")

        case 'display_space':
            output("")

        case 'display_dead_team':
            output(f"Toute l'équipe de {BOLD}{kwargs['team'].owner}{RESET} est KO.")

        case 'display_victory':
            output(f"\n{BOLD}{kwargs['winner'].owner}{RESET} a gagné !")

        case 'clear':
            time.sleep(kwargs['delay'])
            clear()

        case _:
            output(f'\n event : {event} est inconnu\n')


def clear():
    """Efface le terminal proprement, quel que soit l'environnement (Windows, macOS, Linux, VSCode, IDLE, etc.)"""
    # Cas 1 : Si on est dans un terminal "classique"
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS / Linux
        os.system('clear')

    # Cas 2 : Certains environnements (IDLE, PyCharm, VSCode) n’effacent pas vraiment.
    # On simule alors un effacement en imprimant plusieurs sauts de ligne :
    if not sys.stdout.isatty():  # Pas un vrai terminal
        print("\n" * 100)

def output(text, end="\n", delay=0):
    print(text, end=end, flush=True)
    if delay > 0:
        time.sleep(delay)

def display_all(text, end="\n", delay=0):
    for x in text:
        output(x, end, delay=delay)


def display_action(attacker, team_attacker):
    choice_action = [f"C'est au tour de {BOLD}{team_attacker.owner}{RESET} avec {BOLD}{attacker.name}{RESET} !\n",
                    "  1 - Attaquer",
                    "  2 - Description des compétences",
                    "  3 - Changer de Pou\n"]
    display_all(choice_action)

def display_input(cas):
    text = ""
    match cas:
        case 1:
            text = 'Que voulez vous faire ?'
        case 2:
            text = 'Votre choix :'
        case 3:
            text = "Quel Pou choississez-vous ?\n"
        case 4:
            text = "Voulez-vous modifier votre équipe ?\n"
    output(text, end='')

def display_invalid(cas):
    match cas:
        case 1:
            display_all(["Choix invalide, réessaie."])
        case 2:
            display_all(["Pou mort, choix impossible."])
        case 3:
            display_all(["Pou déjà selectionné."])

def display_starter(player1, player2, player_random):
    input('continue?')
    clear()
    output(f"Qui commence entre {BOLD}{player1}{RESET} et {BOLD}{player2}{RESET} ?", end=" ")
    display_sleep(0.5)
    output(f"C'est {BOLD}{player_random}{RESET} qui commence !\n")


def display_sleep(delay=1.0):
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(delay)
    print("\n") 


def display_text_drop(cas):
    match cas:
        case 1:
            output(f"\n{LIGHTGREEN}●{RESET} Les étoiles se sont alignées... Ou pas... {LIGHTGREEN}●{RESET}\nVoici ton équipe : \n")
        case 2:
            output(f"\n{LIGHTBLUE}●{RESET} Les étoiles se sont alignées... Ou presque... {LIGHTBLUE}●{RESET}\nVoici ton équipe :\n")
        case 3:
            output(f"\n{MAGENTA}★{RESET} Les étoiles se sont alignées ! {MAGENTA}★{RESET} \nRegarde moi cette équipe : \n")
        case 4:
            output(f"\n{LIGHTYELLOW}★{RESET} Dios mio abberant le taux de drop {LIGHTYELLOW}★{RESET}\nAdmire ton équipe : \n")


def show_team(pou_list):
    text = [f"  - {pou.color}{pou.name}{RESET}" for pou in pou_list]
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
    for i in range(3):
        output(f"  {i + 1} - {attacker.comp[i].name}")
    output(f"  4 - {attacker.comp[3].name}", end="\n\n")

def display_description(attacker):
    text = [f"{i+1}. {comp.name} : {comp.description}" for i, comp in enumerate(attacker.comp, start=1)]
    display_all(text)

def display_update_buff(action):
    for events in action['events']:
        match events['type_buff']:
            case 'atk':
                return f"L’effet de d'augmentation de l'{LIGHTRED}ATK{RESET} du {BOLD}{action['user'].name}{RESET} de {BOLD}{action['user'].owner}{RESET} s’est dissipé.\n"
            case 'regen':
                return f"{BOLD}{action['user'].name}{RESET} de {BOLD}{action['user'].owner}{RESET} récupère {LIGHTGREEN}{events['amount']}{RESET} PV\n"
            case _:
                return f"erreur"

def display_skill(action):
    msg_debut = f"{BOLD}{action['user'].name}{RESET} de {BOLD}{action['user'].owner}{RESET} utilise {LIGHTMAGENTA}{action['comp_name']}{RESET} "
    message = ""
    match action['type_skill']:
        case 'buff':
            msg_fin = f": {action['stat_id']} passe de {action['before']} à {action['stat_value']} !"
            message_final = msg_debut + msg_fin
        case 'heal':
            msg_fin = f": {action['user'].name} récupère {action['amount']} PV. (PV actuels: {action['user_hp']})"
            message_final = msg_debut + msg_fin
        case 'timed_buff':
            msg_fin = f": {action['stat_id']} augmenté pour {action['duration']} tours !"
            message_final = msg_debut + msg_fin
        case 'timed_heal':
            msg_fin = f": régénère {action['amount']} PV par tours, pendant {action['duration']} tours !"
            message_final = msg_debut + msg_fin
        case 'attack':
            message = []
            for events in action['events']:
                match events['type_events']:
                    case 'announce':
                        message.append(f"\n{action['user'].owner} utilise {LIGHTMAGENTA}{action['comp_name']}{RESET} !")
                    case 'events_passive':
                        for x in events['events_passive']:
                            match x['id_passive']:
                                case 'ignore':
                                    message.append(f"Grace à son passif {x['name_passive']}, {action['user'].name} ignore le passif de {action['target'].name}!")
                                case 'tankiness':
                                    message.append(f"{action['user'].name} réduit les dégats subit de {int(x['tankiness']*100)}% grace à son passif {x['name_passive']} !")
                    case 'miss':
                        message.append("raté!")
                        return message
                    case 'bonus_message':
                        message.append(f"\n{events['bonus_message']}\n")
                    case 'hits_and_crits':
                        if events['hits'] > 1:
                            message.append(f"Coup {events['i'] + 1}: {events['damage']} dmg{YELLOW}{events['crit_txt']}{RESET}")
                        else:
                            if events['crit_txt']:
                                message.append(events['crit_txt'])
                    case 'self_damage':
                        message.append(f"Il prend {events['self_damage']} de dégats de contre coup... Tdc va \n")
                    case 'elem_efficacity':
                        if events['elem_efficacity'] == 'effective':
                            message.append(f"\n{BOLD}c'est super efficace !{RESET}\n")
                        else:
                            message.append(f"\n{BOLD}ce n'est pas très efficace...{RESET}\n")
            message.append(f"{BOLD}{action['user'].name}{RESET} de {BOLD}{action['user'].owner}{RESET} à infligé {RED}{action['total_damage']}{RESET} dégâts à {BOLD}{action['target'].name}{RESET} de {BOLD}{action['target'].owner}{RESET}.")
        case _:
            message = f"erreur starfoullah : {action['type_skill']}"
    return message


def hp_bar(hp, max_hp, width=20):
    filled = int(width * hp / max_hp)
    empty = width - filled
    color = GREEN if hp > max_hp * 0.5 else YELLOW if hp > max_hp * 0.2 else RED if hp != 0 else GREY
    return f"{color}{'█' * filled}{'░' * empty}{RESET}"

def display_show_all_pou_stats(team):
    ANSI_ESCAPE = re.compile(r'\x1b\[([0-9]+)(;[0-9]+)*m')

    def visible_len(s):
        return len(ANSI_ESCAPE.sub('', s))

    def pad_right(s, width):
        return s + ' ' * (width - visible_len(s))

    def pad_left(s, width):
        return ' ' * (width - visible_len(s)) + s

    output(f"\n    [[{BOLD}{team.owner}{RESET}]]")
    for i, pou in enumerate(team.pous):
        dead = "" if pou.hp > 0 else GREY
        actif = CYAN if i == team.active_index else ""

        name_col = f"{actif}{dead}{pou.name} ({pou.elem})"
        name_col = pad_right(name_col[:30], 30)

        hp_col = f"{hp_bar(pou.hp, pou.max_hp)} {GREEN}{pou.hp}{RESET}/{LIGHTGREEN}{pou.max_hp}{RESET} PV"
        hp_col = pad_right(hp_col, 20)

        atk_col = f"{LIGHTRED}{pou.atk}{RESET} ATK"
        atk_col = pad_left(atk_col, 6)  # largeur fixe pour ATK

        passive_col = f"({LIGHTMAGENTA}{pou.passive.name.upper()}{RESET})" if pou.passive else ""
        passive_col = pad_right(passive_col, 15)

        output(f"       - {name_col} : {hp_col} | {atk_col} | {passive_col}")

        #output(f"- {actif}{dead}{pou.name}{RESET} ({pou.elem})".ljust(65) + f" :  {hp_bar(pou.hp, pou.max_hp)} {GREEN}{pou.hp}{RESET}/{LIGHTGREEN}{pou.max_hp}{RESET} PV | {LIGHTRED}{str(pou.atk).rjust(2)}{RESET} ATK | {LIGHTMAGENTA}{("(" + pou.passive.name.upper() + ")") if pou.passive else ''}{RESET}")

def ask_next_pou(team):
    print(f"{team.owner}, choisissez un autre Pou :\n")
    for i, pou in enumerate(team.pous):
        status = CYAN if i == team.active_index else ""
        print(f"  {i + 1}. {status}{pou.name}{RESET} - PV: {GREEN}{pou.hp}{RESET}/{LIGHTGREEN}{pou.max_hp}{RESET} | {LIGHTRED}{pou.atk}{RESET} ATK")
    output("\nChoisissez un Pou par numéro : ", end="")

def display_passive(user, action):
    match action["name_passive"]:
        case 'Dernier Mot':
            return f"{BOLD}{user.name}{RESET} de {BOLD}{user.owner}{RESET} donne tout et voit son ATK doublée ! Son ATK passe à {LIGHTRED}{user.atk}{RESET}."
    return None