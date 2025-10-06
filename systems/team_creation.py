# team_creation.py
from Project_P.core.pou import Pou
from Project_P.data.pou_list import PouModels
from Project_P.core.team import Team

def create_team(owner_name):
    pou_list = [Pou.from_model(owner_name, model) for model in PouModels.values()]
    return Team(owner_name, pou_list)

