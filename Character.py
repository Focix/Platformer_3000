from platform_map import *
from tkinter import *
import time

class Hero():
    def __init__(self, x, y, canv):
        self.x = x
        self.y = y
        self.canvas = canv
        self.id = canv.create_rectangle(self.x, self.y, self.x + 20,
                                          self.y + 10, fill="blue")
        self.Vx = 20
        self.Vy = 0
        self.health = 20

        self.on_platform = True
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Up>', self.jump)


    def magnet_to_platform(self):
        self.on_platform = False
        for platform in platform_list:
            if self.Vy <= 0 and self.x + 20 <= platform.x + 100 \
                    and self.x  >= platform.x \
                    and self.y   - platform.y >= -10 \
                    and self.y   - platform.y <=0:
                self.y = platform.y -10
                self.Vy = 0
                self.on_platform = True
        if not self.on_platform:
            self.y -= self.Vy
            self.Vy -= 0.4

    def turn_right(self, event):
        self.x += self.Vx


    def turn_left(self, event):
        self.x -= self.Vx


    def jump(self, event):
        if self.on_platform:
            self.Vy = 10
            self.on_platform = False


    def draw(self,canv):

        self.magnet_to_platform()
        canv.delete(self.id)
        self.id = canv.create_rectangle(self.x, self.y, self.x + 20,
                                        self.y + 10, fill="blue")

    def decrease_health(self, x):
        self.health -= x


if __name__ == "__main__":

    tk = Tk()  # создаём новый объект — окно с игровым полем, в нашем случае переменная окна называется tk
    tk.title(
        'Game')  # делаем заголовок окна — Games с помощью свойства объекта title
    tk.resizable(0,
                 0)  # запрещаем менять размеры окна, для этого используем свойство resizable
    canvas = Canvas(tk, width=500, height=400,
                    highlightthickness=0)  # создаём новый холст — 400 на 500 пикселей, где и будем рисовать игру
    canvas.pack()  # говорим холсту, что у каждого видимого элемента будут свои отдельные координаты
    tk.update()  # обновляем окно с холстом
    global platform_list
    pl1 = Platform(50, 330, "red", canvas)
    pl2 = Platform(150, 250, 'orange', canvas)

    platform_list = [pl1, pl2 ]
    global dt
    dt = 0.01
    hero = Hero(50, 320, canvas)
    tk.update()
    while hero.health>0:
        hero.draw(canvas)
        tk.update()
        time.sleep(0.01)
    print(type(hero.id))
    print("This module is not for direct call!")
