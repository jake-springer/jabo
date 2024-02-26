from lib._math import Vector2D


class GameObject():
        position: Vector2D
        size: Vector2D
        
        def __init__(self, position: Vector2D, size: Vector2D):
            self.position = position
            self.size = size

        def display(self, display):
            display.rect(self.position.x, self.position.y, self.size.x, self.size.y, 1, True)
            display.show()
            display.rect(self.position.x, self.position.y, self.size.x, self.size.y, 0, True)