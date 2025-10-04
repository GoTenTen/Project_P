import time
import random
import class_poukemon

def start():
    player1 = input('Veuillez définir le nom du Joueur1 s\'il vous plait.   ')
    player2 = input('Veuillez définir le nom du Joueur2 s\'il vous plait.   ')
    print('')

    Pou1 = class_poukemon.Pou(player1, "Pou", 30, 10)
    Pou2 = class_poukemon.Pou(player2, "Pou", 30, 10)

    team1 = {'poukemon1': Pou1}
    team2 = {'poukemon1': Pou2}

    # Crée un dictionnaire pour contenir l'état du jeu
    game_state = {
        'random_number': random.randint(1, 2),
        'tour': 0,
        'log': []
    }

    random_order(player1, player2, game_state)

    while team1['poukemon1'].hp >= 1 and team2['poukemon1'].hp >= 1:
        print('--------------------- TOUR', game_state['tour'], '---------------------\n')
        print('                TEAM 1 (' + player1 + ') :\n')
        time.sleep(0.85)
        print('    1.', team1['poukemon1'].name, '- PV :', team1['poukemon1'].hp)
        print('\n                TEAM 2 (' + player2 + ') :\n')
        time.sleep(0.85)
        print('    1.', team2['poukemon1'].name, '- PV :', team2['poukemon1'].hp)
        print('\n')

        game_choice(team1, team2, game_state)
        game_state['tour'] += 1

    # Fin de partie
    if team1['poukemon1'].hp <= 0:
        print(team2['poukemon1'].owner, 'a gagné !')
    else:
        print(team1['poukemon1'].owner, 'a gagné !')

    print_combat_log(game_state)


def random_order(player1, player2, state):
    print('Qui commencera entre ' + player1 + ' et ' + player2 + ' ? \n')
    for _ in range(3):
        time.sleep(0.9)
        print('.')
    print('')
    time.sleep(0.5)

    if state['random_number'] == 1:
        print(player1 + ' commence !\n\n')
    else:
        print(player2 + ' commence !\n\n')


def game_choice(team1, team2, state):
    if state['random_number'] == 1:
        attacker = team1['poukemon1']
        defender = team2['poukemon1']
        state['random_number'] = 2
    else:
        attacker = team2['poukemon1']
        defender = team1['poukemon1']
        state['random_number'] = 1

    print(f"C'est le tour de {attacker.owner} ! Que voulez-vous faire ?\n")
    print("1 - Attaquer")
    print("2 - Soigner (+10 PV)\n")

    while True:
        choice = input("Votre choix : ")
        if choice == '1':
            damage = attacker.atk
            defender.hp -= damage
            action = f"{attacker.owner} attaque et inflige {damage} dégâts."
            print("\n")
            print(action)
            print(f"PV de {attacker.owner} : {attacker.hp}/{attacker.max_hp}")
            print(f"PV de {defender.owner} : {defender.hp}/{defender.max_hp}\n")
            time.sleep(1)
            state['log'].append(action)
            break
        elif choice == '2':
            heal = 10
            attacker.hp = min(attacker.hp + heal, attacker.max_hp)
            action = f"{attacker.owner} utilise un soin et récupère {heal} PV."
            print("\n")
            print(action)
            print(f"PV de {attacker.owner} : {attacker.hp}/{attacker.max_hp}")
            print(f"PV de {defender.owner} : {defender.hp}/{defender.max_hp}\n")
            time.sleep(1)
            state['log'].append(action)
            break
        else:
            print("Choix invalide, veuillez réessayer.\n")



def print_combat_log(state):
    print("\nRésumé du combat :")
    for entry in state['log']:
        print('   ', entry)
