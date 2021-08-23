"""Review Exercises 4.2"""

# Create a string and print its length using the len() function.
string='Have a nice day!'
print(len(string))


# Create two strings, concatenate them, and print the resulting string.
string1=string[:5]
string2=string[5:]
string3=string1+string2
print(string3)
# Create two strings and use concatenation to add a space in between them. Then print the result.
string_1=string
string_2='Thanks! You too!'
string_3=string_1+' '+string_2
print(string_3)

# Print the string "zing" by using slice notation on the string "bazinga" to specify the correct range of characters.

string_a='bazinga'
string_b=string_a[2:6]
print(string_b)