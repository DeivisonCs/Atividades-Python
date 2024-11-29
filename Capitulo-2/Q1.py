# 1. Fazer algoritmo e programa em Python: o usuário entra com um número usando
# input e o programa imprime com PRINT( ), se o número é positivo ou negativo.

input_num = int(input("Digite um número: "))

if input_num < 0:
    print("Número digitado é negativo")
else:
    print("Número digitado é positivo")