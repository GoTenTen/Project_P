# battle.py
from Project_P.ui.display import display_manager

def game_turn(team_attacker, team_defender):
    # Récupérer les Pous actifs (après potentiels précédents switchs)
    attacker = team_attacker.get_active_pou()
    defender = team_defender.get_active_pou()

    while True:
        display_manager('choose_action', attacker=attacker, team_attacker=team_attacker, cas=2)
        choice = input()
        display_manager('display_space')
        step = select_action(choice)
        match step['next_step']:
            case 'attaquer':
                select_attack(attacker, defender)
            case 'changer_pou':
                select_switch_pou(team_attacker)
            case 'description':
                display_manager('description', attacker=attacker)
            case _:
                display_manager('invalid')
        break

    # mettre à jour les buffs des deux Pous
    update_buff = attacker.update_buffs()
    if update_buff['events']:
        display_manager('display_update_buff', update_buff=update_buff)

    if not team_defender.is_alive_team():
        display_manager('display_dead_team', team=team_defender)
        return # pour bien sortir de la fonction [ne pas suppr !]

    step = team_defender.handle_death_and_switch()
    if step['next_step'] == 'switch_pou':
        select_switch_pou(team_defender)




def select_switch_pou(team):
    while True:
        display_manager('display_ask_next_pou', team=team)
        choix = input()
        if choix.isdigit():
            idx = int(choix) - 1
            if team.switch_pou(idx):
                display_manager('display_ask_next_pou_more', team=team, index=idx)
                break
        display_manager('invalid', cas=1)

def select_attack(attacker, defender):
    while True:
        display_manager('display_comp', attacker=attacker)
        display_manager('display_input', cas=1)
        choice = input()
        if choice in ('1', '2', '3', '4'):
            action = choose_comp(choice, attacker, defender)
            display_manager('display_skill', action=action)
            break
        else:
            display_manager('invalid')

#appeler -> display_comp
def choose_comp(choice, attacker, defender):
    match choice:
        case '1':
            return attacker.comp[0].apply(attacker, defender)
        case '2':
            return attacker.comp[1].apply(attacker, defender)
        case '3':
            return attacker.comp[2].apply(attacker, defender)
        case '4':
            return attacker.comp[3].apply(attacker, defender)
    return None

def select_action(choice):
    match choice:
        case '1':
            return {'next_step' : 'attaquer'}
        case '2':
            return {'next_step' : 'description'}
        case '3':
            return {'next_step' : 'changer_pou'}
        case _:
            return {'next_step' : 'INVALID_ARGUMENT'}