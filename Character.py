from platform_map import *
from tkinter import *
from fighter import *
from shooter import *
import time


class Hero:
    def __init__(self, x, y, canv):
        self.x = x
        self.y = y
        self.step = True
        self.canvas = canv
        self.width = 20
        self.height = 30
        self.id = self.canvas.create_image(self.x, self.y, anchor=CENTER,
                                           image=obj2)
        self.Vx = 10
        self.Vy = 0
        self.health = 5
        self.on_platform = True
        self.right = True
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Up>', self.jump)

    def magnet_to_platform(self):
        self.on_platform = False
        for platform in platform_list:
            if self.Vy >= 0 and \
                    0 < self.y - platform.y - platform.height <= 20 \
                    and platform.x + platform.width >= \
                    self.x >= platform.x:
                self.Vy = - self.Vy
                break
            if self.Vy <= 0 \
                    and platform.x + platform.width >= \
                    self.x + self.width / 2 >= platform.x \
                    and -self.height <= self.y - platform.y <= 0:
                self.y = platform.y - self.height
                self.Vy = 0
                self.on_platform = True
                break
        if not self.on_platform:
            self.y -= self.Vy
            self.Vy -= 0.45

    def turn_right(self, event):
        self.x += self.Vx
        self.right = True
        self.step = not self.step
        for platform in platform_list:
            platform.following(self)
        for enemy in enemies_list:
            enemy.following(self)
        finish.following(self)

    def turn_left(self, event):
        self.x -= self.Vx
        self.right = False
        self.step = not self.step
        for platform in platform_list:
            platform.following(self)
        for enemy in enemies_list:
            enemy.following(self)
        for bullet in bullet_list:
            bullet.following(self)
        finish.following(self)

    def jump(self, event):
        if self.on_platform:
            self.Vy = 12
            self.on_platform = False

    def draw(self):
        self.fall()
        self.magnet_to_platform()
        self.canvas.delete(self.id)
        if self.Vy != 0:
            if not self.right:
                self.id = self.canvas.create_image(self.x, self.y,
                                                   anchor=CENTER,
                                                   image=obj1)
            else:
                self.id = self.canvas.create_image(self.x, self.y,
                                                   anchor=CENTER,
                                                   image=obj2)

        elif self.right:
            if self.step:
                self.id = self.canvas.create_image(self.x, self.y,
                                                   anchor=CENTER,
                                                   image=obj_right1)
            else:
                self.id = self.canvas.create_image(self.x, self.y,
                                                   anchor=CENTER,
                                                   image=obj_right2)
        else:
            if self.step:
                self.id = self.canvas.create_image(self.x, self.y,
                                                   anchor=CENTER,
                                                   image=obj_left1)
            else:
                self.id = self.canvas.create_image(self.x, self.y,
                                                   anchor=CENTER,
                                                   image=obj_left2)

    def fall(self):
        if self.y > 500:
            self.health = 0

    def hit(self, enemy):
        if self.Vy < 0 and 0 < enemy.y - self.y <= self.height and (
                enemy.x <= self.x + self.width <= enemy.x + enemy.width or
                enemy.x <= self.x <= enemy.x + enemy.width):
            self.canvas.delete(enemy.id)
            enemy.alive = False
            self.Vy = -self.Vy


def game(event):
    filename = PhotoImage(file="кухня.png")
    canvas.create_image(0, 0, anchor=NW, image=filename)
    canvas.delete(name, start)
    global finish
    pl1 = Platform(100, 350, "red", canvas)
    pl2 = Platform(150, 240, 'orange', canvas)
    pl3 = Platform(350, 290, 'green', canvas)
    pl4 = Platform(540, 250, 'green', canvas)
    pl5 = Platform(760, 160, "red", canvas)
    global platform_list, enemies_list
    platform_list = [pl1, pl2, pl3, pl4, pl5]
    finish_x = platform_list[-1].x + 50
    finish_y = platform_list[-1].y
    finish = Finish(finish_x, finish_y, canvas)
    global obj1, obj2, obj_right1, obj_right2, obj_left1, obj_left2
    obj1 = PhotoImage(file='лида лево.png')
    obj2 = PhotoImage(file='лида право.png')
    obj_right1 = PhotoImage(file='мал лида идет направо 1.png')
    obj_right2 = PhotoImage(file='мал лида идет направо 2.png')
    obj_left1 = PhotoImage(file='мал лида налево 1.png')
    obj_left2 = PhotoImage(file='мал лида налево2.png')
    hero = Hero(100, 320, canvas)
    enemy1 = Fighter(canvas, 1, platform_list)
    enemy2 = Shooter(canvas, 3, platform_list)
    enemies_list = [enemy1, enemy2]
    global bullet_list
    bullet_list = []
    tk.update()
    hp = canvas.create_text(30, 30, text=hero.health, font='28')
    timer = time.monotonic()
    time_now = time.monotonic() - timer
    tm = canvas.create_text(450, 30, text=time_now, font='28')
    global game_finished
    while not game_finished:
        if abs(hero.x - finish.x) <= hero.width / 2 and abs(
                hero.y - finish.y) <= hero.height:
            game_finished = True
            break
        if hero.health <= 0:
            game_finished = True
            break
        for enemy in enemies_list:
            if not enemy.alive:
                if enemy.skull_count >= 80:
                    enemies_list.remove(enemy)
                    canvas.delete(enemy.skull_id)
                else:
                    enemy.skull()
            else:
                enemy.attack(hero, bullet_list)
                enemy.draw()
        for enemy in enemies_list:
            if enemy.alive:
                hero.hit(enemy)
        for bullet in bullet_list:
            bullet.move(hero)
            if bullet.get:
                bullet_list.remove(bullet)
        hero.draw()
        tk.update()
        canvas.delete(hp)
        canvas.delete(tm)
        time_now = time.monotonic() - timer
        time_now = float('{:.1f}'.format(time_now))
        hp = canvas.create_text(30, 30, text=hero.health, font='28',
                                fill='#FF0000')
        tm = canvas.create_text(450, 30, text=time_now, font='28')
        time.sleep(0.01)
    time.sleep(2)
    canvas.delete('all')
    if hero.health <= 0:
        canvas.create_text(250, 250, text='You died.', font='Time 34', fill='black')
    else:
        canvas.create_text(250, 250, text='You won!', font='Time 34', fill='black')


if __name__ == "__main__":
    tk = Tk()
    tk.title("Polina vs Cockroaches")
    tk.resizable(0, 0)
    canvas = Canvas(tk, width=500, height=500, highlightthickness=0)
    canvas.pack()
    game_finished = False
    name = canvas.create_text(250, 250, text='Polina vs Cockroaches',
                              font='Time 34', fill='red')
    start = canvas.create_text(250, 480, text='Press enter to start',
                               fill='black')
    canvas.bind_all('<KeyPress-Return>', game)
    tk.mainloop()
