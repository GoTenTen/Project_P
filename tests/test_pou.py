#--------------------------------------------------------TESTS POUR VERIFIER QUE LE JEU EST PAS BROKE--------------------------------------------------------
from Project_P.core.pou import Pou
from Project_P.data.skills_list import *

#--------------------------------------------------------ZONE DE CREATION DES OBJETS-------------------------------------------------------------------------
pou_1 = Pou(
    owner="Ordinateur1",
    name="Alien",
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

pou_2 = Pou(
    owner="Ordinateur2",
    name="Predator",
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

#------------------------------------------------------------------------------------------------------------------------------------------------------------



#Point important concernant les tests, il faut que chaque fonctions commence par 'test_' sinon elles ne seront pas détecté par pytest

def test_bac_a_sable():
    comp = SKILLS["Attack"]["Jab"]

    comp.apply(user=pou_1, target=pou_2)

    #assert est ce qui permet de dire qu'un test est passé, ici on test que 20 points de vie sont bien retiré au second pou, et c'est le cas ! => pytest dans le terminal pour tester
    assert pou_2.hp == 30