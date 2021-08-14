#Un stopwatch simple
from time import time

# def calc_prod():
#     product=1
#     for i in range(1,100000):
#         product=product*i
#
#     return product
#
# start_time=time()
# proc=calc_prod()
# end_time=time()
#
# print(f'The result is {len(str(proc))} digits long')
# print (f'This program took {end_time-start_time} seconds to execute')
print('Presione enter para inicar. Presione enter para parar. Presione CTRL+c para salir')


input()

start_time=time()
last_time=start_time
lap_number=1

print(f'Inicando vuelta numero {lap_number}.')

try:
    while True:
        input()
        lap_time=round(time()-last_time,2)#time of each lap
        total_time=round(time()-start_time,2)
        print(f'Vuelta # {lap_number}:Tiempo total: {total_time} Tiempo vuelta: {lap_time}',end='')
        lap_number+=1
        last_time=time()#time a new lap starts


except KeyboardInterrupt:
    print('\nDone')
