


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

ancho_columna=[]
count=0
while count<=len(tableData):
    for i in range(len(tableData)):
        ancho_columna.append(len(tableData[i][count]))
    count+=1
ancho_columna=max(ancho_columna)


def imprimir_tabla(lista_valores,ancho_columna):

    espacio=0
    while espacio<=len(lista_valores):
        for i in range(len(lista_valores)):
            print(lista_valores[i][espacio].rjust(ancho_columna),end='')
        espacio+=1
        print('')

imprimir_tabla(tableData,ancho_columna)