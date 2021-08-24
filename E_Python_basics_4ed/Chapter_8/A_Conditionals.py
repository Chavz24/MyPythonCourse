"""Review Exercises 8.3"""

# Write a script that prompts the user to enter a word using the
# input() function, stores that input in a variable, and then displays
# whether the length of that string is less than 5 characters, greater
# than 5 characters, or equal to 5 characters by using a set of if, elif
# and else statements.

word=input('Indroduce una palabra: ')

if len(word)<5:
    print('La palabra introducida tiene menos de 5 caracteres.')

elif len(word)>5:
    print('La palabra introducida tiene mas de 5 caracteres.')
else:
    print('La palabra introducida tiene 5 caracteres.')
