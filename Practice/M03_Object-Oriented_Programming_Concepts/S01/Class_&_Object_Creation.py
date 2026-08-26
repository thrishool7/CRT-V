'''class Example:
    x = 100
    def display(self):
        print("This is an example class.")
obj = Example()
obj.display()
print(obj.x)'''

class circle:
    radius = 7
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius

c = circle()
print(c.area())
print(c.perimeter())