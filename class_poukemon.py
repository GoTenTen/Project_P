
class Pou:
    def __init__(self,owner,  name, hp, atk, comp):
        self.owner = owner
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.comp = comp

    def is_alive(self):
        return self.hp > 0
    
    def t_damage(self, x): #take_damage
        self.hp -= x  
        if self.hp < 0:
            self.hp = 0

P = Pou #alias permettant d'appeler la classe p au lieu de pou

class comps:
    def __init__(self, name, mult, sign, type):
        self.name = name
        self.mult = mult
        self.sign = sign # '*', '+', '-', '/'
        self.type = type #buff/debuff/attaque/heal

    def comp_stats(self, user, target):
        if self.type != "heal":
            if self.sign == "*":
                return user.atk * self.mult
            elif self.sign == "/":    
                if target:
                    target.atk = target.atk / self.mult
                    return target.atk
        else:
            if user.hp < user.max_hp:
                return user.hp + (user.max_hp / 3)
    
    def comp_atk(self, user, target):    
        target.hp -= (user.atk * self.mult)
        return (user.atk * self.mult)
        

chidori = comps("chi", 2, "*", 'buff')
chidori2 = comps("chi2", 2, "+",'buff')
chidori3 = comps("chi3", 2, "/",'debuff')
chidori4 = comps("chi4", 0, "+", 'heal')
tapefort = comps("tape", 2.5, "*", 'attaque')

