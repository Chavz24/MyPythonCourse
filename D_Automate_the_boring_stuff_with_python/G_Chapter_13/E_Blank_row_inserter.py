

import openpyxl,pyinputplus

#file_name="EE_Blank_row_inserter.xlsx"

print('''Nota: Tenga en cuenta qe los cambios se guardaran en el mismo archivo
cree una copia de seguridad antes de realizar cualquier cambio.''')


file_name=pyinputplus.inputFilename(prompt='Ingrese el nombre del archivo: ')

n=pyinputplus.inputInt(prompt='Ingrese el numero de fila: ')

m=pyinputplus.inputInt(prompt='Ingrese la cantida de filas a insertar: ')

print("Insertando filas...")

wb=openpyxl.load_workbook(filename=file_name)

sheet=wb['Hoja']


sheet.insert_rows(n,amount=m)
#sheet.delete_rows(10,amount=3)
#sheet.move_range('B8:CV100',rows=-6,cols=0)

wb.save(filename=file_name)

print('Terminado.')