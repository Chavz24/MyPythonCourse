"""Review Exercises 12.6"""

from pathlib import Path
import csv

# Write a script that writes the following list of lists to a file called
# numbers.csv in your home directory.

nums = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

file_path = Path.cwd() / 'HH_Numbers.csv'

with file_path.open(mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(nums)

# Write a script that reads the numbers in the numbers.csv file from
# Exercise 1 into a list of lists of integers called numbers. Print the list
# of lists.

with file_path.open(mode='r', encoding='utf-8', newline='') as file:
    reader = csv.reader(file)
    nums2 = []
    for row in reader:
        num_row = [int(value) for value in row]
        nums2.append(num_row)
    print(nums2)

# Write a script that writes the following list of dictionaries to a file
# called favorite_colors.csv in your home directory

file_path2 = Path.cwd() / 'HH_Favorite_colors.csv'

favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
]

with file_path2.open(mode='w', encoding='utf-8', newline='') as file:
    writer=csv.DictWriter(file,fieldnames=favorite_colors[0].keys())
    writer.writeheader()
    writer.writerows(favorite_colors)

# Write a script that reads the data from the favorite_colors.csv file
# from Exercise 3 into a list of dictionaries called favorite_colors.

with file_path2.open(mode='r',encoding='utf-8',newline='') as file:
    reader=csv.DictReader(file)
    favorite_colors2=[]
    for row in reader:
        favorite_colors2.append(dict(row))

    print(favorite_colors2)

