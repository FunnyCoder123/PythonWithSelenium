# write a program to find the grade
# Instructions are 90 - 100 -> A
# 70-89-> B
score = int(input("Enter Your Score Here\n"))
if score >= 90 and score <= 100:
    print("Your grade is", "A")
elif score >= 70 and score <=89:
    print("Grade B")
elif score >=45 and score <= 69:
    print("Grade C")
elif score >=0 and score <= 44:
    print("Failed")
else:
    print("You are a superman!")