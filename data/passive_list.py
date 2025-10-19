# passive_list.py
from Project_P.core.passive import *

PASSIVE = {
    "Peau Dure" : OnReceiveDamage(
        name="Peau Dure",
        description="La peau dure du pou lui permet de mieux encaisser. (-20% de dégats subit)",
        tankiness= 0.2
    ),
    "Dernier Mot" : OnTurnStart(
        name="Dernier Mot",
        description="Double la puissance d'attaque du pou lorsqu'il ne lui reste plus que la moitié de ses pv.",
        stat_multiplier= 2,
        hp_condition= 0.5
    ),
    "Autoritée Divine" : OnAttack(
        name="Autoritée Divine",
        description="Permet d'ignorer le passif du pou adverse lors d'une attaque. ",
    )
}