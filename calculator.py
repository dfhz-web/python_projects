def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    while x == 0:
        print("Invalid input, please enter a number other than 0")
        x = int(input("Enter first number: "))
    while y == 0:
        print("Invalid input, please enter a number other than 0")
        y = int(input("Enter second number: "))

    return x / y

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        while True:
            try:
                num1 = int(input("Enter first number: "))
                break
            except ValueError:
                print("Invalid input, please enter numeric values.")
        
        while True:
            try:
                num2 = int(input("Enter second number: "))
                break
            except ValueError:
                print("Invalid input, please enter numeric values.")
        
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            break

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        next_calculation = input("Do you want to continue calculation (yes/no): ")
        if next_calculation == "no":
          print("Exiting the calculator")
          break

    else:
        print("Invalid input")