# battle.py

import time
import random
from Project_P.ui.display import display_manager

#appeler -> display_comp
def choose_comp(choice, attacker, defender):
    match choice:
        case '1':
            return attacker.comp[0].apply(attacker, defender)
        case '2':
            return attacker.comp[1].apply(attacker, defender) #Askip c'est plus rapide en match case mais j'avoue que j'ai l'impression d'en faire trop pour la fonction que c'est mdr
        case '3':
            return attacker.comp[2].apply(attacker, defender)
        case '4':
            return attacker.comp[3].apply(attacker, defender)
    return None

def select_action(choice):
    match choice:
        case '1':
            return {'next_step' : 'attaquer'}
        case '2':
            return {'next_step' : 'description'}
        case '3':
            return {'next_step' : 'changer_pou'}
        case _:
            return {'next_step' : 'INVALID_ARGUMENT'}

def switch_pou(team_attacker):
    while True:
        display_manager('display_show_all_pou_stats', team=team_attacker)
        new_index = int(input('Choisi un nouveau pou : '))
        if new_index in (1, 2, 3):
            if team_attacker.switch_pou(new_index):
                print(f"{team_attacker.get_active_pou.owner} change pour {team_attacker.get_active_pou.name} !")
                break
            else:
                display_manager('invalid', cas=2)
        else:
            display_manager('invalid', cas=1)

def game_turn(team_attacker, team_defender):
    """
    team_attacker, team_defender sont des instances de Team.
    Cette fonction gère le tour du Pou actif de team_attacker.
    """

    # Vérifier d'abord si l'équipe attaquante a au moins un Pou vivant
    if not team_attacker.is_alive_team():
        print(f"Toute l'équipe de {team_attacker.owner} est KO. Aucun tour possible.")
        return

    # Récupérer les Pous actifs (après potentiels précédents switchs)
    attacker = team_attacker.get_active_pou()
    defender = team_defender.get_active_pou()

    while True:
        display_manager('choose_action', attacker=attacker, team_attacker=team_attacker, cas=2)
        choice = input()
        print('\n')
        step = select_action(choice)
        if step['next_step'] in ['changer_pou','attaquer']:
            break
        elif step['next_step'] == 'description':
            display_manager('description', attacker=attacker)
            print('\n')
        else:
            display_manager('invalid')
            print('\n')

    match step['next_step']:
        case 'attaquer':
            while True:
                display_manager('display_comp', attacker=attacker)
                print('\n')
                display_manager('display_input', cas=1)
                choice = input()
                if choice in ('1', '2', '3', '4'):
                    action = choose_comp(choice, attacker, defender)
                    display_manager('display_skill', action=action)
                    break
                else:
                    display_manager('invalid')
        case 'changer_pou':
            display_manager('display_show_all_pou_stats', team=team_attacker)
            new_index = int(input('quel pou khoya?'))
            while new_index not in (1, 2, 3):
                display_manager('invalid', cas=1)
                new_index = int(input('Choisi un nouveau pou : '))
            switch_pou(team_attacker)

    # mettre à jour les buffs des deux Pous
    attacker.update_buffs()

    # IMPORTANT : ne pas forcer le switch du défenseur ici.
    # On laisse le joueur défenseur changer son Pou au début de son propre tour.
    # On vérifie néanmoins si toute l'équipe défenseur est KO --> fin de partie
    if not team_defender.is_alive_team():
        print(f"Toute l'équipe de {team_defender.owner} est KO.")
        return

    step = team_defender.handle_death_and_switch()
    match step['next_step']:
        case 'switch_pou':
            display_manager('display_show_all_pou_stats', team=team_attacker)
            new_index = int(input('ton pou est mort tu veux quel pou khoya?'))
            while new_index not in (1, 2, 3):
                display_manager('invalid', cas=1)
                new_index = int(input('Choisi un nouveau pou : '))
            switch_pou(team_defender)


