def add(x, y) :
    return x+y
    
def subtract(x,y) :
    return x-y

def multiply(x,y) :
    return x*y

def divide(x,y) :
    if y == 0:
       return "cannot divide by zero"
    else :
       return x/y


operation_dict = {
    'add' : add,
    'subtract' : subtract,
    'divide' : divide,
    'multiply' : multiply
    
}

def main():
    #infinite loop until the user enters halt to stop the programm
    while True :
        print("OPTIONS:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'halt' to stop the program")

        userInput = input(": ")
        if userInput == "halt":
            break
        elif userInput in operation_dict:
            num1 = float(input("Enter the first number "))
            num2 = float(input("Enter the second number "))
            operation = operation_dict[userInput]
            result = operation(num1, num2)
            print("Result: ", result)
        else:
            print("Invalid input")
        
if __name__ == '__main__' :
    #calling the main function to start the program
    main()