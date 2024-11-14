"""
find the area of the circle by taking the radious as input and
the formula to be used is area=Pi x r^2
"""
import math
radius = float(input("Please do enter the Radious\n"))
area = 3.14 * (radius ** 2)
print(f"area of the circle is {area: .2f}")
print("Area of the circle is", area)
area2 = math.pi  * math.pow(radius, 10)
print(area2)

