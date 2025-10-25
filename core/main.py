# main.py
from Project_P.systems.team_creation import create_team
from Project_P.core.battle import game_turn, select_switch_pou
from Project_P.core.team import *
from Project_P.ui.display import display_manager
import random
from Project_P.ui.colors import *

def start():
    display_manager('clear', delay=0)
    display_manager('display_name_player', number_player=1)
    player1 = input()
    display_manager('display_name_player', number_player=2)
    player2 = input()
    display_manager('clear', delay=0)

    team1 = create_team(player1)
    choice_start_pou(team1)
    input('\n(appuyer sur entrer pour continuer)')
    display_manager('clear', delay=0)
    team2 = create_team(player2)
    choice_start_pou(team2)

    pou1 = team1.get_active_pou()
    pou2 = team2.get_active_pou()

    game_state = {
        'random_player' : random.choice([player1, player2]),
        'tour': 1,
    }

    while team1.is_alive_team() and team2.is_alive_team():
        input('\n(appuyer sur entrer pour continuer)')
        display_manager('clear', delay=0)
        print(f"\n╔═------------------------------------------════════ {BOLD}TOUR {game_state['tour']}{RESET} ════════------------------------------------------═╗")
        display_manager('display_show_all_pou_stats', team=team1)
        display_manager('display_show_all_pou_stats', team=team2)
        print("\n╚═-------------------------------------------------------------------------------------------------------------═╝\n")
        time.sleep(0.5)

        game_turn(team1, team2)

        pou1 = team1.get_active_pou()
        pou2 = team2.get_active_pou()

        game_state['tour'] += 1

    winner = pou1 if pou1.is_alive() else pou2
    display_manager('display_victory', winner=winner)
    display_manager('clear', delay=2)

def choice_start_pou(team):
    print("\nVoulez-vous changer votre poukemon actif ? (Oui : 1 / Non : 2)")
    while True:
        choice = input()
        if choice == "1":
            select_switch_pou(team, 2)
            break
        elif choice == "2":
            break
        else:
            display_manager('invalid', cas=1)




if __name__ == "__main__":
    start()
