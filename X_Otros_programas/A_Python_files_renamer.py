"""Este programa le cambia el formato de nombre a los 'scripts' de python a un formato estandar"""

import os, shutil,re, string
from pathlib import Path



working_folder=Path(r'C:/Users/migue/Desktop/Nueva carpeta')
copy_folder=Path(r'C:/Users/migue/Desktop/Copia')
alphabets=list(string.ascii_uppercase)


#Regex para identificar archivos a renombrar.

remove_numbers=re.compile(r"""^(\d{1,}\.\d{1,})
(\s)?
(.*?)?
(.py)$""", re.VERBOSE)

count=0
for file in os.listdir(working_folder):
    rename_files=remove_numbers.search(file)

    try:
        file_name=rename_files.group(3).replace(' ', '_')
        file_extention=rename_files.group(4)
        #print(file_name)
        new_name=f'{alphabets[count]}_{file_name.capitalize()}{file_extention}'

        print(working_folder/f'{file}',copy_folder/f'{new_name}')
        shutil.move(working_folder/f'{file}',copy_folder/f'{new_name}')
        count+=1
    except AttributeError:
        continue


