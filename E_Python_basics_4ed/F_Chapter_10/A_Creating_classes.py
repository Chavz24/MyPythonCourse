"""Review Exercises 10.2"""


# Create a dog class.

# class Dog():
#     """Creates a dog class"""
#
#     species = 'Canis Familiaris'  # Propieedades generales del objeto/class attribute
#
#     def __init__(self, name, age):  # Propiedades de del objeto/instance attribute
#         self.name = name
#         self.age = age
#
#     # Metodos del objeto /instance methods
#
#     def __str__(self):
#         return f'{self.name} is {self.age} years old.'
#
#     def sonido(self, sound):
#         return f'{self.name} says {sound}.'

# Modify the Dog class to include a third instance attribute called
# coat_color that stores the color of the dog’s coat as a string


class Dog():
    """Creates a dog class"""

    species = 'Canis Familiaris'  # Propieedades generales del objeto/class attribute

    def __init__(self, name, age, coat_color):  # Propiedades de del objeto/instance attribute
        self.name = name
        self.age = age
        self.coat_color = coat_color

    # Metodos del objeto /instance methods

    def __str__(self):
        return f'{self.name} is {self.age} years old.'

    def sonido(self, sound):
        return f'{self.name} says {sound}.'


# Create a Car class with two instance attributes: .color, which stores
# the name of the car’s color as a string, and .mileage, which stores
# the number of miles on the car as an integer. Then instantiate
# two Car objects—a blue car with 20,000 miles, and a red car with
# 30,000 miles, and print out their colors and mileage

class Car():  # definiendo la clase
    """Creates a car class"""

    def __init__(self, color, mileage):  # instance attribute
        self.color = color
        self.mileage = mileage


blue_car = Car('blue', 20_000)
red_car = Car('red', 30_000)

print(f'The {blue_car.color} has {blue_car.mileage:,} miles.')
print(f'The {red_car.color} has {red_car.mileage:,} miles.')


# Modify the Car class with an instance method called .drive() that
# takes a number as an argument and adds that number to the.
# mileage attribute. Test that your solution works by instantiating
# a car with 0 miles, then call .drive(100) and print the .mileage
# attribute to check that it is set to 100.

class Car():  # definiendo la clase
    """Creates a car class"""

    def __init__(self, color, mileage):  # instance attribute
        self.color = color
        self.mileage = mileage

    #  Metodo de instancia

    def drive(self, miles):
        self.mileage = self.mileage + miles

car_A=Car('gray',0)

print(car_A.mileage)
car_A.drive(100)
print(car_A.mileage)
car_A.drive(1000)
print(car_A.mileage)
