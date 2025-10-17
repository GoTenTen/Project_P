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
            return {'next_step' : 'Attaquer'}
        case '2':
            return {'next_step' : 'Description'}
        case '3':
            return {'next_step' : 'Changer_pou'}
        case _:
            return {'next_step' : 'INVALID_ARGUMENT'}


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

    '''# Si le Pou actif de l'attaquant est KO, forcer le joueur à choisir un remplaçant
    if not attacker.is_alive():
        print(f"{team_attacker.owner}, votre {attacker.name} est KO et ne peut plus agir.")
        # Si l'équipe n'a aucun vivant, impossible de jouer
        if not team_attacker.is_alive():
            print(f"Aucun Pou disponible pour {team_attacker.owner}.")
            return
        # Demander au joueur de choisir un nouveau Pou (bloquant jusqu'à choix valide)
        team_attacker.choose_next_pou()
        # Après le switch, on arrête ici le tour (le joueur a juste switché)
        return'''

    while True:
        display_manager('choose_action', attacker=attacker, team_attacker=team_attacker, cas=2)
        choice = input()
        print('\n')
        step = select_action(choice)
        if step['next_step'] in ['Changer_pou','Attaquer']:
            break
        elif step['next_step'] == 'Description':
            display_manager('description', attacker=attacker)
            print('\n')
        else:
            display_manager('invalid')
            print('\n')

    match step['next_step']:
        case 'Attaquer':
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
        case 'Changer_Pou':
            team_attacker.choose_next_pou()

    # mettre à jour les buffs des deux Pous
    attacker.update_buffs()

    # IMPORTANT : ne pas forcer le switch du défenseur ici.
    # On laisse le joueur défenseur changer son Pou au début de son propre tour.
    # On vérifie néanmoins si toute l'équipe défenseur est KO --> fin de partie
    if not team_defender.is_alive_team():
        print(f"Toute l'équipe de {team_defender.owner} est KO.")
        return

    team_defender.handle_death_and_switch()

