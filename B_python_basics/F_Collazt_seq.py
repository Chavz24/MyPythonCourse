
#the collatz seq


def collatz(numero):
    if numero%2==0:
        numero=numero//2
        print(str(numero)+'//'+'2 = '+str(numero))
    else:
        numero = (3* numero)+1
        print('3 * '+ str(numero) +'+1 = ' + str(numero))
    while numero!=1:
        return collatz(numero)


msj=''
while msj.lower()!='n':
    try:
        numero=int(input('ingrese un numero entero:'))
        collatz(numero)
    except:
        print('No ha ingresado un numero entero')
        msj=input('desea continuar y/n:')







