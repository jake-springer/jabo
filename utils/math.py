

class Vector2D():
    x: float
    y: float
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def __add__(self, vec):
        return Vector2D(self.x + vec.x, self.y + vec.y)
    
    def __subtract__(self, vec):
        return Vector2D(self.x - vec.x, self.y - vec.y)
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
