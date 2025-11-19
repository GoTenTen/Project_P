# main.py
from Project_P.systems.team_creation import create_team
from Project_P.core.battle import game_turn, select_switch_pou, get_player_action
from Project_P.core.ai_function import get_ai_action
from Project_P.core.team import *
from Project_P.ui.display import display_manager
import random
from Project_P.ui.colors import *

def start():
    #choix du mode de jeu
    print("kel mod tu jou ?\n\n     -1 jcj\n\n      -2 jcai\n")
    #définit si un joueur est une ia ou pas, false de base -> true que lorsqu'on a besoin
    ai1, ai2 = False, False
    #pareil ici étant donné que le mode de base est jcj la valeur de base est get_player_action
    mode_player1,mode_player2 = get_player_action, get_player_action
    mode=int(input())
    match mode:
        case 1:
            display_manager('clear', delay=0)
            display_manager('display_name_player', number_player=1)
            player1 = input()
            display_manager('display_name_player', number_player=2)
            player2 = input()
            display_manager('clear', delay=0)
            mode_player1,mode_player2 = get_player_action, get_player_action
        case 2:
            ai2 = True
            name_list = ["caca", "gros_caca", "pipi", "gros_pipi"]
            display_manager('clear', delay=0)
            display_manager('display_name_player', number_player=1)
            player1 = input()
            player2 = random.choice(name_list)
            print(f"Tu affronteras {player2}")
            input()
            display_manager('clear', delay=0)
            mode_player1 = get_player_action
            mode_player2 = get_ai_action

    team1 = create_team(player1, ai1)
    choice_start_pou(team1)
    input('\n(appuyer sur entrer pour continuer)')
    display_manager('clear', delay=0)
    team2 = create_team(player2, ai2)
    if not ai2:
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

        game_turn(team1, team2, mode_player1, mode_player2)

        pou1 = team1.get_active_pou()
        pou2 = team2.get_active_pou()

        game_state['tour'] += 1

    winner = None
    if pou1.is_alive() or pou2.is_alive():
        if pou1.is_alive():
            winner = pou1
        else:
            winner = pou2
    if winner:
        display_manager('display_victory', winner=winner)
    else:
        display_manager('display_draw', player1=player1, player2=player2)
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
