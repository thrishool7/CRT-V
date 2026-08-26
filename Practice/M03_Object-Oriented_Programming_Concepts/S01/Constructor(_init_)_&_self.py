
class circle:
    
    count = 0
    def __init__(self,radius):
        self.radius = radius
        

    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius

c1 = circle(7)
c2 = circle(5)
c3 = circle(3)
print(c1.area())
print(c1.perimeter())
print(c2.area())
print(c2.perimeter())
print(c3.area())
print(c3.perimeter())


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small


    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
        if carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
        if carType == 3:
            if self.small > 0:
                self.small -= 1
                return True
        return False
        
