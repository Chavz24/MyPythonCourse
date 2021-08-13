#!python

APPID='67f4736a67704c00faf7f9f26fa8dae8'

from json import loads,dumps
from requests import get

from sys import argv,exit

#Get location from command line

if len(argv)<2:
    print(f'B_Open_weather.py se usa introduciendo un nombre de la ciudad, y el codigo de dos letras del pais')
    exit()

location=' '.join(argv[1:])
#location='SanTo Domingo,DO'

#Downloading the JSON data from the weather page

url=f'https://api.openweathermap.org/data/2.5/forecast?q={location}&lang=sp&appid={APPID}'

res= get(url)
res.raise_for_status()

# pprint.pprint(res.text)

weather_data=loads(res.text)

w=weather_data['list']

print(f'El clima para hoy en {(location).strip("DO").capitalize()} es: ')
print(w[0]['weather'][0]['main']+' - '+w[0]['weather'][0]['description'].capitalize())
print(f'Manana:  ')
print(w[1]['weather'][0]['main']+' - '+w[1]['weather'][0]['description'].capitalize())
print(f'Pasado manana:  ')
print(w[2]['weather'][0]['main']+' - '+w[2]['weather'][0]['description'].capitalize())