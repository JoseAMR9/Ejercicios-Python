class Rectangle:
    def __init__(self, width, height):
        self.base = width
        self.height = height
    
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.base)
    

rec1 = Rectangle(10,10)

print(f"Area: {rec1.area()}")
print(f"Perimeter: {rec1.perimeter()}")