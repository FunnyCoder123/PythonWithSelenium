"""
Create a program that determines whether a given year is a leap year.
 A leap year is divisible by 4,
  but not by 100 unless it is also divisible by 400.
   Use an if-else statement to make this determination.
"""

Year = int(input("Please Enter the Year in YYYY format\n"))
if (Year % 100 != 0 and Year % 4 ==0) or (Year % 400 == 0):
    print("Its a Leap Year")
else:
    print("Its Not a Leap Year")
