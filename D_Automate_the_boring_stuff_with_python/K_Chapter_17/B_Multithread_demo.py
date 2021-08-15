import datetime,time,threading

# noche_buena_2021=datetime.datetime(2021,12,24)
#
# print(noche_buena_2021>datetime.datetime.now())
#
# while noche_buena_2021>datetime.datetime.now():
#     time.sleep(10)
#
#     print('hola')

print('Cominezo del programa..')

def pausa():
    time.sleep(2)
    print('Se acabo la pausa')

thread_obj=threading.Thread(target=pausa)

thread_obj.start()#second thread

print('Final del programa')
