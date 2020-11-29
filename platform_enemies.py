import tkinter
from tkinter.filedialog import *
from platform_enemies_model import *
from platform_enemies_vis import *
class Shooter:
    """Тип данных, описывающий стрелка.
    Содержит координаты, размер, число жизней стрелка,
    а также его цвет.
    """
    type = "shooter"
    """Признак объекта стрелка"""
    health = ...
    """Количество жизней стрелка"""
    time = 1
    """Параметр, отвечающий за жизнь стрелка"""
    x = ...
    """Координата по оси **x**"""
    y = ...
    """Координата по оси **y**"""    
    a = ...
    """Сторона квадрата стрелка"""
    color = "black"
    """Цвет стрелка"""
    image = None
    """Изображение стрелка"""


class Fighter:
    """Тип данных, описывающий бойца(это тот, кто руками бьёт гг).
    Содержит координаты, размер, скорость движения, количество жизней бойца,
    а также его цвет.
    """
    type = "Fighter"
    """Признак объекта бойца"""
    health = ...
    """Количество жизней бойца """
    time = 1
    """Параметр, отвечающий за жизнь бойца"""
    x = ...
    """Координата по оси **x**"""
    Vx = ...
    """Скорость по оси **x**"""
    a = ...
    """Сторона квадрата бойца"""
    color = "blue"
    """Цвет бойца"""
    image = None
    """Изображение бойца"""

class Bullet:
    """Тип данных, описывающий пулю.
    Содержит  координаты, скорость, размеры пули,
    а её цвет.
    """
    type = "bullet"
    """Признак объекта пуля"""
    x = ...
    """Координата по оси **x**"""
    y = ...
    """Координата по оси **y**"""
    Vx = ...
    """Скорость пули """
    time = 0
    """Параметр, отвечающий за жизнь пули"""
    length = ...
    """Длина прямоугольника пули"""
    width = ...
    """Ширина прямоугольника пули"""
    color = "black"
    """Цвет пули"""
    image = None
    """Изображение пули"""

if __name__ == "__main__":
        print("This module is not for direct call!")