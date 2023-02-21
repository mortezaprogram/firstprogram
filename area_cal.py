
import math
def rect_area(h,a):
    area = a*h
    return area
def sq_area(r):
    area=math.pi*(math.pow(r,2))
    return area
def area_cal(shape):
    shape=shape.lower()
    if (shape=="rect"):
        h=float(input("Please input H: "))
        a = float(input("Please input A: "))
        area=rect_area(h,a)
        return area
    elif (shape=="circle"):
        r=float(input("Please input radius: "))
        area=sq_area(r)
        return area
    else:
        return "Please inter rect or circle"

print("The area is {:.3f}".format(area_cal(input("Please input your shape: "))))
