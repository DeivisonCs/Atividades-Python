# 4. O “suporte” de uma ação é calculado como 30% do intervalo histórico de uma ação
# (máximo subtraído do mínimo). A “resistência” é calculada como o valor de 60%
# do intervalo histórico. Veja o exemplo:

# Baixa histórica: 1.50
# Alta histórica: 2.20
# Suporte: 1.5 + (2.20 – 1.50) * 0.3
# Resistência: 1.5 + (2.20 – 1.5) * 0.6

# Fazer um programa em Python em que o usuário forneça com input o valor mais
# baixo historicamente e o valor mais alto. O programa pede o valor atual da ação
# também com input e diz com PRINT( ) qual é o suporte, qual é a resistência e se o
# preço da ação está dentro da faixa de suporte-resistência ou fora dela.

baixa = float(input("Digite o preço da baixa histórica: "))
alta = float(input("Digite o preço da alta histórica: "))
preco_atual = float(input("Digite o preço atual do ativo: "))

suporte = baixa + (alta - baixa) * 0.3
resistencia = float(baixa + (alta - baixa) * 0.6)

print("Resistência: %.2f " % resistencia)
print("Suporte %.2f " % suporte)

if preco_atual <= resistencia and preco_atual >= suporte:
    print("O preço R$%.2f está dentro da faixa de suporte-resistência." % preco_atual)
else:
    print("O preço do ativo R$%.2f está fora da faixa de suporte-resistência." % preco_atual)