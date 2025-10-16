#class_poukemon_list
from Project_P.data.skills_list import SKILLS

PouModels = {
    "Pou Soldat": {
        "name": "Pou Soldat",
        "hp": 30,
        "atk": 10,
        "rarity": "commun",
        "skills": [SKILLS["Tape Fort"], SKILLS["Vidage Sanguin"], SKILLS["Slap That Ass"], SKILLS["Soin"]]
    },
    "Pou Sergent": {
        "name": "Pou Sergent",
        "hp": 50,
        "atk": 7,
        "rarity": "commun",
        "skills": [SKILLS["Jab"], SKILLS["Danse Lame"], SKILLS["Tape Fort"], SKILLS["Soin"]]
    },
    "Pou Kamikaze": {
        "name": "Pou Kamikaze",
        "hp": 20,
        "atk": 15,
        "rarity": "rare",
        "skills": [SKILLS["Jab"], SKILLS["Danse Lame"], SKILLS["Slap That Ass"], SKILLS["Soin"]]
    },
    "Pou Accro Au Casino": {
        "name": "Pou Accro Au Casino",
        "hp": 20,
        "atk": 15,
        "rarity": "légendaire",
        "skills": [SKILLS["Jab"], SKILLS["Bandit Manchot"], SKILLS["Jackpot"], SKILLS["Soin"]]
    },
    "Pou BDSM": {
        "name": "Pou BDSM",
        "hp": 20,
        "atk": 15,
        "rarity": "épique",
        "skills": [SKILLS["Jab"], SKILLS["Slap That Ass"], SKILLS["Cire Chaude"], SKILLS["Tape Fort"]]
    }
}