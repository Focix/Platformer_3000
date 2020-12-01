from Character import *
class Platform():
    def __init__(self, x, y, color, canvas):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.height = 20
        self.widht = 100
        self.id = canvas.create_rectangle(self.x, self.y, self.x+self.widht, self.y+self.height, fill=self.color)

    def following(self, hero):
        if hero.right:
            self.canvas.delete(self.id)
            self.x -=hero.Vx
            self.id = self.canvas.create_rectangle(self.x, self.y, self.x+self.widht, self.y+self.height, fill=self.color)
        else:
            self.canvas.delete(self.id)
            self.x +=hero.Vx
            self.id = self.canvas.create_rectangle(self.x, self.y,
                                                   self.x + self.widht,
                                                   self.y + self.height,
                                                   fill=self.color)


