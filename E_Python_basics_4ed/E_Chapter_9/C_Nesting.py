"""Review Exercises 9.2"""


# Create a tuple data with two values. The first value should be the
# tuple (1, 2) and the second value should be the tuple (3, 4).

a_tuple=(1,2),(3,4)


# Write a for loop that loops over data and prints the sum of each
# nested tuple.
count=1
for value in a_tuple:
    suma=0
    for num in value:
        suma+=num

    print(f'Row {count} sum: {suma}')
    count+=1
# or
for value in a_tuple:
    suma=sum(value)
    print(f'Row {a_tuple.index(value)+1} sum: {suma}')

# Create the following list [4, 3, 2, 1] and assign it to the variable numbers.

numbers=[4, 3, 2, 1]

# Create a copy of the numbers list using the [:] slicing notation.

numbers_copy=numbers[:]

# Sort the numbers list in numerical order using the .sort() method.

numbers.sort()
