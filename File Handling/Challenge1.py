while True:
    print("1.Add Notes")
    print("2.View Notes")
    print("3.Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        note = input("Enter your note: ")
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        print("Note added successfully!")
    elif choice == '2':
            with open("notes.txt", "r") as file:
                notes = file.readlines()
                if notes:
                    print("Your Notes:")
                    for idx, note in enumerate(notes, start=1):
                        print(f"{idx}. {note.strip()}")
                else:
                    print("No notes found.")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")