"""Challenge: Simulate a Coin Toss Experiment 8.8"""

import random as r


def lanza_moneda():
    """Simula el lanzamiento de una moneda al aire"""
    if r.randint(0, 1) == 0:
        return 'cara'
    else:
        return 'escudo'

numero_lanzamietos=0
intentos=100_000

for i in range(intentos):
    resultado=lanza_moneda()  # Lanza la moneda
    numero_lanzamietos+=1
    while resultado==lanza_moneda():  # Mientras el resultado no cambia sigue lanzando la moneda.
        lanza_moneda()
        numero_lanzamietos+=1
    numero_lanzamietos+=1

promedio=numero_lanzamietos/intentos
print(f'En promedio se requieren {promedio:.2f} lanzamientos para que la moneda cambie de resultado.')