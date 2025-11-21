#ai_function
from Project_P.core.skills import *
from Project_P.data.elem_list import *
import random

#v1 -> aléatoire, "bête" car peut se heal alors qu'il est full hp etc

def get_ai_action_easy(attacker, defender, team=None):
    choice_action = 1
    match choice_action:
        case 1:
            return get_random_comp(attacker, defender)

def get_ai_action(attacker, defender, team=None):
    choice_action = 1
    #1 -> attaquer                           analyse_situation case "before_action" -> check si sort de heal avant de rentrer dans les attaques, si non -> switch
    match choice_action:
        case 1:
            situation = analyse_situation(attacker, defender, cas="attack", team=None)
            sorted_comp = sort_comp(attacker)
            match situation:
                case "heal":
                    if sorted_comp["heal_list"]:
                        comp_idx = random.choice(sorted_comp["heal_list"])
                    else:
                        return get_random_comp(attacker, defender)
                case "attack":
                    if sorted_comp["attack_list"]:
                        comp_idx = random.choice(sorted_comp["attack_list"])
            return {'attacker' : attacker,
                    'defender' : defender, 
                    'comp_idx' : comp_idx}
            
#----------------------------------------------------FONCTIONS----------------------------------------------------
        
def get_random_comp(attacker, defender):
    choice_comp = random.randint(0,len(attacker.comp)-1)
    return {'attacker' : attacker,
            'defender' : defender, 
            'comp_idx' : choice_comp}

def analyse_situation(attacker, defender, cas, team=None):
    effectiveness = element_comparison(attacker, defender)#non opé
    match cas:
        case "attack":
            health_statut = check_health(attacker, defender)
            if health_statut["attacker_state"] == "low":
                return "heal" 
            else:
                return "attack"
            


def check_health(attacker, defender):
    attacker_state = ""
    defender_state = ""
    situation = ""
    if attacker.hp <= attacker.max_hp * 0.33:
        attacker_state = "low"
    elif defender.hp <= defender.max_hp * 0.33:
        defender_state = "low"
    elif (attacker.hp <= attacker.max_hp * 0.33) and (defender.hp <= defender.max_hp * 0.33):
        if (attacker.hp <= attacker.max_hp * 0.33) > (defender.hp <= defender.max_hp * 0.33):
            situation = "opponent_critical_state"
        elif (attacker.hp <= attacker.max_hp * 0.33) < (defender.hp <= defender.max_hp * 0.33):
            situation = "self_critical_state"
        else:
            situation = "both_low"
    return {
        "attacker_state" : attacker_state,
        "defender_state" : defender_state,
        "situation" : situation
    }

def element_comparison(attacker, defender):
    elem_efficacity = ELEMENT.get(attacker.elem).get(defender.elem, 1)
    match elem_efficacity:
        case 0.5:
            return "not_effective"
        case 1.5:
            return "super_effective"
        case _:
            return "effective"

def sort_comp(attacker):
    heal_list = []
    attack_list = []
    buff_list = []
    status_list = []
    for comp_idx in range(len(attacker.comp)):
        if isinstance(attacker.comp[comp_idx], (TimedHealSkill, HealSkill)):
            heal_list.append(comp_idx)
        elif isinstance(attacker.comp[comp_idx], AttackSkill):
            attack_list.append(comp_idx)
        elif isinstance(attacker.comp[comp_idx], BuffSkill):
            buff_list.append(comp_idx)
        elif isinstance(attacker.comp[comp_idx], StatusSkill):
            status_list.append(comp_idx)

    return{
        "heal_list" : heal_list,
        "attack_list" : attack_list,
        "buff_list" : buff_list,
        "status_list" : status_list
    }
    