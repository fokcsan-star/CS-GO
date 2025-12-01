import math

class Shape:
    def area(self): 
        print("Area: 0 (base shape)")
        return 0
    
    def perimeter(self): 
        print("Perimeter: 0 (base shape)")
        return 0

class Circle(Shape):
    def __init__(self, r): 
        self.r = r
        print(f"Circle created with radius: {r}")
    
    def area(self):
        result = math.pi * self.r ** 2
        print(f"Circle area: π * {self.r}² = {result:.2f}")
        return result
    
    def perimeter(self):
        result = 2 * math.pi * self.r
        print(f"Circle perimeter: 2 * π * {self.r} = {result:.2f}")
        return result

class Triangle(Shape):
    def __init__(self, a, b, c): 
        self.a = a
        self.b = b
        self.c = c
        print(f"Triangle created with sides: {a}, {b}, {c}")
    
    def area(self):
        p = self.perimeter() / 2
        result = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print(f"Triangle area (Heron): sqrt({p:.1f}*{p-self.a:.1f}*{p-self.b:.1f}*{p-self.c:.1f}) = {result:.2f}")
        return result
    
    def perimeter(self):
        result = self.a + self.b + self.c
        print(f"Triangle perimeter: {self.a} + {self.b} + {self.c} = {result}")
        return result



print("=== SHAPE DEMO ===")
shape = Shape()
shape.area()
shape.perimeter()
print()

circle = Circle(5)
circle.area()
circle.perimeter()
print()

triangle = Triangle(3, 4, 5)
triangle.perimeter()
triangle.area()
print()