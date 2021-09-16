# class X(Y) “Make a class named X that is-a Y.”

class AClass:
    pass


class MyClass(AClass):
    pass


# class X has-a __init__ that takes self and J parameters

class ClassRa(object):
    def __init__(self, parameter):
        self.parameter = parameter


# class X has-a function named M that takes self and J parameters.

class NoClass:
    def __init__(self):
        self.parameter = "Attribute"

    def my_function(self, parameter):
        pass


# “Set foo to an instance of class X.”

foo = NoClass()

# “From foo, get the M function, and call it with parameters self, J

foo.my_function(parameter="par")

# “From foo, get the K attribute, and set it to Q

print(foo.parameter)
