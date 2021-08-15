

from time import time
import pyperclip

print('Presione enter para inicar. Presione enter para parar. Presione CTRL+c para salir')

input()
start_time=time()
last_time=start_time
lap_number=1

print(f'Inicando vuelta numero {lap_number}.')
general_info=[]
try:
    while True:
        input()
        lap_time=round(time()-last_time,2)#time of each lap
        total_time=round(time()-start_time,2)
        num_vuelta=f'Vuelta #{str(lap_number).rjust(2)}: '
        tiempo_acu=f'Tiempo desde el inicio {str(total_time).rjust(5)}, '
        tiempo_vuelta=f'Tiempo vuelta {str(lap_time).rjust(5)}.'
        info_vuelta=num_vuelta+tiempo_acu+tiempo_vuelta
        print(info_vuelta,end='')
        general_info.append(info_vuelta)#adding every lap to a list
        pyperclip.copy('\n'.join(general_info))#Coping every event to the clipboard
        lap_number+=1
        last_time=time()#time a new lap starts
except KeyboardInterrupt:
    print('\nDone')

