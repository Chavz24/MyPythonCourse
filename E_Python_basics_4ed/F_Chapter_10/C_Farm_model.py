"""Challenge: Model a Farm 10.4"""


# This script models a farm


class AnimalGranja():
    def __init__(self, nombre, peso, sexo, edad):
        self.nombre = nombre
        self.peso = peso
        self.sexo = sexo
        self.funcion = True
        self.edad = edad
        self.salud = False

    def __str__(self):
        return f'{self.nombre} es de sexo {self.sexo} y tiene {self.edad}'

    def comestible(self):
        if self.funcion:
            return f'{self.nombre} es comestible.'
        else:
            return f'{self.nombre} no es comestible.'

    def estado(self):
        if self.salud:
            return f'{self.nombre} esta enfermo'
        else:
            return f'{self.nombre} no esta enfermo'

    def sonido(self, suena):
        return f'{self.nombre} suena: {suena}'

    def deplazamiento(self,tipo):
        if tipo == 'Avicola':
            return f'{self.nombre} es un ave y camina en dos patas.'
        else:
            return f'{self.nombre} no es un ave y camina a cuatro patas.'

class Vaca(AnimalGranja):

    def __init__(self, nombre, peso, sexo, edad, tipo, color):
        super().__init__(nombre, peso, sexo, edad)
        self.tipo= tipo
        self.alimento = False
        self.color = color

    def __str__(self):
        return f'{self.nombre} es ganado {self.tipo} y tiene {self.edad}'

    def sonido(self, suena='Moo.'):
        return super().sonido(suena)+f'Debe ser una vaca.'

    def deplazamiento(self,tipo=''):
        return super().deplazamiento(self.tipo)

class Cerdo(AnimalGranja):
    def __init__(self, nombre, peso, sexo, edad, tipo, color):
        super().__init__(nombre, peso, sexo, edad)
        self.tipo = tipo
        self.alimento = False
        self.color = color

    def __str__(self):
        return f'{self.nombre} es ganado {self.tipo} y tiene {self.edad}'

    def sonido(self, suena='oink.'):
        return super().sonido(suena) + f'Debe ser un cerdo.'

    def deplazamiento(self, tipo=''):
        return super().deplazamiento(self.tipo)

class Gallina(AnimalGranja):
    def __init__(self, nombre, peso, sexo, edad, tipo, color):
        super().__init__(nombre, peso, sexo, edad)
        self.tipo = tipo
        self.alimento = False
        self.color = color

    def __str__(self):
        return f'{self.nombre} es ganado {self.tipo} y tiene {self.edad}'

    def sonido(self, suena='Co Co Co.'):
        return super().sonido(suena) + f'Debe ser una Gallina.'

    def deplazamiento(self, tipo=''):
        return super().deplazamiento(self.tipo)

class Ovejo(AnimalGranja):
    def __init__(self, nombre, peso, sexo, edad, tipo, color):
        super().__init__(nombre, peso, sexo, edad)
        self.tipo = tipo
        self.alimento = False
        self.color = color

    def __str__(self):
        return f'{self.nombre} es ganado {self.tipo} y tiene {self.edad}'

    def sonido(self, suena='Bee beee.'):
        return super().sonido(suena) + f'Debe ser una oveja.'

    def deplazamiento(self, tipo=''):
        return super().deplazamiento(self.tipo)

class Caballo(AnimalGranja):
    def __init__(self, nombre, peso, sexo, edad, tipo, color):
        super().__init__(nombre, peso, sexo, edad)
        self.tipo = tipo
        self.alimento = False
        self.color = color

    def __str__(self):
        return f'{self.nombre} es ganado {self.tipo} y tiene {self.edad}'

    def sonido(self, suena='Hiii.'):
        return super().sonido(suena) + f'Debe ser un caballo.'

    def deplazamiento(self, tipo=''):
        return super().deplazamiento(self.tipo)



porky=Caballo('Porky',200,'Masculino',12,'Equino','Negro')

print(porky.deplazamiento())
print(porky.sonido())
print(isinstance(porky,Vaca))