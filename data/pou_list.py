#class_poukemon_list
from Project_P.data.skills_list import SKILLS
from Project_P.data.passive_list import PASSIVE
from Project_P.ui.colors import *

PouModels = {
    "Pou Soldat": {
        "name": "Pou Soldat",
        "hp": 30,
        "atk": 10,
        "rarity": 'commun',
        "color": LIGHTGREEN,
        "skills": [SKILLS["Tape Fort"], SKILLS["Vidage Sanguin"], SKILLS["Slap That Ass"], SKILLS["Baume visqueux"]],
        "passive": '',
    },
    "Pou Sergent": {
        "name": "Pou Sergent",
        "hp": 50,
        "atk": 7,
        "rarity": 'commun',
        "color": LIGHTGREEN,
        "skills": [SKILLS["Jab"], SKILLS["Danse Lame"], SKILLS["Tape Fort"], SKILLS["Soin"]],
        "passive": PASSIVE['Peau Dure']
    },
    "Pou Kamikaze": {
        "name": "Pou Kamikaze",
        "hp": 20,
        "atk": 15,
        "rarity": 'rare',
        "color": LIGHTBLUE,
        "skills": [SKILLS["Jab"], SKILLS["Danse Lame"], SKILLS["Slap That Ass"], SKILLS["Soin"]],
        "passive": '',
    },
    "Pou Accro Au Casino": {
        "name": "Pou Accro Au Casino",
        "hp": 20,
        "atk": 15,
        "rarity": 'légendaire',
        "color": LIGHTYELLOW,
        "skills": [SKILLS["Jab"], SKILLS["Bandit Manchot"], SKILLS["Jackpot"], SKILLS["Soin"]],
        "passive": PASSIVE['Autoritée Divine']
    },
    "Pou BDSM": {
        "name": "Pou BDSM",
        "hp": 20,
        "atk": 15,
        "rarity": 'épic',
        "color": MAGENTA,
        "skills": [SKILLS["Jab"], SKILLS["Slap That Ass"], SKILLS["Cire Chaude"], SKILLS["Tape Fort"]],
        "passive": '',
    }
}