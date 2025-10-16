# main.py
import time

from Project_P.systems.team_creation import create_team
from Project_P.core.battle_copy import *
from Project_P.core.team import *
import random

def start():
    player1 = input("\nVeuillez définir le nom du Joueur 1 s\'il vous plait. :  ")
    player2 = input("Veuillez définir le nom du Joueur 2 s\'il vous plait. :  ")

    team1 = create_team(player1)
    team2 = create_team(player2)

    pou1 = team1.get_active_pou()
    pou2 = team2.get_active_pou()

    game_state = {
        'random_number': random.randint(1, 2),
        'tour': 1,
        'log': []
    }

    random_order(player1, player2, game_state)

    while team1.is_alive() and team2.is_alive():
        time.sleep(1.5)
        print(f"\n-------------- TOUR {game_state['tour']} --------------")
        team1.show_all_pou_stats()
        team2.show_all_pou_stats()
        print("\n------------------------------------\n")
        time.sleep(2)

        if game_state['random_number'] == 1:
            game_turn(team1, team2, game_state)
            team2.handle_death_and_switch()  # Si un Pou de team2 est mort, il change
            game_state['random_number'] = 2
        else:
            game_turn(team2, team1, game_state)
            team1.handle_death_and_switch()  # Si un Pou de team1 est mort, il change
            game_state['random_number'] = 1

        pou1 = team1.get_active_pou()
        pou2 = team2.get_active_pou()

        game_state['tour'] += 1

    winner = pou1 if pou1.is_alive() else pou2
    print(f"\n{winner.owner} a gagné !")
    print("\nRésumé du combat :")
    for entry in game_state['log']:
        print(" -", entry)


if __name__ == "__main__":
    start()
