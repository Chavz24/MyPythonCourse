# Crear una calculadora de precios para productos, Leccion 3

# Precio=0.0 #Variable tipo float
# Cant=0     #Variable tipo int

Precio = float(input("Ingrese el precio:"))#tranformando una variable tipo str a float
Cant = int(input("Ingrese la cantidad:"))#tranformando una variable tipo str a int
Total = (Precio * Cant)

print("Total a pagar:",Total)


