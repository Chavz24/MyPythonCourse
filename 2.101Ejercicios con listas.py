## Las listas son los tipos de datos mas versatles dentro de las colleciones, ya que estas pueden:

## 1)Contener datos de diferentes tipos aunque normalmente suelen ser elementos del mismo tipo
ListaVariada = ["Abrigos", 2, "Mangos", True, "Flores", 12.3]
LisaElectronicos = ["Celular", "Laptop", "Tablet", "PC"]

## 2)Al igual que otros datos de tipo secuencial(strings o cadenas, tuplas, etc) las listas se pueden tando dividir
## como indexar.

# print(ListaVariada[2])#Imprime el valor con el indice 2 de la lista
# print(ListaVariada[2:])#Imprime una nueva lista a partir del valor con el indice 2.

## 3)Las listas se pueden concatenar

# print(ListaVariada+LisaElectronicos) #Imprime una nueva lista con los valores de ambas listas.

## 4)Las listas son mutables, es decir, us valores pueden ser cambiados, eliminados, expandidos o reducidos.

# ListaVariada[0] = "Biblia"  # Cambia el elemeto en la primera posicion de la lista con otro.
# print(ListaVariada)
# ListaVariada[:] = [3]  # Cambia todos los elementos de la lista por uno solo
# print(ListaVariada)
# ListaVariada[:] = []  # Elimina todos los elementos de la lista.
# print(ListaVariada)
# ListaVariada[2:4] = ["Piedras", 23, False, 43]  # Se pueden cambiar, o eliminar grupos de elementos en una lista
# print(ListaVariada)
# LisaElectronicos.append("Impresora")#Agrega un elmento al final de la lista con el methodo .append(solo acepta un elem.)
# print(LisaElectronicos)
#print(len(ListaVariada)) #Le funcion len() cuenta los elemento dentro de una lista.

##5) Es posible crear listas que contengan otras listas (termino usado es "nest")

ObjetosConjuntos= [ListaVariada,LisaElectronicos]
# print(ObjetosConjuntos)
# print(ObjetosConjuntos[0]) #El primer elemento de la lista ObsjetosConjuntos es ListaVariada
# print(ObjetosConjuntos[0][2]) #De esta forma se navega dento de los elementos de las lista internas.
