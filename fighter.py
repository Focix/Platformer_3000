from Character import *
import time


class Fighter:

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
        self.width = 40
        self.height = 40
        self.attacking = False
        self.image1 = PhotoImage(file='таракан лево.png')
        self.image2 = PhotoImage(file='таракан право.png')
        self.skull_image = PhotoImage(file='череп.png')
        self.skull_id = None
        self.id = self.canvas.create_image(self.x, self.y, anchor=CENTER,
                                           image=self.image2)

    def attack(self, hero, list):
        self.attack_sec = time.monotonic()
        if ((0 <= hero.x - self.x - self.width / 2 <= 2 * hero.width
             and self.right) or
            (0 <= self.x - self.width / 2 - hero.x <= 2 * hero.width
             and not self.right)) \
                and self.y - self.height < hero.y + hero.height < \
                self.y + self.height and \
                self.attack_sec - self.sec_after_last_attack > 3:
            if self.Vx > 0:
                self.right = True
            else:
                self.right = False
            self.Vx = 0
            hero.health -= 1
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


if __name__ == "__main__":
    print("This module is not for direct call!")
