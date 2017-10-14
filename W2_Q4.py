from math import sqrt

#Naming coordinate
class Coordinate:
    x = 0
    y = 0

#function definning
def area_of_triangle(p1,p2,p3):
    side1 = sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
    side2 = sqrt((p1.x - p3.x) ** 2 + (p1.y - p3.y) ** 2)
    side3 = sqrt((p2.x - p3.x) ** 2 + (p2.y - p3.y) ** 2)
    s = (side1 + side2 + side3) / 2.0
    area = sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area

#input
c1 = Coordinate()    
c1.x = float(raw_input("Enter x coordinate of the first point of a triangle:"))
c1.y = float(raw_input("Enter y coordinate of the first point of a triangle:"))
c2 = Coordinate()    
c2.x = float(raw_input("Enter x coordinate of the second point of a triangle:"))
c2.y = float(raw_input("Enter y coordinate of the second point of a triangle:"))
c3 = Coordinate()    
c3.x = float(raw_input("Enter x coordinate of the third point of a triangle:"))
c3.y = float(raw_input("Enter y coordinate of the thid point of a triangle:"))

print area_of_triangle(c1,c2,c3)