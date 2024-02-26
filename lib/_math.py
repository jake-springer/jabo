import math

class Vector2D():
    x: int
    y: int
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
        
    def __add__(self, vec):
        return Vector2D(self.x + vec.x, self.y + vec.y)
    
    def __sub__(self, vec):
        return Vector2D(self.x - vec.x, self.y - vec.y)
    
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)
    
    def __neg__(self):
        return Vector2D(-self.x, -self.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            return Vector2D(self.x / mag, self.y / mag)
        else:
            return Vector2D()
    
    def dot_product(self, vec):
        return self.x * vec.x + self.y * vec.y
    
    def angle_between(self, vec):
        dot = self.dot_product(vec)
        mag_self = self.magnitude()
        mag_vec = vec.magnitude()
        if mag_self != 0 and mag_vec != 0:
            cos_theta = dot / (mag_self * mag_vec)
            return math.acos(cos_theta)
        else:
            return 0  # Return 0 if one of the vectors has zero magnitude
    
    def project_onto(self, vec):
        mag_vec = vec.magnitude()
        if mag_vec != 0:
            scalar_projection = self.dot_product(vec) / mag_vec
            return vec.normalize() * scalar_projection
        else:
            return Vector2D()  # Return a zero vector if the given vector has zero magnitude
