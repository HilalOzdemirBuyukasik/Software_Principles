
# Open Closed Principle

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

#The calculator works without needing any changes.
class AreaCalculator:
    def calculate(self, shape: Shape):
        return shape.area()

if __name__ == '__main__':
    circle = Circle(radius=5)
    square = Square(side=4)

    calculator = AreaCalculator()

    print(f'Circle Area: ', calculator.calculate(circle))
    print(f'Square Area: ', calculator.calculate(square))