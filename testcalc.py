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
    Inter + for addition
    Inter - for subtraction 
    Inter * for multiplication
    Inter / for division
    """  
    )

    operator = input()

    if operator == "+":
        print("The result is ", addition(x, y) ,"\n")
        

    elif operator == "-":
        print("The result is ", subtraction(x, y) ,"\n")
        

    elif operator == "*":
        print("The result is ", multiplication(x, y) ,"\n")
        

    elif operator == "/":
        print("The result is ", division(x, y) ,"\n")
        

    user_choice = input("Do you want to continue?Y/n\n")
    if user_choice == "Y":
        continue
    else:
        print("Exit")
        break




