import numpy as np

# Create a matrix


matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
second_matrix = np.array([[5, 2, 3], [8, 5, 6], [1, 8, 9]])

# print(second_matrix @ matrix)
# print(matrix.shape)
# print(matrix.sum())
# print(matrix.min())
# print(matrix.max())
# print(matrix.transpose())
# print(matrix.mean())

# stacking matrices

# vertical staking

third_matrix = np.vstack([matrix, second_matrix])
# print(third_matrix)

# horizontal staking

forth_matrix = np.hstack([matrix, second_matrix])
# print(forth_matrix)

# reshaping

fifth_matrix = matrix.reshape(9, 1)
# print(fifth_matrix)

sixth_matrix=np.arange(1,24,2).reshape(3,2,2)
# print(sixth_matrix)

# ramdom matrix

ram_matrix=np.random.random([3,3])
print(ram_matrix)

