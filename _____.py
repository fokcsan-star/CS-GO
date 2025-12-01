class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print(f"Rectangle created: {width}x{height}")
    
    def area(self):
        result = self.width * self.height
        print(f"Area: {self.width} * {self.height} = {result}")
        return result
    
    def perimeter(self):
        result = 2 * (self.width + self.height)
        print(f"Perimeter: 2 * ({self.width} + {self.height}) = {result}")
        return result



r = Rectangle(5, 3)
r.area()
r.perimeter()
print()