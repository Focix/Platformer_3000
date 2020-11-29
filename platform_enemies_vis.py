import tkinter
from tkinter.filedialog import *

def create_shooter_image(map, shooter):
    """Создаёт отображаемый объект стрелка(стрелок - АФК персонаж).

    Параметры:

    **map** — холст для рисования.
    **shooter** — объект стрелка.
    """
    x = shooter.x
    y = shooter.y
    a = shooter.a
    if bullet.time == 1:
        shooter.image = map.create_rectangle(x - a//2, y - a//2, x + a//2, y + a//2,fill="white")


def create_fighter_image(map, fighter):
    """Создаёт отображаемый объект бойца.

    Параметры:

    **space** — холст для рисования.
    **fighter** — объект бойца.
    
    x = scale_x(planet.x)
    y = scale_y(planet.y)
    r = planet.R
    planet.image = space.create_oval([x - r, y - r], [x + r, y + r],
                                     fill=planet.color)
"""
    x = fighter.x
    y = fighter.y
    a = fighter.a
    if bullet.time == 1:
        fighter.image = map.create_rectangle(x - a//2, y - a//2, x + a//2, y + a//2,fill="blue")

def create_bullet_image(map, bullet):
    """Создаёт отображаемый объект пули.

    Параметры:

    **map** — холст для рисования.
    **bullet** — объект пули.
    """
    x = bullet.x
    y = bullet.y
    length = bullet.length
    width = bullet.width
    if bullet.time == 1:
        shooter.image = map.create_rectangle(x - length//2, y - width//2, x + length//2, y + width//2,fill="black")

if __name__ == "__main__":
    print("This module is not for direct call!")