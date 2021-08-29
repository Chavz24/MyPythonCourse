from pathlib import Path
import csv

file_path = Path.cwd() / 'FF_people.csv'
headers = ['name', 'department', 'salary']


# with file_path.open(mode='a',encoding='utf-8',newline='') as file:
#     file.write(headers[0])
#     for header in headers[1:]:
#         file.write(f',{header}')

def row_procces(row):
    row['salary'] = float(row["salary"])
    return row


with file_path.open(mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(dict(row_procces(row)))

people = [
    {"name": "Veronica", "age": 29},
    {"name": "Audrey", "age": 32},
    {"name": "Sam", "age": 24}
]

file_path2=Path.cwd() / 'FF_People_list.csv'

with file_path2.open(mode='w',encoding='utf-8',newline='') as file:
    writer=csv.DictWriter(file,fieldnames=people[0].keys())
    writer.writeheader()
    writer.writerows(people)

