def sum_of_two(a, b):
    return a+b
result = sum_of_two(4, 6)
print(result)

def sum_of_two_with_default(num1 = 100, num2 =200):
    print("I will sum the two numbers!")
    return num1 + num2
result = sum_of_two_with_default(num1=32, num2=23)
print(result)
result= sum_of_two_with_default()
print(result)
