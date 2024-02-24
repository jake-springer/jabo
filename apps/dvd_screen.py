from ..sys.display import Display
from machine import Pin
from random import randint
from math import Vector2D

dim = Vector2D(128, 64)
speed = Vector2D(3, -3)
size = Vector2D(10, 5)
position = Vector2D(0, 0)
display = Display()
#x, y, color


def start_game():
    while (True):
        position.x += speed.x
        position.y += speed.y

        if(position.x > dim.x-size.x):
            position.x = dim.x-size.x
            speed.x *= -1
            
        if(position.x < 0):
            position.x = 0
            speed.x *= -1

        if(position.y > dim.y-size.y):
            position.y = dim.y-size.y
            speed.y *= -1

        if(position.y < 0):
            position.y = 0
            speed.y *= -1

        display.rect(position.x, position.y, size.x, size.y, 1, True)
        display.show()
        display.rect(position.x, position.y, size.x, size.y, 0, True)
        print(position)
        

