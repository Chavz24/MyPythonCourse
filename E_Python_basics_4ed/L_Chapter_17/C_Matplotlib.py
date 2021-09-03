import numpy as np
from matplotlib import pyplot

xs = [1, 2, 3, 4, 5]
ys = [4, 6, 8, 0, 1]
# pyplot.plot(xs,ys,'m:|')
# pyplot.show()

# using numpy to create the plot data

matrix = np.arange(1, 6)

# pyplot.plot(matrix)
# pyplot.show()

# multi-dimensional arrays

data = np.arange(1, 21).reshape(5, 4)

# pyplot.plot(data,'--o')
# pyplot.show()

# pyplot.plot(data.transpose(),'--o')
# pyplot.show()

# Practice exercise

# python learned in real_python vs other sites in 20 days

days = np.arange(21)
other_sites = np.arange(21)
real_python = other_sites ** 2

# pyplot.plot(days, other_sites, "m--o", days, real_python, 'r--D')
# pyplot.xticks([0, 5, 10, 15, 20])
# pyplot.ylabel("Amount Python Learned")
# pyplot.xlabel("Days Learning Python")
# pyplot.title("Python learned in real_python vs other sites")
# pyplot.legend(["other sites".capitalize(), "real python".capitalize()])
# pyplot.savefig("CC_learned.png")
# pyplot.show()

# other types of plots

fruits = {
    "apples": 10,
    "oranges": 16,
    "bananas": 9,
    "pears": 4,
}

pyplot.bar(fruits.keys(), fruits.values())
pyplot.show()
