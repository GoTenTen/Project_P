# main.py
from Project_P.systems.team_creation import create_team
from Project_P.core.battle import game_turn
from Project_P.core.team import *
from Project_P.ui.display import display_manager
import random

def start():
    display_manager('clear', delay=0)
    display_manager('display_name_player', number_player=1)
    player1 = input()
    display_manager('display_name_player', number_player=2)
    player2 = input()

    team1 = create_team(player1)
    team2 = create_team(player2)

    pou1 = team1.get_active_pou()
    pou2 = team2.get_active_pou()

    game_state = {
        'random_player' : random.choice([player1, player2]),
        'tour': 1,
    }

    display_manager('display_starter', player1=player1, player2=player2, player_random=game_state['random_player'])

    while team1.is_alive_team() and team2.is_alive_team():
        input('continue? ')
        display_manager('clear', delay=0)
        print(f"\n------------------ TOUR {game_state['tour']} ------------------")
        display_manager('display_show_all_pou_stats', team=team1)
        display_manager('display_show_all_pou_stats', team=team2)
        print("\n--------------------------------------------\n")
        time.sleep(0.5)

        if game_state['random_player'] == player1:
            game_turn(team1, team2)
            game_state['random_player'] = player2
        else:
            game_turn(team2, team1)
            game_state['random_player'] = player1

        pou1 = team1.get_active_pou()
        pou2 = team2.get_active_pou()

        game_state['tour'] += 1

    winner = pou1 if pou1.is_alive() else pou2
    display_manager('display_victory', winner=winner)
    display_manager('clear', delay=2)


if __name__ == "__main__":
    start()
