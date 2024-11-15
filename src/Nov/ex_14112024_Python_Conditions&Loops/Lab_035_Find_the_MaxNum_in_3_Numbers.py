# to find the max in 3 numbers
model = int(input("Please Enter Your car Model\n"))
if model < 2015:
    print("You have only one year to Renewel")
elif model == 2016:
    print("No need of Renewal")
elif model > 2017:
    print("Wait one more Year to renewal")
else:
    print("Thanks for the confirmation")
