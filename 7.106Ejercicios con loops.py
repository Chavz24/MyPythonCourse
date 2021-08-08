#crea un programa que pida por teclado una contresena. La contrasena no podra tener menos de 8 caracteres
#ni espacios en blanco.Si la contrsena es correcta debe imprimir espacio ok. en caso contrario imprime
# contrasena erronea

Cntrsn=input("Digite una contrasena: ")# pide una contresena al user
Cntdr=0
for i in (Cntrsn): #loop para validar la contrsena
    if i==' ': # si se detecta un espacio
        Cntdr=0 # se resetea el contador
        break # y se rompe el loop
    else:# si no se detecta espacios
        Cntdr+=1 # se incrmenta el contador en uno
if Cntdr>=8:#valida si el contador tiene los suficientes caracteres para cumplir con los reequisitos
    print('Contrasena correcta')
else:
    print('Contrasena incorrecta')



