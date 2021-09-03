"""Review Exercises 17.1"""

import numpy as np

# Create a 3 × 3 NumPy array named first_matrix that includes the
# numbers 3 through 11 by using np.arange() and np.reshape().

first_matrix = np.arange(3, 12).reshape([3, 3])

# Display the minimum, maximum and mean of all entries in first_-
# matrix.
# print(first_matrix.min())
# print(first_matrix.max())
# print(first_matrix.mean())

# Square every entry in first_matrix using the ** operator, and save
# the results in an array named second_matrix

second_matrix = first_matrix ** 2

# Use np.vstack() to stack first_matrix on top of second_matrix and
# save the results in an array named third_matrix.

third_matrix = np.vstack([first_matrix, second_matrix])

# Use the @ operator to calculate the matrix product of third_matrix
# by first_matrix.

# print(third_matrix @ first_matrix)

# Reshape third_matrix into an array of dimensions 3 × 3 × 2.

print(third_matrix.reshape(3, 3, 2))
