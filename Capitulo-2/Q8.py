# 8. O financiamento de um automóvel foi contratado respeitando a série matemática a
# seguir para 70 meses. Criar um algoritmo em Python para calcular a soma seguinte
# até o termo n que o usuário desejar, seguindo a lógica a seguir.

# (!fórmula no livro)

meses = int(input("Mês: "))
sum = 0

for i in range(1, meses + 1):
    sum += (70 - i +1)/(7 * i)

print("Soma: ", sum)