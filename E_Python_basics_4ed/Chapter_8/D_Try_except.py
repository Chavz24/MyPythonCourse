"""Review Exercises 8.6"""

# Write a script that repeatedly asks the user to input an integer,
# displaying a message to “try again” by catching the ValueError that
# is raised if the user did not enter an integer. Once the user enters an integer,
# the program should display the number back to the user and end without crashing.

# while True:
#     try:
#         user_input=int(input('Introduce un numero: '))
#         print(f'El numero introducido es {user_input}.')
#         break
#     except ValueError:
#         print('Intentelo de nuevo')

# Write a program that asks the user to input a string and an integer
# n. Then display the character at index n in the string.
# Use error handling to make sure the program doesn’t crash
# if the user does not enter an integer or the index is out of bounds.
# The program should display a different message depending on
# what error occurs.

try:
    user_mesage=input('Introduce un mensaje: ')
    user_num=int(input('Introduce un numero: '))
    print(f'La letra en la posicion {user_num} del mensaje es {user_mesage[user_num]}.')
except ValueError:
    print('Debe introducir un numero entero.')
except IndexError:
    print(f'Numero mayor que la cantidad de caracteres del mensaje.')





