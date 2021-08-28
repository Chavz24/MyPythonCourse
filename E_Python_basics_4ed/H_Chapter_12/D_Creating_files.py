"""Review Exercises 12.5"""

from pathlib import Path

# Write the following text to file called starships.txt in your home directory:
# Discovery,Enterprise, Defiant, Voyage

ships = ['Discovery\n', 'Enterprise\n', 'Defiant\n', 'Voyage\n']

file_path = Path.cwd() / 'DD_starships.txt'

with file_path.open(mode='w', encoding='utf-8') as file:
    file.writelines(ships)

# Read the file starhips.txt you created in Exercise 1 and print each
# line of text in the file. The output should not have extra blank lines
# between each word.

# with file_path.open(mode='r', encoding='utf-8') as file:
#     pass
#     #print(file.read())

# Read the file startships.txt and print the names of the starships
# that start with the letter D.

with file_path.open(mode='r', encoding='utf-8') as file:
    for line in file:
        if line.startswith('D'):
            print(line, end='')
