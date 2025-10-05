# team_factory.py
from class_poukemon import Pou
from class_poukemon_list import PouModels
from team import Team


def create_team(owner_name):
    """
    Crée une équipe complète de Pous pour un joueur donné.
    Chaque Pou est une nouvelle instance indépendante (owner distinct).
    """
    pou_list = [
        Pou(owner_name, data["name"], data["hp"], data["atk"], data["skills"])
        for data in PouModels.values()
    ]
    return Team(owner_name, pou_list)
