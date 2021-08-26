"""Review Exercises 9.6"""

# Create an empty dictionary named captains.

captains = {}

# Using the square bracket notation, enter the following data into
# the dictionary, one item at a time.

captains['Enterprise'] = 'Picard'
captains['Voyager'] = 'Janeway'
captains['Defiant'] = 'Sisko'

# Write two if statements that check if "Enterprise" and "Discovery"
# exist as keys in the dictionary. Set their values to "unknown" if the
# key does not exist.

if 'Enterprise' not in captains:
    captains['Enterprise'] = 'Unknown'
if 'Discovery' not in captains:
    captains['Discovery'] = 'Unknown'

# Write a for loop to display the ship and captain names contained
# in the dictionary.

for ship, captain in captains.items():
    print(f'The {ship} is captained by {captain}.')

# Delete "Discovery" from the dictionary.

del captains['Discovery']

# Bonus: Make the same dictionary by using dict() and passing in
# the initial values when you first create the dictionary

captains_and_ships=(('Enterprise','Picard'),('Voyager','Janeway'),('Defiant','Sisko'))
captains2=dict(captains_and_ships)
