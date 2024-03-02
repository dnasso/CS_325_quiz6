from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return (3.1415 * (self.radius ** 2))

class square(shape):
    def __init__(self, length):
        self.length = length
    def get_area(self):
        return (self.length * self.length)

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def get_area(self):
        return (self.length * self.width)
    
def demo():
    test = circle(5)
    print(test.get_area())
    test = square(5)
    print(test.get_area())
    test = rectangle(5, 10)
    print(test.get_area())

if __name__ == "__main__":
    demo()