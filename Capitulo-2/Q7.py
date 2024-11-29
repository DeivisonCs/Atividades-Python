# 7. Uma loja de departamentos de roupas de cama e banho percebeu que, se separar seu
# servidor de vendas em pedidos pares e ímpares, o atendimento fica mais ágil. 

# Fazer um algoritmo em Python em que se deve ler o número que representa o total de vendas n
# de uma sequência de números naturais e, posteriormente, ler a própria sequência com
# input. Armazenados os números da sequência, o programa deve mostrar com PRINT( )
# o valor da soma dos números pares (SP) e o valor da soma dos números ímpares (SI).

total_vendas = int(input("Total de vendas: "))

sp = 0
si = 0

for i in range(total_vendas):
    x = int(input(f"Digite o número {i+1}: "))
    
    if x % 2 == 0:
        sp += x
    else:
        si += x

print(f"Soma dos números pares (SP): {sp}")
print(f"Soma dos números ímpares (SI): {si}")