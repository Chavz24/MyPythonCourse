from sys import argv
from os.path import exists

from_file = argv[1]
to_file = argv[-1]

print(f"Copying from {from_file} to file {to_file}...")
print(f"Output file exist? {exists(to_file)}")

with open(from_file, mode="r") as input_file, open(to_file, mode="w") as output_file:
    text = input_file.read()
    print(f"The input file is {len(text)} bytes long.")

    output_file.write(text)

print("Done.")
