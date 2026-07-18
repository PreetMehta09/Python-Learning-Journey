with open("notes.txt", "r") as file:
        content = file.read()
        characters = len(content)
        words = len(content.split())
        lines = len(content.splitlines())
        print("File Statistics:")
        print("Number of words:", words)
        print("Number of lines:", lines)
        print("Number of characters:", characters)

