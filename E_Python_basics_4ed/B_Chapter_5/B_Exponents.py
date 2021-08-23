'''Challenge: Perform Calculations on User Input 5.3'''

# Write a script called exponent.py that receives two numbers from the
# user and displays the first number raised to the power of the second
# number.


base=input('Ingrese una base: ')
exponente=input('Ingrese un exponente: ')
result=float(base)**float(exponente)
print(f'{base} elevado a {exponente} es = {result}')