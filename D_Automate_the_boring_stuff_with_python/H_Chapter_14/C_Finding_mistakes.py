"""Este programa busca un error en un googlesheet y le indica al usuario la celda
    donde esta el error"""

import ezsheets

ss=ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

sheet=ss[0]

for i,row in enumerate(sheet,start=1):
    try:
        if (int(row[0])*int(row[1]))==int(row[2]):
            continue
        else:
            print(f'There is a mistake in cell {ezsheets.convertAddress(3,i)}')
    except ValueError:
        continue
