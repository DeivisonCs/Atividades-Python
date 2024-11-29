# 3. Um website de compras deseja deixar um link para os franqueados entrarem com o
# valor de compra de um produto no input e o valor de venda no input e descobrir se
# o lucro foi menor que 10%, entre 10% e 20%, ou superior a 20%. Para tanto, deve-se
# fazer um programa em Python que imprima a mensagem com PRINT( ) dizendo
# em qual faixa a mercadoria do comerciante se localiza.

preco_compra = int(input("Digite o preço de compra: "))
preco_venda = int(input("Digite o preço de venda: "))

lucro = ((preco_venda - preco_compra) / preco_compra) * 100

if lucro > 0 and lucro < 10:
    print("Lucro é menor que 10%.")

elif lucro >= 10 and lucro <= 20:
    print("Lucro é está entre 10% e 20%.")

elif lucro > 20:
    print("Lucro é maior que 20%.")

else:
    print("Venda deu prejuizo.")