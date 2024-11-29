# 2. Dados três lados de um triângulo qualquer, fazer um programa para descobrir se
# o triângulo é equilátero, isósceles ou escaleno. Entrar com os valores com input.

lado_1, lado_2, lado_3 = float(input("Lado 1 = ")), float(input("Lado 2 = ")), float(input("Lado 3 = "))

if lado_1 == lado_2 == lado_3:
    print("Equilátero")
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print("Isósceles")
else:
    print("Escaleno")