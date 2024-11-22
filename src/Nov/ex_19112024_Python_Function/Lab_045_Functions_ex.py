from src.Nov.ex_19112024_Python_Function.Lab_044_Functions import greet


def first_part_last_name():
    pass
def greet_to_all_of_you():
    print("Hello Every one")
def greet1():
    print("Jabeer")

greet()   #It has been taken from last page
first_part_last_name()
greet_to_all_of_you()
greet1()

"""
User defined functions are 2 types
1. with argument
2. Without argument
"""

def say_hello():
    print('Hello')

say_hello()

# function with argument, Parameter

def greet_by_name(name):
    print("Hello", name)
    print(f"hello, {name}")

greet_by_name("jabeer")