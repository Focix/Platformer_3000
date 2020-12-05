from tkinter import *
from platform_map import *
from Character import *
import time


class Fighter:

    def __init__(self, canv, i, platform_list):
        self.canvas = canv
        self.platform = i
        self.x = platform_list[i].x
        self.y = platform_list[i].y - 30
        self.Vx = -0.3
        self.last_Vx = self.Vx
        self.health = 1
        self.attack_sec = 0
        self.sec_after_last_attack = 0
        self.width = 30
        self.height = 30
        self.attacking = False
        self.id = self.canvas.create_rectangle(self.x, self.y,
                                               self.x + self.width,
                                               self.y + self.height,
                                               fill="black")

    def attack(self, hero):
        self.attack_sec = time.monotonic()
        if abs(hero.x - self.x) <= 2 * hero.width and abs(
                hero.y - self.y) <= self.height - hero.height and \
                self.attack_sec - self.sec_after_last_attack > 3:
            if self.Vx !=0:
                self.last_Vx = self.Vx
                self.Vx = 0
            hero.health -= 1
            self.sec_after_last_attack = time.monotonic()
            print(hero.health)
            self.attacking = True
        else:
            if self.attacking and \
                    time.monotonic() - self.sec_after_last_attack > 3:
                self.Vx = self.last_Vx
                self.attacking = False

    def following(self, hero):
        if hero.right:
            self.canvas.delete(self.id)
            self.x -= hero.Vx
            self.id = self.canvas.create_rectangle(self.x, self.y,
                                                   self.x + self.width,
                                                   self.y + self.height,
                                                   fill='black')
        else:
            self.canvas.delete(self.id)
            self.x += hero.Vx
            self.id = self.canvas.create_rectangle(self.x, self.y,
                                                   self.x + self.width,
                                                   self.y + self.height,
                                                   fill='black')

    def draw(self, platform_list):
        if self.x + self.Vx - platform_list[self.platform].x < self.Vx:
            self.x = platform_list[self.platform].x
            self.Vx = -self.Vx
        elif platform_list[self.platform].x + \
                platform_list[self.platform].width - self.x - \
                self.width - self.Vx < self.Vx:
            self.x = platform_list[self.platform].x + platform_list[
                self.platform].width - self.width
            self.Vx = -self.Vx
        else:
            self.x += self.Vx
        self.canvas.delete(self.id)
        self.id = self.canvas.create_rectangle(self.x, self.y,
                                               self.x + self.width,
                                               self.y + self.height,
                                               fill="black")


if __name__ == "__main__":
    print("This module is not for direct call!")
