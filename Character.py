from platform_map import *
from tkinter import *
from platform_enemies import *
import time


class Hero:
    def __init__(self, x, y, canv):
        self.x = x
        self.y = y
        self.canvas = canv
        self.width = 20
        self.height = 10
        self.id = canv.create_rectangle(self.x, self.y, self.x + self.width,
                                        self.y + self.height, fill="blue")
        self.Vx = 15
        self.Vy = 0
        self.health = 5
        self.on_platform = True
        self.right = True
        self.canvas.bind_all('<KeyPress-d>', self.turn_right)
        self.canvas.bind_all('<KeyPress-a>', self.turn_left)
        self.canvas.bind_all('<KeyPress-w>', self.jump)

    def magnet_to_platform(self):
        self.on_platform = False
        for platform in platform_list:
            if self.Vy >= 0 and 0 < self.y - platform.y - platform.height <= 6 \
                    and platform.x + platform.width >= \
                    self.x + self.width / 2 >= platform.x:
                self.Vy = - self.Vy
                break
            if self.Vy <= 0 \
                    and platform.x + platform.width >= \
                    self.x + self.width / 2 >= platform.x \
                    and -self.height <= self.y - platform.y <= 0:
                self.y = platform.y - 10
                self.Vy = 0
                self.on_platform = True
                break
        if not self.on_platform:
            self.y -= self.Vy
            self.Vy -= 0.4

    def turn_right(self, event):
        self.x += self.Vx
        self.right = True
        for platform in platform_list:
            platform.following(self)
        for enemy in enemies_list:
            enemy.following(self)

    def turn_left(self, event):
        self.x -= self.Vx
        self.right = False
        for platform in platform_list:
            platform.following(self)
        for enemy in enemies_list:
            enemy.following(self)

    def jump(self, event):
        if self.on_platform:
            self.Vy = 10
            self.on_platform = False

    def draw(self):
        self.fall()
        self.magnet_to_platform()
        self.canvas.delete(self.id)
        self.id = self.canvas.create_rectangle(self.x, self.y, self.x + 20,
                                               self.y + 10, fill="blue")

    def fall(self):
        if self.y > 400:
            self.health = 0

    def hit(self, enemies_list):
        for enemy in enemies_list:
            if self.Vy<0 and 0<enemy.y - self.y <= self.height and enemy.x <= self.x + self.width / 2 <= enemy.x + enemy.width:
                self.canvas.delete(enemy.id)
                enemies_list.remove(enemy)
                self.Vy = -self.Vy


if __name__ == "__main__":

    tk = Tk()  # создаём новый объект — окно с игровым полем, в нашем случае
    # переменная окна называется tk
    # tk.title("Lida vs cockroachs")
    tk.title('Game')  # делаем заголовок окна — Games с помощью свойства

    # объекта title
    tk.resizable(0, 0)  # запрещаем менять размеры окна, для этого используем
    # свойство resizable
    canvas = Canvas(tk, width=500, height=500, highlightthickness=0)
    # создаём новый холст — 400 на 500 пикселей, где и будем рисовать игру
    canvas.pack()  # говорим холсту, что у каждого видимого элемента будут
    # свои отдельные координаты
    global platform_list
    pl1 = Platform(100, 340, "red", canvas)
    pl2 = Platform(150, 240, 'orange', canvas)
    pl3 = Platform(350, 290, 'green', canvas)
    platform_list = [pl1, pl2, pl3]
    global hero
    hero = Hero(100, 320, canvas)
    global enemies_list
    enemy1 = Fighter(canvas, 1, platform_list)
    enemies_list = [enemy1]
    tk.update()
    k = canvas.create_text(30, 30, text=hero.health, font='28')
    while hero.health > 0:
        for enemy in enemies_list:
            enemy.attack(hero)
            enemy.draw(platform_list)
        hero.draw()
        hero.hit(enemies_list)
        tk.update()
        canvas.delete(k)
        k = canvas.create_text(30, 30, text=hero.health, font='28',
                               fill='#FF0000')
        time.sleep(0.01)
    canvas.create_text(230, 30, text='You died.', font='35', fill='black')
    tk.update()
    time.sleep(3)
