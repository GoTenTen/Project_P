# battle.py
from Project_P.ui.display import display_manager
import random

def game_turn(team1, team2):
    # Pous actifs
    pou_team1 = team1.get_active_pou()
    pou_team2 = team2.get_active_pou()

    # Réinitialiser flags ("swicthed_pou" uniquement pour l'instant)
    for pou in (pou_team1, pou_team2):
        pou.flags['switched_pou'] = False

    # Passives OnTurnStart
    for attacker, defender in [(pou_team1, pou_team2), (pou_team2, pou_team1)]:
        passive = attacker.verif_passive('OnTurnStart', target=defender)
        if passive:
            display_manager('display_passive', user=attacker, action=passive)

    # Récupérer les actions des joueurs
    action = [
        get_player_action(pou_team1, pou_team2, team1),
        get_player_action(pou_team2, pou_team1, team2)
    ]

    # Appliquer switches si demandés
    pou_team1 = apply_switch(pou_team1, team1)
    pou_team2 = apply_switch(pou_team2, team2)

    # Appliquer attaques dans le bon ordre (évite le calcul de dégats avant le switch ce qui causait des dégats a l'ancien pou)
    execute_actions(pou_team1, pou_team2, action)

    # Vérifier morts et switchs forcés
    for team in (team1, team2):
        if not team.is_alive_team():
            display_manager('display_dead_team', team=team)
            return
        step = team.handle_death_and_switch()
        if step['next_step'] == 'switch_pou':
            select_switch_pou(team)

    # mettre à jour les buffs des deux Pous
    for pou in [pou_team1, pou_team2]:
        update_buff = pou.update_buffs()
        if update_buff['events']:
            display_manager('display_update_buff', update_buff=update_buff)

# ---------------------- FONCTIONS ------------------------

def get_player_action(attacker, defender, team):
    while True:
        display_manager('choose_action', attacker=attacker, team_attacker=team, cas=2)
        choice = input()
        display_manager('display_space')
        step = select_action(choice)
        match step['next_step']:
            case 'attaquer':
                return select_attack(attacker, defender)
            case 'changer_pou':
                attacker.flags['switch_pou'] = True
                return None
            case 'description':
                display_manager('description', attacker=attacker)
                continue
            case _:
                display_manager('invalid')
                continue

def select_switch_pou(team, cas=1):
    while True:
        display_manager('display_ask_next_pou', team=team)
        choix = input()
        if choix.isdigit():
            idx = int(choix) - 1
            if team.switch_pou(idx):
                display_manager('display_ask_next_pou_more', team=team, index=idx, cas=cas)
                break
        display_manager('invalid', cas=1)

def apply_switch(pou_team, team):
    # --- Appliquer les switchs avant la phase d'attaque ---
    if pou_team.flags['switch_pou']:
        select_switch_pou(team)
        pou_team.flags['switch_pou'] = False
        new_pou = team.get_active_pou()
        new_pou.flags['switched_pou'] = True
        return new_pou
    return pou_team

def select_attack(attacker, defender):
    while True:
        display_manager('display_comp', attacker=attacker)
        display_manager('display_input', cas=1)
        choice = input()
        if choice in ('1', '2', '3', '4'):
            return choose_comp(choice, attacker, defender)
            #display_manager('display_skill', action=action)
            #break
        else:
            display_manager('invalid')

def execute_actions(pou_team1, pou_team2, actions):
    # Gestion des switches : si un joueur switch, l'autre attaque en priorité
    if pou_team1.flags['switched_pou'] or pou_team2.flags['switched_pou']:
        if pou_team1.flags['switched_pou'] and not pou_team2.flags['switched_pou']:
            action_final = pou_team2.comp[actions[1]['comp_idx']].apply(pou_team2, pou_team1)
            display_manager('display_skill', action=action_final)
        elif pou_team2.flags['switched_pou'] and not pou_team1.flags['switched_pou']:
            action_final = pou_team1.comp[actions[0]['comp_idx']].apply(pou_team1, pou_team2)
            display_manager('display_skill', action=action_final)
    else:
        prio1 = pou_team1.comp[actions[0]['comp_idx']].priority if actions[0] else 0
        prio2 = pou_team2.comp[actions[1]['comp_idx']].priority if actions[1] else 0

        # Ordre par priorité de comp
        if prio1 > prio2:
            order = [0, 1]
        elif prio2 > prio1:
            order = [1, 0]
        else:
            # Ordre par vitesse, tirage aléatoire si égalité
            order = [0, 1] if pou_team1.speed >= pou_team2.speed else [1, 0]
            if pou_team1.speed == pou_team2.speed:
                random.shuffle(order)
        for idx in order:
            if actions[idx] is not None:
                action_final = actions[idx]['attacker'].comp[actions[idx]['comp_idx']].apply(actions[idx]['attacker'], actions[idx]['defender'])
                display_manager('display_skill', action=action_final)

#appeler -> display_comp
def choose_comp(choice, attacker, defender):
    idx = int(choice)-1
    if 0 <= idx < 4:
        return {"attacker": attacker, "defender": defender, "comp_idx": idx}
        #return attacker.comp[idx].apply(attacker, defender)
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