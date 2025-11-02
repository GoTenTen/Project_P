# skills_list.py
from Project_P.core.skills import *

SKILLS = {
    "Attack": { #-------------------------------------------------------------------------------------------------------
        "Tape Fort" : AttackSkill(
            name="Tape Fort",
            description="Une attaque puissante infligeant le double des dégâts.",
            priority=1,
            accuracy=0.8,
            multiplier=2.0
        ),
        "Slap That Ass" : AttackSkill(
            name="Slap That Ass",
            description="Frappe entre 1 et 5 fois.",
            priority=1,
            multiplier=1.0,
            multi_hit_range=(1,5)
        ),
        "Jackpot" : AttackSkill(
            name="Jackpot",
            description="Une attaque qui tue à coup sûr. Rate 9 fois sur 10",
            priority=1,
            multiplier=999.0,
            accuracy=0.1,
            bonus_message="LA CHANCE VOUS SOURIT ! (vous êtes cocu) \nDites au revoir à votre adversaire."
        ),
        "Jab" : AttackSkill(
            name="Jab",
            description="Une attaque rapide qui inflige l'atk de l'utilisateur",
            priority=1,
            multiplier=1.0,
        ),
        "Bandit Manchot" : AttackSkill(
            name="Bandit Manchot",
            description="Une attaque qui touche entre 2 à 3 fois, les coups critiques sont doublés. 90 de précision.",
            priority=0,
            multiplier=1.0,
            multi_hit_range=(2,3),
            accuracy=0.9,
            crit_mult=2.0,
        ),
        "Twin Tower" : AttackSkill(
            name = "Vidage sanguin",
            description = "Le pou explose les tours jumelles, causant de blessures graves à l'adversaire le laissant à 1hp, causant au passage sa propre mort",
            priority=0,
            multiplier=1.0,
            set_target_hp=1,
            self_damage=1, # pourcentage
        ),
        "Ruée vers l'Or" : AttackSkill(
            name="Ruée vers l'Or",
            description="Le pou se jette sur tout ce qui brille. Attaque prioritaire.",
            priority=2,
            multiplier=1.0,
        ),
        "Brûlure" : AttackSkill(
            name = "Brûlure",
            description="Brûle l'ennemi",
            priority=0,
            duration = 3,
            multiplier = 0,
            amount = 0.05,
            accuracy = 1.0,
            type_effect = "burn"
        ),
        "Poison" : AttackSkill(
            name = "Poison",
            description="Empoisonne l'ennemi",
            priority=0,
            duration = 4,
            multiplier = 0,
            amount = 0.05,
            accuracy = 1.0,
            type_effect = "poison"
        ),
    },
    "TimedBuffAttack": { #----------------------------------------------------------------------------------------------
        "Danse Lame" : TimedBuffSkill(
            name="Danse Lame",
            description="Double la puissance d'attaque pour 2 tours.",
            priority=1,
            stat="atk",
            factor=2.0,
            duration=2
        ),
        "Cire Chaude" : TimedBuffSkill(
            name="Cire Chaude",
            description="De la cire chaude coule sur le dos de l'utilisateur et fais monter son adrénaline pour booster son atk de 50% pendant 4 tours.",
            priority=0,
            factor=1.5,
            duration=4,
        ),
    },
    "Heal": { #---------------------------------------------------------------------------------------------------------
        "Soin" : HealSkill(
            name="Soin",
            description="Soigne 10 PV.",
            priority=1,
            amount=10,
        ),
    },
    "TimedHeal": { #----------------------------------------------------------------------------------------------------
        "Baume visqueux": TimedHealSkill(
            name="Baume visqueux",
            description="Génère un baume à partir de sa bave à étaler sur ses blessures. Rend 5 PV par tours pendant 2 tours",
            priority=0,
            amount=5,
            duration=2
        )
    },
}