from pathlib import Path
import csv

temperature_readings = [68, 65, 68, 70, 74, 72]

file_path = Path.cwd() / 'EE_temp.cvs'

# with file_path.open(mode='a', encoding='utf-8') as file:
#     file.write(str(temperature_readings[0]))
#     for temp in temperature_readings[1:]:
#         file.write(f',{temp}')

daily_temperatures = [
    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [68, 70, 74, 76, 74, 73],
[68, 70, 74, 76, 74, 73]
]

with file_path.open(mode='w', encoding='utf-8',newline='') as file:
    write = csv.writer(file)
    write.writerows(daily_temperatures)
