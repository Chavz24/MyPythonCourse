from sys import argv

filename = argv[1]

print(f"You are abut to erase {filename}")
print("Press CTRL + C if you want to abort")
print("Press Enter or Return if you want to continue")
input("?")

with open(filename, mode="w") as file:
    print("Write 3 lines in the file")
    line1 = input("line 1: ")
    line2 = input("line 2: ")
    line3 = input("line 3: ")
    print("Erasing file...")
    print("Done")
    print("Writing lines into the file...")
    content=f"{line1}\n{line2}\n{line3}"
    file.write(content)
    print("Done.")

