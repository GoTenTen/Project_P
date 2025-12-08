from Project_P.data.elem_list import ELEMENT
from Project_P.data.skills_list import *
from Project_P.data.pou_list import PouModels
from Project_P.core.pou import *

import random

#Idée, analyse_situation stock les inputs à faire dans une liste

class Ai:
    def __init__(self):
        self.situation = {} #Ici, on vient stocker tout les flags décrivant la situation (Ex : attacker_low = True)

    def get_action(self, attacker, defender, team, difficulty):
        situation = self.analyse_situation(attacker, defender, team)
        match difficulty:
            case "easy":
                comp_idx = self.get_random_comp(attacker)
                return {
                    "attacker" : attacker,
                    "defender" : defender,
                    "comp_idx" : comp_idx
                }
            case "medium":
                sort_skill = self.sort_skill(attacker)
            
            case "hard":
                ...

    def analyse_situation(attacker, defender, team):
        ...

#----------------------------------------------------FONCTIONS----------------------------------------------------
    @staticmethod
    def get_random_comp(attacker):
        choice_comp = random.randint(0,len(attacker.comp)-1)
        return choice_comp

    @staticmethod
    def check_health(attacker, defender):
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


    @staticmethod
    def element_comparison(attacker, defender):
        elem_efficacity = ELEMENT.get(attacker.elem).get(defender.elem, 1)
        match elem_efficacity:
            case 0.5:
                return {"element_comparison" : "not_effective"}
            case 1.5:
                return {"element_comparison" : "super_effective"}
            case _:
                return {"element_comparison" : "effective"}

    @staticmethod
    def sort_skill(attacker):
        skill_list = {}
        for skill_idx, skill in enumerate(attacker.comp):
            name_class = type(skill).__name__
            if name_class not in skill_list:
                skill_list[name_class] = []
            skill_list[name_class].append(skill_idx)
        return skill_list
    
    @staticmethod
    def kill_confirm(attacker, defender, sort_skill): #maj possible ajouter la proba du critique
        list_skill = []
        atk = attacker.atk
        def_hp = defender.hp
        if "AttackSkill" not in sort_skill:
            return None
        for i in sort_skill["AttackSkill"]:
            argument = attacker.comp[i].kwargs
            multiplier = argument.get("multiplier", 1)
            multi_hit_range = argument.get("multi_hit_range", (1,1))
            average_hit = (multi_hit_range[0] + multi_hit_range[1])/2
            base_damage_skill = atk * multiplier * (ELEMENT.get(attacker.elem, {}).get(defender.elem, 1))
            total_damage = base_damage_skill * average_hit
            if "set_target_hp" in argument:
                continue
            elif total_damage >= def_hp:
                list_skill.append(i)
        if list_skill:
            return list_skill
        else:
            return None
        
    @staticmethod
    def get_best_damage(attacker, defender, sort_skill):
        min_remaining_hp = float('inf')
        skill_idx = None
        atk = attacker.atk
        def_hp = defender.hp
        if "AttackSkill" not in sort_skill:
            return None
        for i in sort_skill["AttackSkill"]:
            argument = attacker.comp[i].kwargs
            remaining_hp = def_hp
            if "set_target_hp" in argument:
                remaining_hp = argument["set_target_hp"]
            else:
                multiplier = argument.get("multiplier", 1)
                multi_hit_range = argument.get("multi_hit_range", (1,1))
                average_hit = (multi_hit_range[0] + multi_hit_range[1])/2
                base_damage_skill = atk * multiplier * (ELEMENT.get(attacker.elem, {}).get(defender.elem, 1))
                total_damage = base_damage_skill * average_hit
                remaining_hp = def_hp - total_damage

            if remaining_hp < min_remaining_hp:
                min_remaining_hp = remaining_hp
                skill_idx = i

        return skill_idx
    
    #essayer de reduire les get car similaire et alourdit le code DRY !

    @staticmethod
    def get_best_switch(attacker, defender, team):
        ...




#-------------------------------------------------------Zone de Test-------------------------------------------------
pou_ia = Pou(
    owner="Ordinateur",
    name="Terminator",
    hp=50,
    atk=20,
    speed=15,
    comp_list=[
        SKILLS["Attack"]["Jab"], 
        SKILLS["Heal"]["Soin"], 
        SKILLS["TimedBuffAttack"]["Danse Lame"], 
        SKILLS["Heal"]["Soin"]
    ],
    passive='',
    rarity="rare",
    elem="Gluant",
    color=''
)

print(Ai.sort_skill(pou_ia))