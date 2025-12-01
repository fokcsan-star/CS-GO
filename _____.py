import math

class Shape:
    def area(self): return 0
    def perimeter(self): return 0

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r ** 2
    def perimeter(self): return 2 * math.pi * self.r

class Triangle(Shape):
    def __init__(self, a, b, c): 
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    def perimeter(self): return self.a + self.b + self.c
