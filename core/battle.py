# battle.py

import time
import random

def random_order(p1, p2, state):
    print(f"\nQui commence entre {p1} et {p2} ?")

    for _ in range(3):
        print(".", end="", flush=True)#-> display_sleep
        time.sleep(1)
    print("\n")

    if state['random_number'] == 1:
        print(f"{p1} commence !\n")
    else:
        print(f"{p2} commence !\n")

# Affichage du menu d'action -> display_action
def choose_action(attacker, team_attacker):
    print(f"C'est au tour de {team_attacker.owner} avec {attacker.name} !\n")
    print("  1 - Attaquer")
    print("  2 - Description des compétences")
    print("  3 - Changer de Pou\n")
    choice = input("Votre choix : ")
    print('')
    return choice

def choose_comp(attacker, defender, state, action=None):
    for i in range(4):
        print(f"  {i + 1} - {attacker.comp[i].name}")
    print('')
    while True:
        choice = input("Votre choix : ")
        print('')
        for i in range(4):
            if choice == str(i + 1):
                action = attacker.comp[i].apply(attacker, defender)
                state['log'].append(action)
        break
    return action

def select_action(attacker, defender, team_attacker, state):
    while True:
        choice = choose_action(attacker, team_attacker)
        if choice == '1':
            return choose_comp(attacker, defender, state)
        elif choice == '4':
            describe_skills(attacker)
        elif choice == '5':
            # Forcer le changement de Pou actif
            team_attacker.choose_next_pou()
            # Fin du tour après le switch
            return
        else:
            print("Choix invalide, réessaie.") # -> display_invalid

def describe_skills(attacker):
    print("\nDescriptions des compétences :\n")
    for i, comp in enumerate(attacker.comp, start=1):
        print(f"{i}. {comp.name} : {comp.description}")
    print("")



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


