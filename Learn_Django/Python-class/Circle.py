
class Circle():
    
    pi = 3.14
    
    def __init__(self,radius=1):
        self.radius = radius
        

    def area(self):
        return self.pi * self.radius**2
    
    def perimeter(self):
        return self.pi * self.radius * 2
    
    
    def __str__(self):
        
        return f"Radius: {self.radius}, Area: {self.area()}, Perimeter: {self.perimeter()}."
    

c = Circle(4)

print(c)
        