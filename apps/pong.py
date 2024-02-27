# import sys
# sys.path.append("../utils")
from ..lib._math import Vector2D
from system.display import Display
from lib.game_lib import GameObject
from lib.input_handler import input_handler
import pygame

dimension = Vector2D(128, 64)

player1 = GameObject(Vector2D(0, 0), Vector2D(30, 5))
speed = 4
player2 = GameObject(Vector2D(123, 0), Vector2D(30, 5))

game_running = True
input: input_handler
display: Display
pg = pygame.init()
screen = pygame.display.set_mode((128, 64))

def start_game(_input: input_handler):
    input = _input
    display = Display()
    while game_running:
        screen.fill((255, 255, 255))
        tick()
        pg.display.flip()
 

# Coded this fucken function on my phone
def tick():
    input.tick()
    player1.display(screen) # flip to display for jabo
    player2.display(screen)
    
       
        
#Important to note increasing Y value is down    
def move():
    if(input.up):
        player1.position.y -= speed
    if(input.down):
        player1.position.y += speed