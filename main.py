from tkinter import *
from platform_enemies_vis import *
from platform_enemies import *
from Character import *
from platform_map import *
from platform_enemies_model import *
import time


tk = Tk() # создаём новый объект — окно с игровым полем, в нашем случае переменная окна называется tk
tk.title('Game') # делаем заголовок окна — Games с помощью свойства объекта title
tk.resizable(0, 0) # запрещаем менять размеры окна, для этого используем свойство resizable
tk.wm_attributes('-topmost', 1)  # помещаем наше игровое окно выше остальных окон на компьютере
canvas = Canvas(tk, width=500, height=400, highlightthickness=0) # создаём новый холст — 400 на 500 пикселей, где и будем рисовать игру
canvas.pack()  # говорим холсту, что у каждого видимого элемента будут свои отдельные координаты
tk.update() # обновляем окно с холстом


physical_time = 0

displayed_time = None

time_step = None

x_start = 100
y_start = 50

"""
включение меню
"""
menu = Menu(canvas)
"""
загрузка карты, врагов и героев
"""
pl1 = Platform(100, 50, "red", canvas)
global platform_list
platform_list = [pl1]
#score = Score(canvas) #создает объект счет
hero = Hero(x_start, y_start, canvas)# создает объект героя
#fighter = Fighter(canvas, x, y)
#shooter = Shooter(canvas, x, y)
#enemies_list = [fighter, shooter]# создает лист врагов


        #map.draw()
tk.update()

        #score.draw()
        #for enemy in enemies_list:
            #enemy.draw()
        #тут должны выполяняться бинды на движение героя
while hero.x<=500:
    hero.draw(canvas)
    tk.update()
    time.sleep(0.01)




time.sleep(3)
"""
каждый промежуток времени обновлять положение врагов и проверять, если нажата
кнопка вправо, то движение вправо; если влево, то влево; если вверх, то прыжок;
если пробел, то удар
"""


"""
если пуля попала по герою, то отнять один хп
если героя ударил враг, то отнять один хп
"""

"""
если герой ударил врага, то убить врага
"""

"""
если герой умер, то вывести экран с меню
"""