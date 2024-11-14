# # # Ternary Operator : if-else statement


user_input = int(input("Please Enter Your Age\n"))
if user_input > 18:
    print("Yes, You are Eligible to Vote")
else:
    print("Not Eligible to Vote")
print(int(input("Please do enter your age\n")), )

print("Yes You can Vote" if int(input("Please do enter the age\n")) > 18 else "No You can't Vote")
print("You can watch this movie" if int(input("Please Enter your age\n")) == 15 else "You are Not Eligible")