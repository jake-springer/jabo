# import sys
# sys.path.append("../utils")


class Pong:
    def __init__(self):
        from lib._math import Vector2D
        from system.display import Display
        from lib.game_lib import GameObject
        
        self.display = Display()
        self.player1 = GameObject(Vector2D(0, 0), Vector2D(30, 5))
        self.player2 = GameObject(Vector2D(123, 0), Vector2D(30, 5))

        self.game_running = True


    def run(self):
        while self.game_running:
            self.player1.display(self.display)
            self.player2.display(self.display)
