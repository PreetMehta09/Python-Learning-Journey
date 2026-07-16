Balance = 5000

while True:
    print("Welcome to Mini ATM")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    n = int(input("Enter your choice: "))

    if n == 1:
        print("Your balance is:", Balance)
        continue
    elif n ==2:
        amount = int(input("Enter the amount to withdraw: "))
        if amount>Balance:
            print("Insufficient Balance")
        else: 
            Balance -= amount
            print("Withdrawal successful. Your new balance is:", Balance)
    elif n == 3:
        amount = int(input("Enter the amount to deposit: "))
        Balance += amount
        print("Deposit successful. Your new balance is:", Balance)
    elif n == 4:
        print("Thank you for using Mini ATM.")
        break
    else:
        print("Invalid choice. Please try again.")
