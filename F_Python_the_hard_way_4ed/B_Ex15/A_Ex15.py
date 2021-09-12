from sys import argv

filename = argv[1]

with open(filename, mode="r") as file:
    print(f"Opening {file.name}")
    text = file.read()
    print(text)
