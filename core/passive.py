# passive.py

class Passive:
    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description
        self.kwargs = kwargs

    def apply(self, user, target, damage, **kwargs):
        raise NotImplementedError("Ce passif n'est pas encore défini.")


class OnAttack(Passive):
    """Passif qui s'éxecute lors de l'attaque"""
    def __init__(self, name, description, **kwargs):
        super().__init__(name, description)
        self.kwargs = kwargs

    def apply(self, user, target, damage, **kwargs):
        ignore_passive = self.kwargs.get('ignore_passive', False)

        if ignore_passive:
            target.flags['passive_ignored'] = True
            return {
                "damage": damage,
                "text" : f"Grace à son passif {self.name}, {user.name} ignore le passif de {target.name}!"
            }

        return {
            "text" : ""
        }

class OnReceiveDamage(Passive):
    """Passif qui s'éxecute quand le défenseur recoit des dégats"""
    def __init__(self, name, description, **kwargs):
        super().__init__(name, description)
        self.kwargs = kwargs

    def apply(self, user, target, damage, **kwargs):
        tankiness = self.kwargs.get('tankiness', 0)

        if tankiness > 0:
            new_damage = int(damage * (1 - tankiness))
            return {
                "damage": new_damage,
                "text": f"{user.name} réduit les dégats subit de {int(tankiness*100)}% grace à son passif {self.name} !"
            }

        return {
            "text" : ""
        }


class OnTurnStart(Passive):
    """Passif qui s'éxecute en début de tour"""
    def __init__(self, name, description, **kwargs):
        super().__init__(name, description)
        self.kwargs = kwargs

    def apply(self, user, target, damage, **kwargs):
        stat_multiplier = self.kwargs.get('stat_multiplier', 1)
        hp_condition = self.kwargs.get('hp_condition', 1)

        if not user.flags['turnstart_passive_applied']:
            if user.hp <= (user.hp_max * hp_condition):
                user.atk *= stat_multiplier
                user.flags['turnstart_passive_applied'] = True
                return {
                    "text": f"{user.name} ne lache rien est voit son attaque doublée !"
                }

        return {
            "text" : ""
        }

class OnTurnEnd(Passive):
    """Passif qui s'éxecute en fin de tour"""
    def __init__(self, name, description, amount):
        super().__init__(name, description)
        self.amount = amount

    def apply(self, user, target, damage, **kwargs):
        pass