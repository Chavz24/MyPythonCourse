#Crear un programa en usando for donde se impriman dos fraces alternadas

# for i in range (3):
#     print("Tic")
#     for i in range(1):
#         print("Tac")

#Crear un patron de piramides

i=5
for i in range(1,i+1):
    for i in range(1,i+1):
        print("*", end="")

    print(" ")
#Numeros primos

prime = int(input('numero : '))

if prime % 2 == 0 and prime > 2:
    print(prime, 'no es primo')

elif prime % 2 != 0:

    for i in range(2, prime,3):
        if prime % i == 0:
            print(i, prime, ' no es primo')
            break
    else:
        print(prime, 'es primo')

