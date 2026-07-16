SN = 7

while True:
    guess = int(input("Guess the number: "))
    if guess == SN:
        print("Congratulations 🎉")
        break
    else:
        print("Wrong Guess")