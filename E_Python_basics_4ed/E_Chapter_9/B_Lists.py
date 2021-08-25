"""Review Exercises 9.2"""

# Create a list named food with two elements "rice" and "beans".

comida=list(('arroz','habichuela'))

# Append the string "broccoli" to food using .append().

comida.append('Brocoli')

#  Add the string "bread" and "pizza" to "food" using .extend().

comida.extend(('pan','pizza'))

# Print the first two items in the food list using print() and slicing
# notation.

print(comida[:2])

# Print the last item in food using print() and index notation.

print(comida[-1])

# Create a list called breakfast from the string "eggs, fruit, orange
# juice" using the string .split() method.

desayuno="eggs,fruit,orange juice".split(',')

# Verify that breakfast has three items using len().

print(len(desayuno))

#  Create a new list called lengths using a list comprehension
#  that contains the lengths of each string in the breakfast list.

longitud=[len(i) for i in desayuno]

print(longitud)
