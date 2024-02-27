from lib._math import Vector2D
import pygame

class GameObject():
        position: Vector2D
        size: Vector2D
        
        def __init__(self, position: Vector2D, size: Vector2D):
            self.position = position
            self.size = size

        def display(self, display):
            if(type(display) == type(pygame)):
                rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
                pygame.draw.rect(display, (255, 255, 255), rect)
                return
            
            display.rect(self.position.x, self.position.y, self.size.x, self.size.y, 1, True)
            display.show()
            display.rect(self.position.x, self.position.y, self.size.x, self.size.y, 0, True)
            
        def is_colliding(self, other: 'GameObject'):
            # Check for collision in each dimension
            collision_x = (self.position.x < other.position.x + other.size.x) and (self.position.x + self.size.x > other.position.x)
            collision_y = (self.position.y < other.position.y + other.size.y) and (self.position.y + self.size.y > other.position.y)
            
            # Return True if there is a collision in both dimensions
            return collision_x and collision_y