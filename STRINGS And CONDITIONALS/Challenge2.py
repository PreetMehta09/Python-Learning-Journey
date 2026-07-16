a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
c = int(input("Enter your Third number : "))

if(a>b and a>c):
    print(a,"is the largest")
elif(b>c):
    print(b,"is the largest")
else: 
    print(c,"is the largest")