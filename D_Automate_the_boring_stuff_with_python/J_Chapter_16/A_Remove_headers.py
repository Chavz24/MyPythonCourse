
#Removes header from csv filees in cwd
import os
from csv import writer,reader
from os import listdir,makedirs,path

makedirs('AA_Header_removed',exist_ok=True)

#Looping in search of every in the cwd

for csv_file_name in listdir('.'):
    #making the program only targets files with the .csv ext
    if not csv_file_name.endswith('.csv'):
        continue
    print('Removing Header from ' + str(csv_file_name + '....'))

    csv_rows=[]
    csv_file_obj=open(csv_file_name)
    csv_reader_obj=reader(csv_file_obj)
    #taking out the headers from the files
    for row in csv_reader_obj:
        if csv_reader_obj.line_num==1:
            continue
        csv_rows.append(row)
    csv_file_obj.close()
    #writing new csv file
    csv_file_obj=open(os.path.join('AA_Header_removed', csv_file_name),'w',newline='')
    csv_file_writer=writer(csv_file_obj)
    for row in csv_rows:
        csv_file_writer.writerow(row)
    csv_file_obj.close()




