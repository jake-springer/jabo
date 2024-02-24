# import sys
# sys.path.append("../utils")
from lib._math import Vector2D
from system.display import Display
from lib.game_lib import GameObject

player1 = GameObject(Vector2D(0, 0), Vector2D(30, 5))
player2 = GameObject(Vector2D(123, 0), Vector2D(30, 5))

game_running = True

def start_game():
    display = Display()
    while game_running:
        player1.display(display)
        player2.display(display)

start_game()