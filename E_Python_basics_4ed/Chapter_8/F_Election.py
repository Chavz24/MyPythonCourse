"""Challenge: Simulate an Election 8.9"""

import random as r

def porcentaje_victoria(prob_de_ganar):
    if r.random()<prob_de_ganar:
        return "A wins"
    else:
        return "B wins"

gana_candidato_A=0
gana_candidato_B=0

numeero_intentos=10_000

for i in range(0,numeero_intentos):
    votos_candidato_A = 0
    votos_candidato_B = 0
    if porcentaje_victoria(0.87)=="A wins":
        votos_candidato_A+=1
    else:
        votos_candidato_B+=1
    if porcentaje_victoria(0.65)=="A wins":
        votos_candidato_A+=1
    else:
        votos_candidato_B+=1

    if porcentaje_victoria(0.17)=="A wins":
        votos_candidato_A+=1
    else:
        votos_candidato_B+=1

    if votos_candidato_A>votos_candidato_B:
        gana_candidato_A+=1
    else:
        gana_candidato_B+=1


print(f'La probabilidad del que el candidato A gane es de {gana_candidato_A/numeero_intentos:.2%}')
print(f'La probabilidad del que el candidato B gane es de {1-(gana_candidato_A/numeero_intentos):.2%}')

