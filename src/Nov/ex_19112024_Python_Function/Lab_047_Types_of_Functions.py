"""
User Defined functions are 4 types
1. they can't return -> non return
2. They can return something
3. They have Parameters
4. They Dont have Parameters
"""


# 1. they can't return -> non return
# Nothing is there in ()
def greet():
    print("Hello")

greet()

# 2. They can No return type and with argument

def say_hello_default_arg(name = "Jabeer"):
    print("Hello", name.upper())

say_hello_default_arg()
say_hello_default_arg("Basha")


def multiple_arguments(name = "Jabeer", Lastname = "Shaik"):
    print("Jabee")
multiple_arguments()

