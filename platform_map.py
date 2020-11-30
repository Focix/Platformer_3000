class Platform():
    def __init__(self, x, y, color, canvas):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.id = canvas.create_rectangle(x, y, x+100, y+20, fill=color)


