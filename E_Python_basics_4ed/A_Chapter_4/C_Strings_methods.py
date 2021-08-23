'''Review Exercises 4.3'''


# Write a script that converts the following strings to lowercase: "Animals", "Badger", "Honey Bee", "Honeybadger".
# Print each lowercase string on a separate line.

string_list=["Animals", "Badger", "Honey Bee", "Honeybadger"]

for string in string_list:
    #print(string.lower())
    pass

# Repeat Exercise 1, but convert each string to uppercase instead of lowercase.

for string in string_list:
    #print(string.upper())
    pass

# Write a script that removes whitespace from the following strings.
# Print out the strings with the whitespace removed.

string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "

# print(string1.lstrip())
# print(string2.rstrip())
# print(string3.strip())

# Write a script that prints out the result of .startswith("be") on each of the following strings:

string_1 = "Becomes"
string_2 = "becomes"
string_3 = "BEAR"
string_4 = " bEautiful"
# print(string_1.startswith('be'))
# print(string_2.startswith('be'))
# print(string_3.startswith('be'))
# print(string_4.startswith('be'))

# Using the same four strings from Exercise 4, write a script that
# uses string methods to alter each string so that .startswith("be") returns True for all of them.

string_list2=[string_4,string_1,string_3,string_2]

for string in string_list2:
    print(string.strip().lower().startswith('be'))
