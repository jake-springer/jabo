from display import Display
from machine import Pin
from random import randint

dim = [127, 63]
speed = [3, -3]
size = 10
position = [0, 0]
display = Display()
#x, y, color


while (True):
    position[0] += speed[0]
    position[1] += speed[1]

    if(speed[0] == 0): speed[0] = 1
    if(speed[1] == 0): speed[0] = 1

    if(position[0] > dim[0]-size):
        position[0] = dim[0]-size
        speed[0] = -randint(speed[0]-1, speed[0]+1)
        
    if(position[0] < size):
        position[0] = size
        speed[0] = -randint(speed[0]-1, speed[0]+1)

    if(position[1] > dim[1]-size):
        position[1] = dim[1]-size
        speed[1] = -randint(speed[1]-1, speed[1]+1)

    if(position[1] < size):
        position[1] = size
        speed[1] = -randint(speed[1]-1, speed[1]+1)

    display.rect(position[0], position[1], size, size, 1, True)
    display.show()
    display.rect(position[0], position[1], size, size, 0, True)
    print(position)
    

