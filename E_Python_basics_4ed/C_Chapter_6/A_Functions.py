"""Review Exercises 6.2"""


# Write a function called cube() with one number parameter and returns
# the value of that number raised to the third power. Test the
# function by displaying the result of calling your cube() function on
# a few different numbers.

def cube(x):
    """This function takes the value x and rises it to the third power"""
    cub = pow(x, 3)
    return cub


print(cube(8))
print(cube(10))
print(cube(25))


# Write a function called greet() that takes one string parameter
# called name and displays the text "Hello <name>!", where <name> is
# replaced with the value of the name parameter.

def greet(nam):
    print(f'Hello, {nam}')


name = 'Marcos'
greet(name)
