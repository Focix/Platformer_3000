def shooter.draw(map, shooter):
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


def fighter.draw(map, fighter):
    """Создаёт отображаемый объект бойца.

    Параметры:

    **space** — холст для рисования.
    **fighter** — объект бойца.
"""
    x = fighter.x
    y = fighter.y
    a = fighter.a
    if bullet.time == 1:
        fighter.image = map.create_rectangle(x - a//2, y - a//2, x + a//2, y + a//2,fill="blue")

def bullet.draw(map, bullet, shooter):
    """Создаёт отображаемый объект пули.

    Параметры:

    **map** — холст для рисования.
    **bullet** — объект пули.
    """
    x = shooter.x
    y = shooter.y
    length = bullet.length
    width = bullet.width
    if bullet.time == 1:
        shooter.image = map.create_rectangle(x - length//2, y - width//2, x + length//2, y + width//2,fill="black")