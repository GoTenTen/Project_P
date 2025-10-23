#skills.py
import random
import time

class Skill:
    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description
        self.kwargs = kwargs

    def apply(self, user, target):
        raise NotImplementedError("Cette compétence n'est pas encore définie.")


class AttackSkill(Skill):
    def __init__(self, name, description, **kwargs):
        super().__init__(name, description)
        self.kwargs = kwargs  # stocke les paramètres de dégâts

    def get_multi_hit(self):
        if self.kwargs.get('multi_hit_range', 1):
            return random.randint(*self.kwargs.get('multi_hit_range', (1,1)))  # "*" est utilisé pour débaler l'argument "(1,5)" devient "1,5"
        return 1

    def apply(self, user, target):
        total_damage = 0
        hits = self.get_multi_hit()
        bonus_message = self.kwargs.get("bonus_message", None)
        self_damage = self.kwargs.get("self_damage", 0)
        accuracy = self.kwargs.get("accuracy", 1.0)

        # On prépare une liste "d’événements"
        events = []

        # message standard
        events.append({
            "type_events": "announce"
        })

        successful_hit = False  # pour savoir si au moins un coup a touché
        miss = False

        for i in range(hits):
            # Vérifie la précision
            if random.random() > accuracy:
                miss = True
                events.append({
                    "type_events": "miss",
                    "i": i
                })
                continue # si raté, termine ce tour de boucle

            # Coup réussi
            successful_hit = True
            damage, crit, elem_efficacity = user.deal_damage(target, **self.kwargs, miss=miss)
            total_damage += damage
            crit_txt = "(Critique!)" if crit else ""
            events.append({
                "type_events": "hits_and_crits",
                "hits": hits,
                "damage": damage,
                "crit_txt": crit_txt,
                "i": i
            })

        # affiche les messages bonus que s'il y a au moins un coup réussi
        if successful_hit:
            if bonus_message: # message bonus optionnel
                events.append({
                    "type_events": "bonus_message",
                    "bonus_message": bonus_message
                })
            if elem_efficacity:
                events.append({
                    "type_events" : "elem_efficacity",
                    "elem_efficacity" : elem_efficacity
                })

        if self_damage >= 1:
            user.take_damage(self_damage)
            events.append({
                "type_events": "self_damage",
                "self_damage": self_damage
            })

        return {
            "type_skill": "attack",
            "user": user,
            "target_name": target.name,
            "target_owner": target.owner,
            "total_damage": total_damage,
            "events": events,
            "comp_name": self.name
        }

class BuffSkill(Skill):
    """Compétence de buff."""
    def apply(self, user, target=None):
        stat = self.kwargs.get("stat", "atk")
        factor = self.kwargs.get("factor", 2.0)
        before = getattr(user, stat)
        setattr(user, stat, int(before * factor))
        return {
            "type_skill": "buff",
            "user": user,
            "comp_name": self.name,
            "stat_id": stat.upper(),
            "before": before,
            "stat_value": getattr(user, stat)
        }

class TimedBuffSkill(BuffSkill):
    def apply(self, user, target=None):
        stat = self.kwargs.get("stat", "atk")
        factor = self.kwargs.get("factor", 1.5)
        duration = self.kwargs.get("duration", 3)

        user.add_buff(stat, factor, duration)
        return {
            "type_skill": "timed_buff",
            "user": user,
            "comp_name": self.name,
            "stat_id": stat.upper(),
            "duration": duration,
        }

class HealSkill(Skill):
    """Compétence de soin."""
    def __init__(self, name, description, amount):
        super().__init__(name, description)
        self.amount = amount

    def apply(self, user, target=None):
        #return user.heal(self.amount)
        healed = min(self.amount, user.max_hp - user.hp)
        user.hp += healed
        return {
            "type_skill": "heal",
            "user": user,
            "comp_name": self.name,
            "user_hp": user.hp,
            "amount": healed,
        }
        
class TimedHealSkill(Skill):
    def apply(self, user, target=None):  #un truc que j'ai pas compris c'est tes init et super init, ici ça fonctionne ça, si tu penses que c'est mieux avec modifies
        amount = self.kwargs.get("amount", 0)
        duration = self.kwargs.get("duration", 0)
        stat = self.kwargs.get("stat", "hp")
        user.add_heal(stat, amount, duration, self.name)
        return {
            "type_skill": "timed_heal",
            "user": user,
            "comp_name": self.name,
            "amount": amount,
            "duration": duration,
        }