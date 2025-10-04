import time
import random
from class_poukemon import *
'''
def start():
    player1 = str(input('Veuillez définir le nom du Joueur1 s\'il vous plait.   '))
    player2 = str(input('Veuillez définir le nom du Joueur2 s\'il vous plait.   '))
    print('')

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
    


def test():
    print(f"Les hp de Pou1 sont {Pou1.hp}")
    t_damage(Pou1, malus(chidori3, Pou2))
    print(f"Et maintenant {Pou1.hp}")
    is_alive(Pou1)

test()