# 6. Abrir o arquivo bov.txt do exercício anterior no Console e imprimir o resultado
# dos elementos existentes nele.

file = open('files/bov.txt', 'r')

acoes = file.read()

print(acoes)

file.close()