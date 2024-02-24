from display import Display
from machine import Pin
from random import randint

dim = [128, 64]
speed = [3, -3]
position = [0, 0]
display = Display()
#x, y, color


while (True):
    position[0] += speed[0]
    position[1] += speed[1]

    if(position[0] > 128):
        position[0] = 128
        speed[0] = -randint(speed[0]-1, speed[0]+1)
        
    if(position[0] < 0):
        position[0] = 0
        speed[0] = -randint(speed[0]-1, speed[0]+1)

    if(position[1] > 64 or position[1] < 1):
        position[1] = 64
        speed[1] = -randint(speed[1]-1, speed[1]+1)

    if(position[1] < 0):
        position[1] = 0
        speed[1] = -randint(speed[1]-1, speed[1]+1)

    display.pixel(position[0], position[1], 1)
    display.show()
    display.pixel(position[0], position[1], 0)
    print(position)
    

