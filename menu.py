from tkinter import *
class Menu():
    """
    Класс, создающий меню, по нажатию enter в котором начинается игра
    """
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill="red")
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)# после нажатия enter игра начинается
    def start_game(self, event):
        self.started = True