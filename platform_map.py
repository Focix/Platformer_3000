import random


class Platform:
    def __init__(self, x, y, canvas):
        colors = ["red", 'orange', 'green', 'blue', 'magenta', 'pink', ]
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = random.choice(colors)
        self.height = 20
        self.width = 170
        self.id = canvas.create_rectangle(self.x, self.y, self.x + self.width,
                                          self.y + self.height,
                                          fill=self.color)

    def following(self, hero):
        """
               Перемещает объект при движении героя
               """
        if hero.right:
            self.canvas.delete(self.id)
            self.x -= hero.Vx
            self.id = self.canvas.create_rectangle(self.x, self.y,
                                                   self.x + self.width,
                                                   self.y + self.height,
                                                   fill=self.color)
        else:
            self.canvas.delete(self.id)
            self.x += hero.Vx
            self.id = self.canvas.create_rectangle(self.x, self.y,
                                                   self.x + self.width,
                                                   self.y + self.height,
                                                   fill=self.color)


class Finish:
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.id1 = self.canvas.create_line(self.x, self.y - 50, self.x, self.y,
                                           fill='black')
        self.id2 = self.canvas.create_polygon(self.x, self.y - 50, self.x + 10,
                                              self.y - 37.5, self.x,
                                              self.y - 25, fill='red')

    def following(self, hero):
        """
               Перемещает объект при движении героя
               """
        if hero.right:
            self.canvas.delete(self.id1, self.id2)
            self.x -= hero.Vx
            self.id1 = self.canvas.create_line(self.x, self.y - 50, self.x,
                                               self.y, fill='black')
            self.id2 = self.canvas.create_polygon(self.x, self.y - 50,
                                                  self.x + 10, self.y - 37.5,
                                                  self.x, self.y - 25,
                                                  fill='red')
        else:
            self.canvas.delete(self.id1, self.id2)
            self.x += hero.Vx
            self.id1 = self.canvas.create_line(self.x, self.y - 50, self.x,
                                               self.y, fill='black')
            self.id2 = self.canvas.create_polygon(self.x, self.y - 50,
                                                  self.x + 10, self.y - 37.5,
                                                  self.x, self.y - 25,
                                                  fill='red')


if __name__ == "__main__":
    print("This module is not for direct call!")
