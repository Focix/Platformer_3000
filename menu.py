from tkinter import *
class Menu():
    """
    Класс, создающий меню, по нажатию enter в котором начинается игра
    """
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = Label(canvas, text='Press Enter to start')
        self.started = False
        self.canvas.bind_all('<KeyPress-Down>', self.start_game)# после нажатия enter игра начинается

    def start_game(self, event):
        self.started = True
