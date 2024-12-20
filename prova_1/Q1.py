# 1) Sabendo-se que a UAL calcula a divisão através de subtrações sucessivas, criar um
# programa que calcule e imprima o resto da divisão de números inteiros lidos. suponha
# que os números lidos sejam positivos e que o dividendo seja maior que o divisor.

dividendo, divisor = int(input("Dividendo: ")), int(input("Divisor: "))

inteiro = 0
resto = 0

while dividendo > 0:
    dividendo -= divisor

    inteiro += 1

    if(dividendo<divisor):
        break

resto = dividendo

print(f'''
Inteiro: {inteiro}
Resto: {resto}''')