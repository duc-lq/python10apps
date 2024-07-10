from random import randint

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def falls_in_rectangle(self, rectangle):
        return (rectangle.point1.x < self.x < rectangle.point2.x \
            and rectangle.point1.y < self.y < rectangle.point2.y)
    
    def point_info(self):
        return "[{0},{1}]".format(self.x, self.y)


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def rectangle_info(self):
        return "Rectangle ({0} and {1})".format(self.point1.point_info(), self.point2.point_info())
    

# Create rectangle
p1 = Point(randint(0,9), randint(0, 9))
p2 = Point(randint(0,9), randint(0, 9))
r = Rectangle(p1, p2)

print(r.rectangle_info())