
## As long as the get_area() functions are passed the same arguments, then the design adheres to LSP
class Shape:
    def get_area(self):
        print("<Not implemented!>")

class hasBaseAndLength:
    def set_width(self):
        print("<Not implemented!>")
    def set_length(self):
        print("<Not implemented!>")

class hasHeightAndWidth:
    def set_base(self):
        print("<Not implemented!>")
    def set_width(self):
        print("<Not implemented!>")

class Circle(Shape, hasHeightAndWidth):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return (3.1415 * ((self.width / 2) ** 2))
    
class Rectangle(Shape, hasHeightAndWidth):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return (self.height * self.width)
    
class Triangle(Shape, hasBaseAndLength):
    def __init__(self, base, height):
        self.base = base
        self.length = height
    def set_base(self, base):
        self.base = base
    def set_length(self, length):
        self.length = length
    def get_area(self):
        return (self.base * self.length * .5)

def printArea(shape):
    if isinstance(shape, hasBaseAndLength):
        shape.set_base(5)
        shape.set_length(5)
    elif isinstance(shape, hasHeightAndWidth):
        shape.set_height(5)
        shape.set_width(5)  
    else:
        print("This shape is undefined.")
    print(shape.get_area())

### If we wanted to add another type of shape, we could add 
### another base class for its properties, and add another 
### elif to our printFunction to check for it. At the very 
### least, provided the object is set, we know that the 
### get_area() call at the end works.
    
def demo():
    test = Circle(10,10)
    printArea(test)
    test = Triangle(10,10)
    printArea(test)
    test = Rectangle(5, 10)
    printArea(test)

if __name__ == "__main__":
    demo()