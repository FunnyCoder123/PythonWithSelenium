# Match Statement is similar to Switch in Java
# Match the OP and execute
# It is applicable in Python > 3.10
# Syntax: match ***: case***:
#  Write A program to ask the user which browser he want to run the Automation
browser_name = input("Enter The Browser Name\n")
match browser_name:
    case "Chrome":
        print("Starting the Chrome!!!")
    case "Mozilla":
        print("Starting the Mozilla")
    case "safari":
        print("Starting the Safari")
    case _: #_ used as defult. if the value dosent match it will print the statement of below
        print("Browser Not found")
