"""Challenge: Find the Factors of a Number 8.4"""

# Write a script that asks the user to input a positive integer
# and then prints out the factors of that number.


while True:
    try:
        num = int(input("Ingrese un numero entero positivo: "))
        if num > 0:
            break
        else:
            print("Intente de nuevo.")
    except:
        print("Intente de nuevo.")

for n in range(1, (num + 1)):
    if num % n == 0:
        print(f'{n} es un factor de {num}.')
    else:
        continue
