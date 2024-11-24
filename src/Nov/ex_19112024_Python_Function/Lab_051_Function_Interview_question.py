'''
Create a program to sum 3 numbers with user input,
if user not given any number use default as 100, 200, 300
'''

num1 = int(input("Enter the number 1 \n"))
num2 = int(input("Enter the number 2 \n"))
num3 = int(input("Enter the number 3 \n"))
def sum_of_three_numbers(n1=100, n2=200, n3=300):
    return n1+n2+n3
result = sum_of_three_numbers(num1,num2,num3)
print(result)

result2 = sum_of_three_numbers()
print(result2)
