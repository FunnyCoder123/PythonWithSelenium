def add_extra_security(func):
    def wrapper():
        print("Before Starting a Test")
        print("Start the Test")
        func()
        print("After complition of a Test")
        print("Close the browser")
    return wrapper()
@add_extra_security
def test_ui():
    print("Hello Jabeer")




@add_extra_security
def drive_scooty():
    print("This is my normal function!!")
    print("I am driving Fz!!")
