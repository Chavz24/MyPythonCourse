"""este programa hace un countdown y reproduce un sonido de alarma
cuando el countdown termina"""

import subprocess,time,datetime

tiempo=5

while tiempo>0:
    print(tiempo)
    time.sleep(1)
    tiempo-=1

path_to_sound=''
subprocess.Popen(['start',f'{path_to_sound}'],shell=True)


# ano=datetime.datetime.now().year
# print(ano)
# happy_birthday_yomar=datetime.datetime(ano,12,18)
# print(happy_birthday_yomar.month)
# print(happy_birthday_yomar.day)

