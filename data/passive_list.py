# passive_list.py
from Project_P.core.passive import Passive

PASSIVE = {
    "Peau Dure" : Passive(
        name="Peau Dure",
        description="La peau dure du pou lui permet de mieux encaisser. (-20% de dégats subit)",
        trigger="OnReceiveDamage",
        effect_id="reduce_damage",
        tankiness=0.2
    ),
    "Dernier Mot" : Passive(
        name="Dernier Mot",
        description="Double la puissance d'attaque du pou lorsqu'il ne lui reste plus que la moitié de ses pv.",
        trigger="OnTurnStart",
        effect_id="double_attack_below_half",
        stat_multiplier= 2,
        hp_condition= 0.5
    ),
    "Autoritée Divine" : Passive(
        name="Autoritée Divine",
        description="Permet d'ignorer le passif du pou adverse lors d'une attaque. ",
        trigger="OnAttack",
        effect_id="ignore_enemy_passive",
    )
}

