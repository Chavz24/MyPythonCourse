'''Review Exercises 4.8'''


# In one line of code, display the result of trying to .find()
# the substring "a" in the string "AAA". The result should be -1.

print('AAA'.find('a'))

# Replace every occurrence of the character "s" with "x" in the string "Somebody said something to Samantha."

phrase="Somebody said something to Samantha."
print(phrase.replace('s','x'))

# Write and test a script that accepts user input using the input()
# function and displays the result of trying to .find() a particular
# letter in that input.

letter_to_find='e'
user_input=input('Write something: ')
print(f'La letra {letter_to_find} se encuentr en la frase {user_input}')
