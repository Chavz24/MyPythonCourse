"""Review Exercises 8.5"""

# Using break, write a program that repeatedly asks the user for some
# input and only quits if the user enters "q" or "Q".

# while True:
#     user_input = input('Ingrese un dato: ')
#     if user_input.lower() == 'q':
#         break


# Using continue, write a program that loops over the numbers 1 to
# 50 and prints all numbers that are not multiples of 3

for i in range(1, 51):
    if i % 3 == 0:
        continue
    else:
        print(f'{i}, no es multiplo de tres.')
