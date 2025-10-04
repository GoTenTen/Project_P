import time
import random
<<<<<<< HEAD
from class_poukemon import *
'''
=======
import class_poukemon

>>>>>>> 7fffcfca88e6d2b6d633f0300a05a72260d6ae88
def start():
    player1 = input('Veuillez définir le nom du Joueur1 s\'il vous plait.   ')
    player2 = input('Veuillez définir le nom du Joueur2 s\'il vous plait.   ')
    print('')

<<<<<<< HEAD
    print(player1, player2)

team1 = {'Pou1' : P.Pou1}
team2 = {'Pou2' : P.Pou2}

teams = [team1, team2]'''

def is_alive(self):
    return self.hp > 0 

def t_damage(self, x): #take_damage
    self.hp -= x  
    if self.hp < 0:
        self.hp = 0

def use_c(self, Pou): #use_comps
    if self.sign == "*":
        return Pou.atk * self.mult
    if self.sign == "+":
        return Pou.atk + self.mult
    #Prend en entree une competence et verifie le signe afin de faire le calcul adéquat

def malus(self, P):
    if self.sign == "-":    
        return P.atk - self.mult
    if self.sign == "/":    
        return P.atk / self.mult
    #Meme principe que use_c mais pour les debuff

def apply_c(self, user, target = None):
    if self.sign == "*":
        return user.atk * self.mult
    elif self.sign == "+":
        return user.atk + self.mult
    elif self.sign == "-":
        if target:
            return target.atk - self.mult
    elif self.sign == "/":    
        if target:
            return target.atk / self.mult
    
=======
    Pou1 = class_poukemon.Pou(player1, "Pou", 30, 10)
    Pou2 = class_poukemon.Pou(player2, "Pou", 30, 10)

    team1 = {'poukemon1': Pou1}
    team2 = {'poukemon1': Pou2}

    # Crée un dictionnaire pour contenir l'état du jeu
    game_state = {
        'random_number': random.randint(1, 2),
        'tour': 0,
        'log': []
    }

    random_order(player1, player2, game_state)

    while team1['poukemon1'].hp >= 1 and team2['poukemon1'].hp >= 1:
        print('--------------------- TOUR', game_state['tour'], '---------------------\n')
        print('                TEAM 1 (' + player1 + ') :\n')
        time.sleep(0.85)
        print('    1.', team1['poukemon1'].name, '- PV :', team1['poukemon1'].hp)
        print('\n                TEAM 2 (' + player2 + ') :\n')
        time.sleep(0.85)
        print('    1.', team2['poukemon1'].name, '- PV :', team2['poukemon1'].hp)
        print('\n')

        game_choice(team1, team2, game_state)
        game_state['tour'] += 1

    # Fin de partie
    if team1['poukemon1'].hp <= 0:
        print(team2['poukemon1'].owner, 'a gagné !')
    else:
        print(team1['poukemon1'].owner, 'a gagné !')

    print_combat_log(game_state)


def random_order(player1, player2, state):
    print('Qui commencera entre ' + player1 + ' et ' + player2 + ' ? \n')
    for _ in range(3):
        time.sleep(0.9)
        print('.')
    print('')
    time.sleep(0.5)

    if state['random_number'] == 1:
        print(player1 + ' commence !\n\n')
    else:
        print(player2 + ' commence !\n\n')


def game_choice(team1, team2, state):
    if state['random_number'] == 1:
        attacker = team1['poukemon1']
        defender = team2['poukemon1']
        state['random_number'] = 2
    else:
        attacker = team2['poukemon1']
        defender = team1['poukemon1']
        state['random_number'] = 1

    print(f"C'est le tour de {attacker.owner} ! Que voulez-vous faire ?\n")
    print("1 - Attaquer")
    print("2 - Soigner (+10 PV)\n")

    while True:
        choice = input("Votre choix : ")
        if choice == '1':
            damage = attacker.atk
            defender.hp -= damage
            action = f"{attacker.owner} attaque et inflige {damage} dégâts."
            print("\n")
            print(action)
            print(f"PV de {attacker.owner} : {attacker.hp}/{attacker.max_hp}")
            print(f"PV de {defender.owner} : {defender.hp}/{defender.max_hp}\n")
            time.sleep(1)
            state['log'].append(action)
            break
        elif choice == '2':
            heal = 10
            attacker.hp = min(attacker.hp + heal, attacker.max_hp)
            action = f"{attacker.owner} utilise un soin et récupère {heal} PV."
            print("\n")
            print(action)
            print(f"PV de {attacker.owner} : {attacker.hp}/{attacker.max_hp}")
            print(f"PV de {defender.owner} : {defender.hp}/{defender.max_hp}\n")
            time.sleep(1)
            state['log'].append(action)
            break
        else:
            print("Choix invalide, veuillez réessayer.\n")
>>>>>>> 7fffcfca88e6d2b6d633f0300a05a72260d6ae88


def test():
    print(f"Les hp de Pou1 sont {Pou1.hp}")
    t_damage(Pou1, malus(chidori3, Pou2))
    print(f"Et maintenant {Pou1.hp}")
    is_alive(Pou1)

<<<<<<< HEAD
test()
=======
def print_combat_log(state):
    print("\nRésumé du combat :")
    for entry in state['log']:
        print('   ', entry)
>>>>>>> 7fffcfca88e6d2b6d633f0300a05a72260d6ae88
