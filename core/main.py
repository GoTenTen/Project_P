# main.py
import time

from Project_P.systems.team_creation import create_team
from Project_P.core.battle import game_turn
from Project_P.core.team import *
from Project_P.ui.display import display_manager
import random

def start():
    player1 = input("\nVeuillez définir le nom du Joueur 1 s\'il vous plait. :  ")
    player2 = input("Veuillez définir le nom du Joueur 2 s\'il vous plait. :  ")

    team1 = create_team(player1)
    team2 = create_team(player2)

    pou1 = team1.get_active_pou()
    pou2 = team2.get_active_pou()

    game_state = {
        'random_number' : random.randint(1,2),
        'tour': 1,
        'log': []
    }

    display_manager('display_starter', p1=player1, p2=player2)

    while team1.is_alive_team() and team2.is_alive_team():
        time.sleep(1.5)
        print(f"\n-------------- TOUR {game_state['tour']} --------------")
        team1.show_all_pou_stats()
        team2.show_all_pou_stats()
        print("\n------------------------------------\n")
        time.sleep(2)

        if game_state['random_number'] == 1:
            game_turn(team1, team2)
            game_state['random_number'] = 2
        else:
            game_turn(team2, team1)
            game_state['random_number'] = 1

        pou1 = team1.get_active_pou()
        pou2 = team2.get_active_pou()

        game_state['tour'] += 1

    winner = pou1 if pou1.is_alive() else pou2
    print(f"\n{winner.owner} a gagné !")


if __name__ == "__main__":
    start()
