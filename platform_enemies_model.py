def move_enemies_fighter(map, body, hero, base, dt):
    """Перемещает бойца 
        hero - главный герой (гг)
        map - вся наша карта, ну или платформа
        base - объект, по которому движется боец
       **body** — боец, которого нужно переместить.
       hero.x - наверное левый край героя
    """    
    body.x += body.Vx * dt

    if body.x - body.a//2 >= base.x0 or body.x + body.a//2 >= base.x1 : 
        body.Vx = -body.Vx
    if hero.x == body.x - body.a and hero.y == base.y : # Тут должно быть условие столкновения бойца с гг
        body.health -= 1
        hero.health -= 1
    if body.health == 0:
        body.time = 0
    map.move(body.image, body.Vx, body.Vy)


def move_enemies_bullet(map, body, hero, base, shooter, dt):
   """Перемещает пулю 
        hero - главный герой (гг)
        map - вся наша карта, ну или платформа
        base - объект, по которому движется гг
       **body** — пуля, которую нужно переместить.
    """  
    body.x = shooter.x - shooter.a//2
    body.x += body.Vx * dt
    if hero.y == base.y and hero.x >= base.x0 and hero.x <= base.x1 : # Тут должно быть условие появления пули (когда гг достаточно длизок к стрелку)
        bullet.time = 1
    if hero.x == body.x - body.length or shooter.health == 0 : # Тут должно быть условие столкновения пули с гг
        bullet.time = 0
        hero.helth -= 1
    map.move(body.image, body.Vx, body.Vy)

'''
    body.x, body.y, body.Vx, body.Vy, body.a = tuple
    map.move(body.image, body.Vx, body.Vy)
    if hero.x == body.x - body.a and hero.y == body.y - body.a:
        body.x = -body.x
        body.Vx = -body.Vx
    if body.x - body.a == base.x0 or body.x + body.a == base.x1 :
        body.body.Vx = -body.Vx
    new_tuple_fighter = body.x + body.Vx*dt, body.y + body.Vy*dt, body.Vx, body.Vy, body.a # фиксирую новые параметры шарика
    return new_tuple_fighter
    '''

    def recalculate_map_objects_positions(map, map_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **fighter** — боец
    **bullet** - пуля
    **dt** — шаг по времени
    """
    for body in map_objects:
        move_enemies_fighter(map, body, hero, base, dt)
        move_enemies_bullet(map, body, hero, base, dt)