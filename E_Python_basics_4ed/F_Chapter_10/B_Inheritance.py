"""Review Exercises 10.3"""


# Define classes that inherit from the Dog class The classes should
# change the sonido method

class Dog():
    """Creates a dog class"""

    species = 'Canis Familiaris'  # Propieedades generales del objeto/class attribute

    def __init__(self, name, age):  # Propiedades de del objeto/instance attribute
        self.name = name
        self.age = age

    # Metodos del objeto /instance methods

    def __str__(self):
        return f'{self.name} is {self.age} years old.'

    def sonido(self, sound):
        return f'{self.name} ladra: {sound}.'


class Boxer(Dog):  # THis class has all the attributes of the Dog Class.

    def sonido(self, sound='Goof'):
        return super().sonido(sound)


class GreatDanes(Dog):  # This class has all the attributes of the Dog Class.

    def sonido(self, sound='Rawr'):
        return super().sonido(sound)


class FoxTerrier(Dog):  # THis class has all the attributes of the Dog Class.

    def sonido(self, sound='Guauf'):
        return super().sonido(sound)  # Con el metodo super() busca el metodo en la clase padre
        # y pase el valor a esta, asi solo se modifica el metodo
        # en la clase padre y modifica a todas las de mas.


pet = Boxer('Mike', 5)
pet2 = GreatDanes('Mali', 5)
pet1 = FoxTerrier('Bet', 5)

print(pet.sonido())
print(pet1.sonido())
print(pet2.sonido())


# Create a GoldenRetriever class that inherits from the Dog class. Give
# the sound argument of the GoldenRetriever.speak() method a default
# value of "Bark".

class GoldenRetriever(Dog):
    def sonido(self, sound='Bark'):
        return super().sonido(sound)


my_golden_retriever = GoldenRetriever('Becky', 2)
print(my_golden_retriever.sonido())


# Write a Rectangle class that must be instantiated with two
# attributed: length and width. Add a .area() method to the class that
# returns the area (length * width) of the rectangle. Then write
# a Square class that inherits from the Rectangle class and that is
# instantiated with a single attribute called side_length.

class Rectangle():
    """Crea figuras geometricas de la familia de los rectangulos"""

    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        try:
            area = float(self.largo) * float(self.ancho)
            return area
        except TypeError:
            return f'Los valores introducidos deben de ser numericos.'
        except ValueError:
            return f'Los valores introducidos deben de ser numericos.'

# my way
class Square(Rectangle):
    """Crea cuadrados"""

    def __init__(self, longitud_lados):
        Rectangle.__init__(self, largo=longitud_lados, ancho=longitud_lados)
        self.longitud_lados = longitud_lados

# the pythonic way
# class Square(Rectangle):
#     def __init__(self, side_length):
#         super().__init__(side_length, side_length)
cuadrado = Square(4)
print(cuadrado.area())
