from Project_P.data.elem_list import ELEMENT
from Project_P.data.skills_list import *
from Project_P.core.pou import *
import random

#Idée, analyse_situation stock les inputs à faire dans une liste

class Ai:
    def __init__(self):
        self.situation = {} #Ici, on vient stocker tout les flags décrivant la situation (Ex : attacker_low = True)

    def get_ai_action(self, attacker, defender, team):
        comp_idx = self.get_random_comp(attacker)
        return {
            "attacker" : attacker,
            "defender" : defender,
            "comp_idx" : comp_idx
        }

    def analyse_situation(attacker, defender, team):
        ...

#----------------------------------------------------FONCTIONS----------------------------------------------------

    def get_random_comp(self, attacker):
        choice_comp = random.randint(0,len(attacker.comp)-1)
        return choice_comp


    def check_health(self, attacker, defender):
        attacker_state = attacker.hp <= attacker.max_hp * 0.33
        defender_state = defender.hp <= defender.max_hp * 0.33

        if attacker_state and defender_state:
            situation = "both_low"
        elif attacker_state:
            situation = "self_critical_state"
        elif defender_state:
            situation = "opponent_critical_state"
        else:
            situation = ""

        return {
            "attacker_state": "low" if attacker_state else "",
            "defender_state": "low" if defender_state else "",
            "both_state": situation
        }



    def element_comparison(self, attacker, defender):
        elem_efficacity = ELEMENT.get(attacker.elem).get(defender.elem, 1)
        match elem_efficacity:
            case 0.5:
                return {"element_comparison" : "not_effective"}
            case 1.5:
                return {"element_comparison" : "super_effective"}
            case _:
                return {"element_comparison" : "effective"}

    def sort_skill(self, attacker):
        list_comp = {
                "HealSkill" : [],
                "TimedHealSkill" : [],
                "AttackSkill" : [],
                "BuffSkill" : [],
                "TimedBuffSkill" : [],
                "StatusSkill" : []
        }
        for comp_idx in range(len(attacker.comp)):
            for key, value in list_comp.items():
                if type(attacker.comp[comp_idx]).__name__ == key:
                    value.append(comp_idx)
        return list_comp