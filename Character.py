

class Hero():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.Vx = 5
        self.Vy = 0
        self.health = 20
        self.mana = 20
        self.stamina = 20
        self.money = 0
        self.Cast = False
        self.Run = False
        self.Dead = False
        
    def set_health(x):
        self.health = x

    def set_mana(x):
        self.mana = x

    def set_stamina(x):
        self.stamina = x

    def set_money(x):
        self.money = x

    def move_hero(direction):
        if y > 0:
            a = -10
        else:
            a = 0
            y = 0
        self.y += Vy * t + a * t**2 / 2
        Vy -= a * t
        self.x += Vx * t

    def Jump():
        Vy = 30

    def Sprint_On():
        self.Run = True
        Vx = 10

    def Sprint_Off():
        Vx = 5
        self.Run = False

    def decrease_health(x):
        self.health -= x
    
    def set_hero_position(x, y):
        self.x = x
        self.y = y
    
    def decrease_stamina(x):
        self.stamina -= x


if __name__ == "__main__":
    print("This module is not for direct call!")