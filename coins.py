from Character import *


class Coin:
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y - 5
        self.width = 25
        self.height = 20
        self.canvas = canvas
        self.image = PhotoImage(file='крыса.png')
        self.id = self.canvas.create_image(self.x, self.y, anchor=CENTER,
                                           image=self.image)

    def taken(self, hero, coins_list):
        if (hero.x - self.x) ** 2 + (hero.y - self.y) ** 2 <= (
                2 * self.width) ** 2:
            hero.coins += 1
            self.canvas.delete(self.id)
            coins_list.remove(self)

    def following(self, hero):
        if hero.right:
            self.canvas.delete(self.id)
            self.x -= hero.Vx
            self.id = self.canvas.create_image(self.x, self.y, anchor=CENTER,
                                               image=self.image)

        else:
            self.canvas.delete(self.id)
            self.x += hero.Vx
            self.id = self.canvas.create_image(self.x, self.y, anchor=CENTER,
                                               image=self.image)
