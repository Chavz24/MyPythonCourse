"""Review Exercises 9.1"""

# Create a tuple literal named cardinal_numbers that holds the strings
# "first", "second" and "third", in that order.

cardinal_numbers = "first", "second", "third"

# Using index notation and print(), display the string at index 1 in
# cardinal_numbers.

print(cardinal_numbers[1])

# Unpack the values in cardinal_numbers into three new strings
# named position1, position2 and position3 in a single line of code,
# then print each value on a separate line.

position1, position2, position3 = cardinal_numbers

# Create a tuple called my_name that contains the letters of your name
# by using tuple() and a string literal.

mi_nombre = tuple("Mikolas")

# Check whether or not the character "x" is in my_name using the in
# keyword.

print('x' in mi_nombre)

# Create a new tuple containing all but the first letter in my_name using
# slicing notation.

new_tuple = mi_nombre[1:]
print(new_tuple)
