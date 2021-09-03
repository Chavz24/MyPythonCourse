"""Review Exercises 17.2"""

import csv
import numpy as np
from pathlib import Path
from matplotlib import pyplot

# It is a well-documented fact that the number of pirates in the world
# is correlated with a rise in global temperatures. Write a script
# pirates.py that visually examines this relationship

path_to_file = Path(
    "F:/A_Practicas_python/A_Python_basics_4ed/python-basics-exercises-master/"
    "ch17-scientific-computing-and-graphing/practice_files/pirates.csv")

# Read in the file pirates.csv from the Chapter 17 practice files
# folder.

with path_to_file.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)

    #  Create a line graph of the average world temperature in degrees
    # Celsius as a function of the number of pirates in the world—
    # that is, graph Pirates along the x-axis and Temperature along
    # the y-axis.
    x_pirates = []
    y_temp = []
    year_label = []

    for row in reader:
        try:
            x_pirates.append(int(row[2]))
            y_temp.append(float(row[1]))
            year_label.append(row[0])
        except ValueError:
            continue


    pyplot.plot(x_pirates, y_temp, "m-o")
    pyplot.ylabel("Average temp in degrees Celcius.")
    pyplot.xlabel("Number of pirates in the world.")
    pyplot.xticks([0, 10000, 20000, 30000, 40000, 50000, 60000])
    pyplot.title("Correlation of number of pirates i the world and global temperature.")
    count = 0
    for x, y in zip(x_pirates, y_temp):
        label = year_label[count]
        pyplot.annotate(label, (x, y))
        count += 1

    pyplot.savefig("D_temp_pirates")
    pyplot.show()
