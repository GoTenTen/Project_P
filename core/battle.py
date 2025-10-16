# battle.py

import time
import random
from Project_P.ui.display import display_manager

#appeler -> display_comp
def choose_comp(choice, attacker, defender, state, action=None):
    match choice:
        case '1':
            action = attacker.comp[0].apply(attacker, defender)
        case '2':
            action = attacker.comp[1].apply(attacker, defender) #Askip c'est plus rapide en match case mais j'avoue que j'ai l'impression d'en faire trop pour la fonction que c'est mdr
        case '3':
            action = attacker.comp[2].apply(attacker, defender)
        case '4':
            action = attacker.comp[3].apply(attacker, defender)
    state['log'].append(action)
    return action

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


def game_turn(team_attacker, team_defender, state):
    """
    team_attacker, team_defender sont des instances de Team.
    Cette fonction gère le tour du Pou actif de team_attacker.
    """

    # Vérifier d'abord si l'équipe attaquante a au moins un Pou vivant
    if not team_attacker.is_alive():
        print(f"Toute l'équipe de {team_attacker.owner} est KO. Aucun tour possible.")
        return

    # Récupérer les Pous actifs (après potentiels précédents switchs)
    attacker = team_attacker.get_active_pou()
    defender = team_defender.get_active_pou()

    # Si le Pou actif de l'attaquant est KO, forcer le joueur à choisir un remplaçant
    if not attacker.is_alive():
        print(f"{team_attacker.owner}, votre {attacker.name} est KO et ne peut plus agir.")
        # Si l'équipe n'a aucun vivant, impossible de jouer
        if not team_attacker.is_alive():
            print(f"Aucun Pou disponible pour {team_attacker.owner}.")
            return
        # Demander au joueur de choisir un nouveau Pou (bloquant jusqu'à choix valide)
        team_attacker.choose_next_pou()
        # Après le switch, on arrête ici le tour (le joueur a juste switché)
        return

    action = select_action(attacker, defender, team_attacker, state)

    time.sleep(1)
    print(action)
    time.sleep(1)

    team_attacker.handle_death_and_switch()

    # mettre à jour les buffs des deux Pous
    attacker.update_buffs()

    state['log'].append(action)

    # IMPORTANT : ne pas forcer le switch du défenseur ici.
    # On laisse le joueur défenseur changer son Pou au début de son propre tour.
    # On vérifie néanmoins si toute l'équipe défenseur est KO --> fin de partie
    if not team_defender.is_alive():
        print(f"Toute l'équipe de {team_defender.owner} est KO.")


