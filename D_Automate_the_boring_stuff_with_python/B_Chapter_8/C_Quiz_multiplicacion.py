#le pregunta al usuario 10 preguntas de multiplicacion

import pyinputplus as pyip
from random import randint
from time import sleep

num_preguntas=11
respuestas_correctas=0

for pregunta in range(1,num_preguntas):

    num1=randint(0,9)
    num2=randint(0,9)

    promt=f'#{pregunta}: {num1}x{num2} ='
    try:
        pyip.inputStr(promt,allowRegexes=[f'^{num1*num2}$'],
                      blockRegexes=[('.*','Incorrecto')],timeout=8,limit=3)
    except pyip.TimeoutException:
        print('Se acabo el tiempo')
    except pyip.RetryLimitException:
        print('No tienes mas intentos')
    else:
        print('Correcto')
        respuestas_correctas+=1
    sleep(1)

print(f'Puntos {respuestas_correctas}/{num_preguntas-1}')