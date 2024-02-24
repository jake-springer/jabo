# import sys
# sys.path.append("../utils")
from ..lib._math import Vector2D
from ..sys.display import Display
from ..lib.game_lib import GameObject
from ..lib.input_handler import input_handler

dimension = Vector2D(128, 64)

player1 = GameObject(Vector2D(0, 0), Vector2D(30, 5))
player2 = GameObject(Vector2D(123, 0), Vector2D(30, 5))

game_running = True

def start_game(input: input_handler):
    display = Display()
    while game_running:
        player1.display(display)
        player2.display(display)
        
        
