def palindrome(s):
    if len(s) <= 1:
        print("The word is small")
    else:
        if s == s[::-1]:
            print("The word is a palindrome")
        else:
            print("The word is not a palindrome")

palindrome(input("Enter a word to check if it is a palindrome: "))
