class Square:
    def __init__(self,l):
        self.length = l
    def square_area(self):
        return self.length*self.length
newSquare = Square(10)
print("Area of Square:", newSquare.square_area())