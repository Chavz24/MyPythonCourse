# Leccion 5
# Crear un programa que pida, el nombre del producto, precio, cantidad
# y de como output el total a pagar junto con el nombre del producto.

Nombre = input("Ingrese el nombre del producto:")
Precio = float(input("Ingrese el precio del producto:"))
Cantidad = int(input("Ingrese el cantidad del producto:"))
Total = Precio * Cantidad

# Tres formas para concatenar
# Con esta manera puedo concatenar variables de diferentes tipos
print("El total a pagar por el producto", Nombre, "es", Total)  # La variable Nombres es str y Total es float
# Con esta forma no se pueden concatenar variables de diferentes tipos
print("El total a pagar por el producto " + Nombre + " es " + str(Total))
# Con esta forma, utilizando el  comando format este cambia todas las variables a str
print("El total a pagar por el producto {} es {}".format(Nombre, Total))
# Con esta forma es similar a la anterior, solo que las variables se introducen manualmete en el lugar que se desea.
print(f"El total a pagar por el producto {Nombre} es {Total}")
# Con esta forma usando el operador % se puede dcir cuantos numeros despues del punto decimal imprimir
# para str= %s, para int= %d, float=%f(si se pone un numero antes de la letra eso indica la cantidad de decimales a mostrar.
print("El total a pagar por el producto %s" % Nombre, "es %.2f" % Total)
# Una forma mas limpia del ejemplo anterior.
print("El total a pagar por el producto %s es %.2f" % (Nombre,Total))

