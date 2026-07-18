while True:
    name = input("Enter your name: ")
    marks = input("Enter your marks: ")
    with open("students.txt", "a") as file:
        file.write("Name: " + name + ", Marks: " + marks + "\n")
        with open("students.txt", "r") as file:
            data = file.read()
            print(data)