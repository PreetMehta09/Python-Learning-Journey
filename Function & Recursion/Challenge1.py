while True:
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    choice=int(input("Enter your choice: "))

    if choice == 1:
        def num_add(a,b):
            sum = a + b
            print("The sum is:", sum)
        num_add(int(input("Enter first number: ")), int(input("Enter second number: ")))
    elif choice == 2:
        def num_subtract(a,b):
            difference = a - b
            print("The difference is:", difference)
        num_subtract(int(input("Enter first number: ")), int(input("Enter second number: ")))
    elif choice == 3:
        def num_multiply(a,b):
            product = a * b
            print("The product is:", product)
        num_multiply(int(input("Enter first number: ")), int(input("Enter second number: ")))
    elif choice == 4:
        def num_divide(a,b):
            if b == 0:
                print("Error: Division by zero is not allowed.")
            else:
                quotient = a / b
                print("The quotient is:", quotient)
        num_divide(int(input("Enter first number: ")), int(input("Enter second number: ")))
    elif choice == 5:
        print("Exiting the calculator. Goodbye!")
        break
    
    