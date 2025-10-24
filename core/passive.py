# passive.py
from Project_P.core.passive_effects import PASSIVE_EFFECTS

class Passive:
    def __init__(self, name, description, trigger, effect_id, **kwargs):
        self.name = name
        self.description = description
        self.trigger = trigger
        self.effect_id = effect_id
        self.kwargs = kwargs

    def apply(self, user, target, damage=0, **extra):
        effect_func = PASSIVE_EFFECTS.get(self.effect_id)
        if not effect_func:
            return {"text": f"Effet inconnu : {self.effect_id}"}
        print("apply de Passive fonctionne!")
        return effect_func(user=user, target=target, damage=damage, **self.kwargs)
