from display import Display
from machine import Pin
from random import randint
from time import sleep

dim = [128, 64]
speed = [3, -3]
size = [10, 5]
position = [0, 0]
display = Display()
#x, y, color


while (True):
    position[0] += speed[0]
    position[1] += speed[1]

    if(position[0] > dim[0]-size[0]):
        position[0] = dim[0]-size[0]
        speed[0] *= -1
        
    if(position[0] < 0):
        position[0] = 0
        speed[0] *= -1

    if(position[1] > dim[1]-size[1]):
        position[1] = dim[1]-size[1]
        speed[1] *= -1

    if(position[1] < 0):
        position[1] = 0
        speed[1] *= -1

    display.rect(position[0], position[1], size[0], size[1], 1, True)
    display.show()
    display.rect(position[0], position[1], size[0], size[1], 0, True)
    print(position)
    

