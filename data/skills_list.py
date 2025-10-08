# skills_list.py
import random
from Project_P.core.skills import AttackSkill, BuffSkill, HealSkill, TimedBuffSkill

SKILLS = {
    "Tape Fort" : AttackSkill(
        name="Tape Fort",
        description="Une attaque puissante infligeant le double des dégâts.",
        accuracy=0.8,
        multiplier=2.0
    ),
    "Danse Lame" : TimedBuffSkill(
        name="Danse Lame",
        description="Double la puissance d'attaque pour 2 tours.",
        stat="atk",
        factor=2.0,
        duration=2
    ),
    "Soin" : HealSkill(
        name="Soin",
        description="Soigne 10 PV.",
        amount=10,
    ),
    "Slap That Ass" : AttackSkill(
        name="Slap That Ass",
        description="Frappe entre 1 et 5 fois.",
        multiplier=1.0,
        multi_hit=random.randint(1, 5)
    ),
    "Jackpot" : AttackSkill(
        name="Jackpot",
        description="Une attaque qui tue à coup sûr. Rate 9 fois sur 10",
        multiplier=999.0,
        accuracy=0.1,
        bonus_message="LA CHANCE VOUS SOURIT ! (vous êtes cocu) \nDites au revoir à votre adversaire."
    ),
    "Jab" : AttackSkill(
        name="Jab",
        description="Une attaque rapide qui inflige l'atk de l'utilisateur",
        multiplier=1.0,
    ),
    "Bandit Manchot" : AttackSkill(
        name="Bandit Manchot",
        description="Une attaque qui touche entre 1 à 3 fois, les coups critiques sont doublés. 90 de précision.",
        multiplier=1.0,
        accuracy=0.9,
        crit_mult=2.0,
    ),
    "Cire Chaude" : TimedBuffSkill(
        name="Cire Chaude",
        description="De la cire chaude coule sur le dos de l'utilisateur et fais monter son adrénaline pour booster son atk de 50% pendant 4 tours.",
        factor=1.5,
        duration=4,
    ),
    "Vidage Sanguin" : AttackSkill(
        name = "Vidage sanguin",
        description = "Dans un ultime élant, le pou décide d'aspirer l'entièreté du sang de son adversaire le laissant à 1hp, causant au passage sa propre mort",
        multiplier=1.0,
        self_damage=9999
    )
}