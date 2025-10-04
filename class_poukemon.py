
class Pou:
    def __init__(self, owner, name, hp, atk):
        self.owner = owner
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk

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

    def use_c(self, user, target = None):
        if self.type != "heal":
            if self.sign == "*":
                return user.atk * self.mult
            elif self.sign == "+":
                return user.atk + self.mult
            elif self.sign == "-":
                if target:
                    target.atk = target.atk - self.mult
                    return target.atk
            elif self.sign == "/":    
                if target:
                    target.atk = target.atk / self.mult
                    return target.atk
        else:
            if self.hp < self.max_hp:
                return self.hp + (self.max_hp / 3)


Pou1 = P("Pou", 35, 5)
Pou2 = P("Pou", 35, 5)

chidori = comps("chi", 2, "*", 'buff')
chidori2 = comps("chi2", 2, "+",'buff')
chidori3 = comps("chi3", 2, "/",'debuff')
'''chidori4 = comps("chi4", None, "+", 'heal')'''


def test():
    print(f"Les hp de Pou1 sont {Pou1.hp}\n")
    print(f"Les hp de Pou2 sont {Pou2.hp}\n")
    chidori3.use_c(Pou1, Pou2)
    print(f"L'attaque de pou2 baisse de 5 a {Pou2.atk}\n")
    Pou1.t_damage(Pou2.atk)
    print(f"Les hp de Pou1 sont {Pou1.hp}\n")
    '''chidori4.use_c(Pou1, Pou1)
    print(f"Les hp de Pou1 sont {Pou1.hp}\n")'''
    
test()