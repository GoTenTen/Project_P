# battle.py

import time
import random

def random_order(p1, p2, state):
    print(f"\nQui commence entre {p1} et {p2} ?")

    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(1)
    print("\n")

    if state['random_number'] == 1:
        print(f"{p1} commence !\n")
    else:
        print(f"{p2} commence !\n")

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
        print(f"{attacker.owner}, votre {attacker.name} est KO et ne peut plus agir.")
        # Si l'équipe n'a aucun vivant, impossible de jouer
        if not team_attacker.is_alive():
            print(f"Aucun Pou disponible pour {team_attacker.owner}.")
            return
        # Demander au joueur de choisir un nouveau Pou (bloquant jusqu'à choix valide)
        team_attacker.choose_next_pou()
        # Après le switch, on arrête ici le tour (le joueur a juste switché)
        return

    # Affichage du menu d'action
    print(f"C'est au tour de {attacker.owner} avec {attacker.name} !\n")
    print("  1 - Attaquer (Tape Fort)")
    print("  2 - Se soigner (+10 PV)")
    print("  3 - Booster (Danse Lame)")
    print("  4 - Description des compétences")
    print("  5 - Changer de Pou\n")

    while True:
        choice = input("Votre choix : ")
        print('')
        if choice == '1':
            action = attacker.comp[0].apply(attacker, defender)
            state['log'].append(action)
            break
        elif choice == '2':
            old_hp = attacker.hp
            attacker.hp = min(attacker.hp + 10, attacker.max_hp)
            action = f"{attacker.owner} se soigne de {attacker.hp - old_hp} PV."
            state['log'].append(action)
            break
        elif choice == '3':
            action = attacker.comp[1].apply(attacker)
            state['log'].append(action)
            break
        elif choice == '4':
            print("\nDescriptions des compétences :\n")
            for i, comp in enumerate(attacker.comp, start=1):
                print(f"{i}. {comp.name} : {comp.description}")
            print("")
        elif choice == '5':
            # Forcer le changement de Pou actif
            team_attacker.choose_next_pou()
            # Fin du tour après le switch
            return
        else:
            print("Choix invalide, réessaie.")

    time.sleep(1)
    print(action)
    time.sleep(1)
    state['log'].append(action)

    # On verifie si le pou est vivant après l'attaque
    # Dans le cas contraire on affiche un message indiquant sa mort
    if not defender.is_alive():
        print(f"{defender.name} perd connaissance.")
        time.sleep(1)
    # IMPORTANT : ne pas forcer le switch du défenseur ici.
    # On laisse le joueur défenseur changer son Pou au début de son propre tour.
    # On vérifie néanmoins si toute l'équipe défenseur est KO --> fin de partie
    if not team_defender.is_alive():
        print(f"Toute l'équipe de {team_defender.owner} est KO.")


