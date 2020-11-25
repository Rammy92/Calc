# assignment 1 python

def addition (x, y):
    return x + y

def subtraction (x, y):
    return x - y

def multiplication (x, y):
    return x * y

def division (x, y):
    return x / y
while True:

    x = int(input("Hello! Please inter a number \n "))

    y = int(input("Please inter another number \n "))

    print("""
    Inter 1 for addition
    Inter 2 for subtraction 
    Inter 3 for multiplication
    Inter 4 for division
    """  
    )

    operator = input()

    if operator == "1":
        result = addition(x, y)
        print("The result is ", result ,"\n")
        
        

    if operator == "2":
        result = subtraction(x, y)
        print("The result is ", result ,"\n")
        

    if operator == "3":
        result = multiplication(x, y)
        print("The result is ", result ,"\n")
        

    if operator == "4":
        result = division(x, y)
        print("The result is ", result ,"\n")

    elif result < 50:
            print("Less than fifty\n")
    elif result == 50:
            print("Fifty\n")
    elif result < 100:   
            print("Almost a hundred\n")
    elif result == 100:
            print("Spot on!")
    elif result > 100:
            print("Missed the spot\n")

    user_choice = input("Do you want to continue?Y/n\n")
    if user_choice == "Y":
        continue
    else:
        print("Exit!")
        break




