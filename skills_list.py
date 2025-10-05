# skills_list.py
import random

from skills import AttackSkill, BuffSkill, HealSkill, TimedBuffSkill

TapeFort = AttackSkill(
    name="Tape Fort",
    description="Une attaque puissante infligeant le double des dégâts.",
    accuracy=0.8,
    multiplier=2.0
)

DanseLame = TimedBuffSkill(
    name="Danse Lame",
    description="Double la puissance d'attaque pour 2 tours.",
    stat="atk",
    factor=2.0,
    duration=2
)

Heal = HealSkill(
    name="Soin",
    description="Rend 10 PV.",
    amount=10
)

SlapThatAss = AttackSkill(
    name="Slap That Ass",
    description="Frappe entre 1 et 5 fois.",
    multiplier=1.0,
    multi_hit=random.randint(1, 5)
)

Jackpot = AttackSkill(
    name="Jackpot",
    description="Une attaque qui tue à coup sûr. Rate 9 fois sur 10",
    multiplier=999.0,
    accuracy=0.1,
    bonus_message="LA CHANCE VOUS SOURIT ! \nDites au revoir à votre adversaire."
)

Jab = AttackSkill(
    name="Jab",
    description="Une attaque rapide qui inflige l'atk de l'utilisateur",
    multiplier=1.0,
)

BanditManchot = AttackSkill(
    name="Bandit Manchot",
    description="Une attaque qui touche entre 1 à 3 fois, les coups critiques sont doublés. 90 de précision.",
    multiplier=1.0,
    accuracy=0.9,
    crit_mult=2.0,
)

CireChaude = TimedBuffSkill(
    name="Cire Chaude",
    description="De la cire chaude coule sur le dos de l'utilisateur et fais monter son adrénaline pour booster son atk de 50% pendant 4 tours.",
    factor=1.5,
    duration=4
)