#'crea un programa que pida numeros por teclado. El program debe tener una funcion,que deviuelve el numero
#'mayor de los dos introducidos'.

print("*"*8, 'Devuelve el numero maximo',"*"*8,'\n')


while True:
    try:
        primer_numero=int(input('Introduce un numero: '))
        segundo_numero=int(input('Introduce otro numero: '))
        if primer_numero==segundo_numero:
            print('Los numero son iguales. intente con tros numeros!\n')
        else:
            break
    except ValueError:
        print('Debe introducir un numero, no se aceptan letras!!')

numero_maximo = 0
def devuelve_numero_maximo(num1,num2):
    global numero_maximo
    if primer_numero>segundo_numero:
        numero_maximo=primer_numero
    else:
        numero_maximo=segundo_numero
    return numero_maximo

devuelve_numero_maximo(primer_numero,segundo_numero)

print('El numero ',numero_maximo,' es el mayor de los dos')