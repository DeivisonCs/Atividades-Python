# 3) Faça um programa que calcule o menor número possível de notas (cédulas) que um
# valor, inserido pelo usuário, pode ser decomposto. As notas consideradas são de 100,
# 50, 20, 10, 5, 2 e 1.

NOTAS = [100, 50, 25, 10, 5, 2, 1]
VALOR = int(input("Insira a cédula: "))
QTD = [0, 0, 0, 0, 0, 0, 0]

resto = VALOR
index = 0
while resto > 0:
    nota_atual = NOTAS[index]
    
    if(nota_atual <= resto):
        resto -= nota_atual
        QTD[index] += 1

    elif nota_atual/2 >= 1:
        index += 1
        nota_atual = NOTAS[index]


for i in range(len(NOTAS)):
    print(f'Nota {NOTAS[i]}: {QTD[i]}x')