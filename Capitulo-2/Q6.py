# 6. A tabela a seguir fornece os descontos de uma compra. Fazer um programa em
# Python que leia o valor de uma compra, determine o desconto a ser aplicado e
# calcule o valor a ser pago pelo cliente. Imprimir o valor a ser pago com PRINT( ).

#         Tabela 1 – Descontos
# Valor da compra (R$)    Desconto (%)
# Entre 0 e 20                5
# Entre 21 e 50               10
# Entre 51 e 100              15
# Entre 101 e 1.000           20
# Maior que 1.000             30

valor_compra = float(input("Valor da compra: "))

if valor_compra <= 20:
    desc = 0.05
elif valor_compra <= 50:
    desc = 0.1
elif valor_compra <= 100:
    desc = 0.15
elif valor_compra <= 1000:
    desc = 0.2
else:
    desc = 0.3

valor_w_desconto = valor_compra * (1-desc)
print("Valor da compra com desconto = ", valor_w_desconto)