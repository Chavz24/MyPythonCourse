# Las variables en python son :
# 1)Strings: o tipo cadena, son un conjunto de caracteres que se escriben dentro de comillas ("String" o 'String')
# 2Numericas: pueden ser numeros enteros o int (3,-4,0, etc), numeros con decimales o float (12.3, 0.44566, etc)
# o numeros complejos (5+5j)
# 3 Variables de tipo logico o bool: son aquellas que solo pueden tomar valores de True o False o 0,1.


# Las variables en python son nombres de objetos que se guardan en memoria para ser usados mas adelante.
# Las variables pueden ser nombradas segun gustes pero deben de seguir ls reglas generales para facilitar
# el entendimiento del codigo mas adelante.
# Python sugiere usar el metodo snake_case o el CamelCase.
# Metodo snake_case: se nombran las variables en minusculas separando las palabras con un underscore(_).
# Metodo CamelCase: se nombran las variables iniciando cada palabra en mayusculas sin espacio entre ellas.
# Reglas para declarar variables en python;
# 1)El primer caracter no puede ser un numero, es decir, no se puede declarar una variable por ejemplo
# 1producto_aleatorio.
# 2)No usar caracteres especiales como son @,#,$,%, etc.
# 3)No usar palabras reservadas de python.
# Por ultimo para crear una variable en python se sigue el siguiente proceso:
# 1)Se escribe el nombre de la variable siguiendo uno de los metodos ya descritos y sin romper las reglas enunciadas.
# 2)Se digita el signo de (=).
# 3)Se digita el valor que se le quiere dar a la variable.
# Nota: Siempre el nombre de la variable va a la izquierda del signo (=) y el valor a la derecha del signo(=).
# Nota2: toda variable declarada dentro de comillas ("Variable") o apostrofes('Variable') es de tipo cadena o str
# sin importar que sea un  numero, es decir, la variable "200" es tipo str aunque es un numero.


EdadPersona = 25  # int
NombrePersona = "Romero"  # str
precio_producto = 12.56  # float
existencia_producto = True  # bool

# Aqui la funcion type() devuelve el tipo de dato a que corresponde una variable o un objeto.
# print(type(EdadPersona))
# print(type(NombrePersona))
# print(type(precio_producto))
# print(type(existencia_producto))

# Colecciones en Python
# Las colecciones en python son basicamente contenedores de datos.
# Los tipos pricipales de colleciones en python son:

# 1)Listas: se declaran en corchetes [] y su contenido puede ser cambiado y pueden contener variables como colleciones.
# 2)Tuplas: se declaran entre parentesis () y su contenido es inmutable.
# 3)Set: se declara en llaves {} no acepta valores duplicados
# 4)Diccionario: se declaran en llaves {} su contenido puede ser cambiado. se escriben datos en forma key: value
# que se utilizan para extraer datos de manera mas eficiente.

# Ejemplo de lista

ListaVariada = ["Jose", "Juan", (1200, 2000, 3000, 400), 34.5, True]
print(ListaVariada)
print(ListaVariada[2])  # Imprimiendo una posicion especifica de la lista (la tupla dentro de la lista solo representa
# una posicion dentro del la lita.

# Ejemplo de tupla

CodigoArea = (557, 546, 800, 577, [2, 40, 6, 'juan'])
print(CodigoArea)
print(CodigoArea[4])  # Imprime una posicion especifica de la tupla.

# Ejemplo de diccionarios

CodigoProdutos = {12: 'Impresora', 15: 'Camara', 18: 'Mouse'}
print(CodigoProdutos[12]) # Asi se llamo un codico dentro de un diccionario.

# Ejemplo de Set

IdentificadorProducto = {145, 145, 145, 255, 346, 7}

print(IdentificadorProducto)

#Identificando las colecciones

print(type(CodigoArea)) #tuple
print(type(IdentificadorProducto)) #set
print(type(CodigoProdutos))#dict
print(type(ListaVariada))#list