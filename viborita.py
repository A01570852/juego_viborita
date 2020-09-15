#A00827826 Edgar Castillo
#A01570852 Luis Martínez

"""
Programa del juego snake.
"""

from turtle import *
from random import randrange
from freegames import square, vector

#Vector con los 5 colores que se pueden presentar (comida y víbora)
color = ['gray','blue','green','black','yellow']
snakeIndex=randrange(5)
foodIndex=randrange(5)

#Si se llegan a repetir, los vuelve a mezclar aleatoriamente hasta que sean distintos.
while snakeIndex == foodIndex:
    snakeIndex=randrange(5)
    foodIndex=randrange(5)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
cont = 0

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y
    global cont
    cont = cont + 1
    
    """
    Si la comida está dentro de la ventana y el usuario ha dado un movimiento (esto es modificable, pueden ser
    más movimientos) la primera se moverá hacia cualquier dirección, una cantidad de 10 pixeles. Si se sale de
    la ventana, reposicionará la comida a una ubicación aleatoria y mandará un mensaje.
    """
    if inside(food):
        if(cont == 1):
            index = randrange(1,5)
            if (index == 1):
                food.x += 10
            elif(index == 2):
                food.y += 10
            elif(index == 3):
                food.x -= 10
            else:
                food.y -= 10
            cont = 0;
    else:
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        print('La comida se salió del tablero.')
        cont = 0

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    #Se usa el índice aleatorio que se haya obtenido en un inicio
    for body in snake:
        square(body.x, body.y, 9, color[snakeIndex])

    square(food.x, food.y, 9, color[foodIndex])
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()