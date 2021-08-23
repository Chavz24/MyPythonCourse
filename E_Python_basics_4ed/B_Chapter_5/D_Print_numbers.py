'''Review Exercises 5.6'''

# Print the result of the calculation 3 ** .125 as a fixed-point number
# with three decimal places.

base=3
exponente=0.125
result=pow(base,exponente)
print(f'El resultado de elevar {base} a {exponente} es {result:.2f}.')

# Print the number 150000 as currency, with the thousands grouped
# with commas. Currency should be displayed with two decimal
# places.

balance=150000
print(f'Your current balance is {balance:,.2f} Zimbabwean dollars.')

# Print the result of 2 / 10 as a percentage with no decimal places.
# The output should look like 20%.

percentage=2/10
print(f'Tu descuento es de {percentage:.0%}.')
