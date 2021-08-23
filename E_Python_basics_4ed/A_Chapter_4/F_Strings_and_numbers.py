'''Review Exercises 4.6'''

# Create a string containing an integer, then convert that string into an actual integer object using int().
# Test that your new object is a number by multiplying it by another number and displaying the result.

string_num='15'
string_num=int(string_num)
print(string_num*5)

# Repeat the previous exercise, but use a floating-point number and float().

string_num='23.5'
string_num=float(string_num)
print(string_num*2)

# Create a string object and an integer object, then display them side-by-side
# with a single print statement by using the str() function.

string='You are'
num= 25
print(string+' '+str(num))

# Write a script that gets two numbers from the user using the input() function twice,
# multiplies the numbers together, and displays the result.

first_number=int(input('Ingrese un numero: '))
second_number=int(input('Ingrese otro numero: '))
result=float(first_number*second_number)
print(result)

