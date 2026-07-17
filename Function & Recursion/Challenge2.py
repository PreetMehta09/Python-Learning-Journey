def num_fact(n):
    if n== 0 or n == 1:
        return 1
    else:
        return n * num_fact(n-1)
print("The factorial is:", num_fact(int(input("Enter a number to find its factorial: "))))