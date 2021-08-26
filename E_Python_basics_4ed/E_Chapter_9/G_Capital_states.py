"""Challenge: Capital City Loop 9.7"""

# display the name of the state to the user and ask them to enter
# the capital.
from random import choice

capitales_estados = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
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

estados = [estado for estado in capitales_estados.keys()]

estado = choice(estados)
capital = capitales_estados[estado]
user_answer = input(f'Cual es la capital del estado de {estado}?')

while user_answer.lower() != capital.lower():
    user_answer = input(f'Cual es la capital del estado de {estado}?')
    if user_answer.lower() == 'exit':
        print(f'La respuesta correcta es {capital}.')
        break
