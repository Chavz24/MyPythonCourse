#generador de  quiz aleatorio, crea quiz con las mismas preguntas
# en orden aleatorio y las respuestas en orden aleatorio

from random import shuffle,sample

#Dict con las Claves y los Values

capitales_estados={'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


for num_quiz in range(3):
    archivo_quiz=open(f'quiz_capitales{num_quiz+1}.txt','w')
    archivo_respuestas=open(f'quiz_capitales_respuestas{num_quiz+1}.txt','w')

    archivo_quiz.write('Name:\n\nFecha:\n\nClase:\n\n')
    archivo_quiz.write((' '*20)+f'Quiz de capitales (No.{num_quiz+1})')
    archivo_quiz.write('\n\n')
    archivo_respuestas.write(f'Quiz #{num_quiz+1}\n')

    estados=list(capitales_estados.keys())
    shuffle(estados)

    for num_pregunta in range(50):
        resp_correcta=capitales_estados[estados[num_pregunta]]
        resp_incorrecta=list(capitales_estados.values())
        del resp_incorrecta[resp_incorrecta.index(resp_correcta)]
        resp_incorrecta=sample(resp_incorrecta,3)
        opcines_respuesta=resp_incorrecta+[resp_correcta]
        shuffle(opcines_respuesta)

        archivo_quiz.write(f'{num_pregunta+1}.Cual es la capital de {estados[num_pregunta]}?\n')
        for i in range(4):
            archivo_quiz.write(f'    {"ABCD" [i]}. {opcines_respuesta[i]}\n')
        archivo_quiz.write('\n')
        archivo_respuestas.write(f"{num_pregunta+1}.{'ABCD' [opcines_respuesta.index(resp_correcta)]}\n")
    archivo_quiz.close()
    archivo_respuestas.close()



