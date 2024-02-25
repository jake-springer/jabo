# import sys
# sys.path.append("../utils")
from ..lib._math import Vector2D
from ..sys.display import Display
from ..lib.game_lib import GameObject
from ..lib.input_handler import input_handler

dimension = Vector2D(128, 64)

player1 = GameObject(Vector2D(0, 0), Vector2D(30, 5))
speed = 4
player2 = GameObject(Vector2D(123, 0), Vector2D(30, 5))

game_running = True
input: input_handler

def start_game(_input: input_handler):
    input = _input
    display = Display()
    while game_running:
        tick()
 

# Coded this fucken function on my phone
def tick():
    input.tick()
    player1.display(display)
    player2.display(display)
    
       
        
#Important to note increasing Y value is down    
def move():
    if(input.up):
        player1.position.y -= speed
    if(input.down):
        player1.position.y += speed