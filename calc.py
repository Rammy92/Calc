def addition (x, y):
    result = x + y
    return result

def subtraction (x, y):
    result = x - y
    return result

def multiplication (x, y):
    result = x * y
    return result

def division (x, y):
    result = x / y
    return result
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

    if result < 50:
        print("Less than fifty")
    elif result == 50:
        print("Fifty")
    elif result < 100:   
        print("Almost a hundred")
    elif result == 100:
        print("Spot on!")
      elif result > 100:
            print("Missed the spot")

    user_choice = input("Do you want to continue?Y/n\n")
    if user_choice == "Y":
        continue
    else:
        print("Exit")
        break




