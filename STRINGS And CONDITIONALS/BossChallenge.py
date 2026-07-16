balence = int(input("Enter your balence : "))
amount = int(input("Enter amount you want to withdraw : "))

if (amount >= balence):
    print("Insufficient Balence")
else:
    print("Transaction Succesfull")
    print("Remaining Balence =", balence-amount)
    
    