'''Challenge: Pick Apart Your User’s Input 4.5'''

# Write a script named first_letter.py that first prompts the user for
# input by using the string "Tell me your password:" The script should
# then determine the first letter of the user’s input, convert that letter
# to upper-case, and display it back.

user_input=''

while user_input=='' or user_input==' ':
    user_input=input('Tell me your password: ')
    if user_input!=''and user_input!=' ':
        print('The first letter of you input is: '+user_input[0].upper())
    else:
        print('Introduce a character A-Z, a-z')
