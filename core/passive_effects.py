# passive_effects.py

def reduce_damage(user, target, damage, tankiness=0.2, **kwargs):
    new_damage = int(damage * (1 - tankiness))
    return {
        "name_passive": user.passive.name,
        "damage": new_damage,
        "tankiness": tankiness,
        "id_passive": "tankiness"
        # f"{user.name} réduit les dégats subit de {int(tankiness*100)}% grace à son passif {self.name} !"
    }


def ignore_enemy_passive(user, target, damage, **kwargs):
    target.flags["passive_ignored"] = True
    return {
        "name_passive": user.passive.name,
        "damage": damage,
        "id_passive": "ignore"  # f"Grace à son passif {self.name}, {user.name} ignore le passif de {target.name}!"
    }

def double_attack_below_half(user, target, damage, stat_multiplier=2, hp_condition=0.5, **kwargs):
    origin_atk = user.atk
    new_atk = 0
    if user.hp <= user.max_hp * hp_condition and not user.flags.get("atk_boosted", False):
        user.flags['origin_atk'] = user.atk
        user.atk *= stat_multiplier
        user.flags["atk_boosted"] = True
        return {
            "name_passive": user.passive.name,
            "id_passive": "double_attack_below_half"
        }
    elif user.hp > user.max_hp * hp_condition and user.flags.get("atk_boosted", False):
        user.atk = user.flags.get(['origin_atk'], user.base_atk)
        user.flags["atk_boosted"] = False
        return {
            "name_passive": user.passive.name,
            "id_passive": "double_attack_back_to_normal"
        }


# ----------------------------------------------------------------------------------------------------------------------

PASSIVE_EFFECTS = {
    "reduce_damage": reduce_damage,
    "ignore_enemy_passive": ignore_enemy_passive,
    "double_attack_below_half": double_attack_below_half,
}