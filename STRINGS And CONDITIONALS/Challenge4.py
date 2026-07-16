marks = int(input("Enter your marks : "))
 
if (marks >= 90):
    print("Grade A")
elif(marks >= 75 and marks < 90):
    print("Grade B")
elif(marks >= 60 and marks < 74):
    print("Grade C")
else:
    print("FAIL")