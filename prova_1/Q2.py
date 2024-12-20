# 2) Na usina de Angra dos Reis, os técnicos analisam a perda de massa de um material
# radioativo. Sabendo-se que este perde 25% de sua massa a cada 30 segundos, criar um
# programa que imprima o tempo necessário para que a massa deste material se torne
# menor que 0,10 gramas. O programa pode calcular o tempo para várias massas.

MASSAS = {'Uranio':100, 'Plutonio':12.2, 'Politicagem':1, 'Césio':1}
TEMPO = {'Uranio':0, 'Plutonio':0, 'Politicagem':0, 'Césio':0}


for i in MASSAS:
    sec = 0
    material = MASSAS[i]
    
    while material >= .10:
        material -= material * .25
        sec += 30

    TEMPO[i] = sec

print(f'Tempo: {TEMPO}')


# MASSAS = [100, 12.2, 1, 2, 5.5]
# tempo = [0, 0, 0, 0, 0]
# index = 0

# while index < len(MASSAS):
#     sec = 0
#     material = MASSAS[index]

#     while material >= .10:
#         material -= material * .25
#         sec += 30

#     tempo[index] = sec
#     index += 1

# for i in tempo:
#     print(f'Tempo Material {tempo.index(i)+1}: {i}')