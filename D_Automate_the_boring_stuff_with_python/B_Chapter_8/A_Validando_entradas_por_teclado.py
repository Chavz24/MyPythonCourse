import pyinputplus as pyip

def sumar_hasta_10(num):
    lista_numeros=list(num)

    for i, digito in enumerate(lista_numeros):
        lista_numeros[i]=int(digito)
    if sum(lista_numeros)!=10:
        raise Exception ('los digitos deben sumar 10 no %s. '%sum(lista_numeros))
    return int(num)


resp=pyip.inputCustom(sumar_hasta_10)

