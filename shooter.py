from Character import *
import time


class Shooter:
    def __init__(self, canv, i, platform_list):
        self.canvas = canv
        self.list = platform_list
        self.platform = i
        self.alive = True
        self.skull_count = 0
        self.x = platform_list[i].x
        self.y = platform_list[i].y - 30
        self.Vx = 0.3
        self.last_Vx = self.Vx
        self.right = True
        self.health = 1
        self.attack_sec = 0
        self.sec_after_last_attack = 0
        self.width = 50
        self.height = 40
        self.attacking = False
        self.image1 = PhotoImage(file='паук лево.png')
        self.image2 = PhotoImage(file='паук право.png')
        self.skull_image = PhotoImage(file='череп.png')
        self.skull_id = None
        self.id = self.canvas.create_image(self.x, self.y, anchor=CENTER,
                                           image=self.image2)

    def attack(self, hero, list):
        """
        Описывает паттерн аттаки противника, создает пулю,
        если персонаж находится достаточно близко
        """
        self.attack_sec = time.monotonic()
        if ((0 <= hero.x - self.x - self.width / 2 <= 6 * hero.width
             and self.right) or
            (0 <= self.x - self.width / 2 - hero.x <= 6 * hero.width
             and not self.right)) \
                and self.y - self.height < hero.y + hero.height < \
                self.y + self.height and \
                self.attack_sec - self.sec_after_last_attack > 3:
            if self.Vx > 0:
                self.right = True
                bullet = Bullet(self.canvas, self.x, self.y, True)
            else:
                self.right = False
                bullet = Bullet(self.canvas, self.x, self.y, False)
            list.append(bullet)
            self.Vx = 0
            self.sec_after_last_attack = time.monotonic()

            self.attacking = True
        else:
            if self.attacking and \
                    time.monotonic() - self.sec_after_last_attack > 3:
                if self.right:
                    self.Vx = 0.3
                else:
                    self.Vx = -0.3
                self.attacking = False

    def following(self, hero):
        """
               Перемещает объект при движении героя
               """
        if hero.right and self.x - hero.Vx > self.list[self.platform].x:
            self.canvas.delete(self.id)
            self.x -= hero.Vx
        else:
            self.canvas.delete(self.id)
            self.x += hero.Vx

    def draw(self):
        if self.x + self.Vx - self.list[self.platform].x <= self.Vx:
            self.x = self.list[self.platform].x
            self.Vx = -self.Vx
            self.right = True
        elif self.list[self.platform].x + \
                self.list[self.platform].width - self.x - \
                self.Vx < self.Vx:
            self.x = self.list[self.platform].x + self.list[
                self.platform].width
            self.Vx = -self.Vx
            self.right = False
        self.x += self.Vx
        if self.right:
            self.new_id_right()
        else:
            self.new_id_left()

    def new_id_left(self):
        self.canvas.delete(self.id)
        self.id = self.canvas.create_image(self.x, self.y, anchor=CENTER,
                                           image=self.image1)

    def new_id_right(self):
        self.canvas.delete(self.id)
        self.id = self.canvas.create_image(self.x, self.y, anchor=CENTER,
                                           image=self.image2)

    def skull(self):
        self.canvas.delete(self.skull_id)
        self.skull_id = self.canvas.create_image(self.x, self.y - self.height -
                                                 0.5 * self.skull_count,
                                                 anchor=CENTER,
                                                 image=self.skull_image)
        self.skull_count += 1


class Bullet:
    def __init__(self, canvas, x, y, direction):
        self.x = x
        self.y = y
        self.get = False
        self.canvas = canvas
        self.right = direction
        if self.right:
            self.Vx = 1.5
        else:
            self.Vx = -1.5
        self.id = self.canvas.create_oval(self.x - 10, self.y + 10,
                                          self.x + 10, self.y - 10,
                                          fill='white', width=2)

    def move(self, hero):
        """
        Перемещает пулю и проверяет, попала ли она в героя
        """
        if (hero.x - self.x) ** 2 + (hero.y - self.y) ** 2 <= hero.width ** 2:
            hero.health -= 1
            self.canvas.delete(self.id)
            self.get = True
        elif (hero.x - self.x) ** 2 + (hero.y - self.y) ** 2 >= 500 ** 2:
            self.canvas.delete(self.id)
        else:
            self.x += self.Vx
            self.canvas.delete(self.id)
            self.id = self.canvas.create_oval(self.x - 10, self.y + 10,
                                              self.x + 10, self.y - 10,
                                              width=2, fill='white')

    def following(self, hero):
        """
               Перемещает объект при движении героя
               """
        if hero.right:
            self.canvas.delete(self.id)
            self.x -= hero.Vx

        else:
            self.canvas.delete(self.id)
            self.x += hero.Vx


if __name__ == "__main__":
    print("This module is not for direct call!")
