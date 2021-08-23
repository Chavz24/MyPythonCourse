'''Review Exercises 5.5'''

# Write a script that asks the user to input a number and then displays
# that number rounded to two decimal places.

user_input=input('Ingrese un numero: ')
rounded_user_input=round(float(user_input),2)
print(f'The number {user_input} rounded to 2 decimal spaces is {rounded_user_input}')


# Write a script that asks the user to input a number and then displays the absolute value of that number.

user_input=input('Ingrese un numero: ')
abs_user_input=abs(float(user_input))
print(f'The absolute value of the number {user_input}  is {abs_user_input}')

# Write a script that asks the user to input two numbers by using the
# input() function twice, then display whether or not the difference
# between those two number is an integer.

user_input1=input('Ingrese un numero: ')
user_input2=input('Ingrese un numero: ')
result=(float(user_input1)-float(user_input2)).is_integer()
print(f'Les resta de {float(user_input1)} y {float(user_input2)} es un numero entero? {result}')


