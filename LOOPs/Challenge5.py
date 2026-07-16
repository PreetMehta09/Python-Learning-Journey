attempt = 3

password = "python123"

i = 1

while i<=attempt:
    n = input("Enter the password: ")
    if n==password:
        print("correct password")
        break
    else:
        print("Wrong password")
        i+=1
        if i == attempt+1:
            print("Account Locked")
            break

