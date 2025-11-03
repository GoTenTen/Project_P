#class_poukemon_list
from Project_P.data.skills_list import SKILLS
from Project_P.data.passive_list import PASSIVE
from Project_P.ui.colors import *

PouModels = {
    "Pou Test": {
        "name": "Pou Test",
        "hp": 30,
        "atk": 10,
        "speed": 16,
        "rarity": 'commun',
        "elem" : 'Gluant',
        "color": LIGHTGREEN,
        "skills": [SKILLS["Attack"]["Poing_Poison"], SKILLS["Heal"]["Soin"], SKILLS["Status"]["Poison"], SKILLS["Status"]["Brûlure"]],
        "passive": '',
    },
    "Pou Soldat": {
        "name": "Pou Soldat",
        "hp": 30,
        "atk": 10,
        "speed": 16,
        "rarity": 'commun',
        "elem" : 'Gluant',
        "color": LIGHTGREEN,
        "skills": [SKILLS["Attack"]["Jab"], SKILLS["Heal"]["Soin"], SKILLS["Attack"]["Tape Fort"], SKILLS["Status"]["Brûlure"]],
        "passive": '',
    },
    "Pou Sergent": {
        "name": "Pou Sergent",
        "hp": 50,
        "atk": 7,
        "speed": 11,
        "rarity": 'commun',
        "elem" : 'Corrompu',
        "color": LIGHTGREEN,
        "skills": [SKILLS["Attack"]["Jab"], SKILLS["TimedBuffAttack"]["Danse Lame"], SKILLS["Attack"]["Tape Fort"], SKILLS["Heal"]["Soin"]],
        "passive": PASSIVE['Peau Dure']
    },
    "Pou Kamikaze": {
        "name": "Pou Kamikaze",
        "hp": 20,
        "atk": 15,
        "speed": 18,
        "rarity": 'rare',
        "elem" : 'Antisémite',
        "color": LIGHTBLUE,
        "skills": [SKILLS["Attack"]["Jab"], SKILLS["TimedBuffAttack"]["Danse Lame"], SKILLS["Attack"]["Twin Tower"], SKILLS["Heal"]["Soin"]],
        "passive": '',
    },
    "Pou Accro Au Casino": {
        "name": "Pou Accro Au Casino",
        "hp": 20,
        "atk": 15,
        "speed": 15,
        "rarity": 'légendaire',
        "elem" : 'Glitch',
        "color": LIGHTYELLOW,
        "skills": [SKILLS["Attack"]["Jab"], SKILLS["Attack"]["Bandit Manchot"], SKILLS["Attack"]["Jackpot"], SKILLS["Attack"]["Ruée vers l'Or"]],
        "passive": PASSIVE['Autoritée Divine']
    },
    "Pou BDSM": {
        "name": "Pou BDSM",
        "hp": 20,
        "atk": 15,
        "speed": 13,
        "rarity": 'épic',
        "elem" : 'Gluant',
        "color": MAGENTA,
        "skills": [SKILLS["Attack"]["Jab"], SKILLS["Attack"]["Slap That Ass"], SKILLS["TimedBuffAttack"]["Cire Chaude"], SKILLS["Heal"]["Soin"]],
        "passive": PASSIVE['Dernier Mot'],
    }
}