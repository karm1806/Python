r=int(input("Enter the Radius of Circle: "))
class Circle:
    def __init__(self,r):
        self.radius = r
    def circle_area(self):
        return 3.14*self.radius
newCircle = Circle(r*r)
print("Area of Circle:", newCircle.circle_area())
c=int(input("Enter the Radius of Circle: "))
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        return 2 * 3.14 * self.radius
my_circle = Circle(c)
result = my_circle.perimeter()
print(f"Perimeter of Circle: : {round(result, 2)}")