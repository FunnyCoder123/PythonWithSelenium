'''
Write a program that classifies a triangle based on its side lengths.
 Given three input values representing the lengths of the sides,
  determine if the triangle is equilateral (all sides are equal),
   isosceles (exactly two sides are equal),
    or scalene (no sides are equal).
 Use an if-else statement to classify the triangle.
'''

side1 = int(input("Please Enter The Side1 Value= \n"))
side2 = int(input("Please Enter The Side2 Value= \n"))
side3 = int(input("Please Enter The Side3 Value= \n"))

if side1 == side2 == side3:
    print("Its a Equilateral Triangle")
elif side1 == side2 and side3:
    print("Its a Isosceles Triangle")
elif side1 < side2 and side3:
    print("Its a Scalene Triangle")
else: print("Its a Scalene Triangle")