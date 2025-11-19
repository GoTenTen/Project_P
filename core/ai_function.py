
import random

#v1 -> aléatoire, "bête" car peut se heal alors qu'il est full hp etc

def get_ai_action(attacker, defender, team=None):
    choice_action = 1
    match choice_action:
        case 1:
            choice_comp = random.randint(0,len(attacker.comp)-1)
            return {'attacker' : attacker,
                    'defender' : defender, 
                    'comp_idx' : choice_comp}
        
