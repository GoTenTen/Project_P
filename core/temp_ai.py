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
        #L'idée que j'avais ici, c'est de faire un situation handler pour l'ia, de lui fournir le plus de flags possible à travers les méthodes 
        # et de la laisser décider du meilleur mouv à faire, cette fonction devra être friendly à l'ajout des "récompenses" et à la gestion du niveau de l'ia
        #situation = self.analyse_situation(attacker, defender, team)
        match difficulty:
            case "easy":
                comp_idx = self.get_random_comp(attacker)
                return {
                    "attacker" : attacker,
                    "defender" : defender,
                    "comp_idx" : comp_idx
                }
            case "medium":
                ...
                '''sort_skill = self.sort_skill(attacker)'''
            
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
        #Ici j'ai mis 33% de la vie mais on peut modifier au choix à l'avenir, peut être mettre diférent palier selon le niveau de l'ia
        target_life_limit = 0.33
        attacker_state = attacker.hp <= attacker.max_hp * target_life_limit
        defender_state = defender.hp <= defender.max_hp * target_life_limit

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
        #Ici on va venir récuperer les type ("element") des pous afin de définir le flag défficacité
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
        #Comme son nom l'indique, cette fonction vient trier les compétences en différentes list dans un dictionnaire ex : "AttackSkill" : ["TapeFort"]
        skill_list = {}
        for skill_idx, skill in enumerate(attacker.comp):
            name_class = type(skill).__name__
            if name_class not in skill_list:
                skill_list[name_class] = []
            skill_list[name_class].append(skill_idx)
        return skill_list
    
    @staticmethod
    def get_optimal_damage(attacker, defender, sort_skill): 
        #maj possible ajouter la proba du critique et peut être classé par ordre du plus probable par rapport à l'accuracy
        list_skill = []
        atk = attacker.atk
        def_hp = defender.hp
        if "AttackSkill" not in sort_skill:
            return list_skill
        for i in sort_skill["AttackSkill"]:
            final_damage = 0
            is_lethal = False
            #Ici on vient récupérer toutes les infos dont à besoin pour calculer et comparer les compétences
            argument = attacker.comp[i].kwargs

            #Les gets principaux qui servent de base pour calculer tous les degats
            accuracy = argument.get("accuracy", 0)
            multiplier = argument.get("multiplier", 1)
            multi_hit_range = argument.get("multi_hit_range", (1,1))

            #Cas exceptionnel, "set_target_hp"
            if "set_target_hp" in argument:
                target_hp_goal = argument["set_target_hp"]
                #Ici on verif si la target n'est pas égale ou en dessous du set_hp
                final_damage = def_hp - target_hp_goal

                if final_damage < 0:
                    final_damage = 0

                #evidemment si on set hp à 0 et bien l'attaque est lethal, pour l'instant aucune compétences fait ça, mais au moins la fonction est futur-proof
                is_lethal = (target_hp_goal == 0)
            else:
                #Moyenne des coups si range (1,6) -> 3 etc...
                average_hit = (multi_hit_range[0] + multi_hit_range[1])/2

                #Calcul des degats d'unn coup en prenant en compte l'element
                base_damage_skill = atk * multiplier * (ELEMENT.get(attacker.elem, {}).get(defender.elem, 1))

                #Calcul de la moyenne des degats si c'est une attaque multi coups, sinon, juste *1 soit un seul coup
                final_damage = base_damage_skill * average_hit

                is_lethal = (final_damage >= def_hp)

            #Ici on vient ajouter la compétence sous forme de dictionnaire dans la liste, avec le flag is_lethal qui dit si oui ou non elle est léthal (logique)
            list_skill.append({
                "index" : i,
                "name": attacker.comp[i].name,
                "damage" : final_damage,
                "accuracy" : accuracy,
                "is_lethal" : is_lethal
            })
        return list_skill

    @staticmethod
    def get_best_switch(attacker, defender, team):
        #EN DEV
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