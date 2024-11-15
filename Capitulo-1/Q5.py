# 5. Abrir um arquivo chamado bov.txt e salvar os dados 
# das siglas das ações e seus valores na seguinte ordem: 
# ‘petr4’, ‘vale3’, ‘ggbr4’, 28.4, 31.3, 15.76.

ACOES = ['petr4', 'vale3', 'ggbr4', 28.4, 31.3, 15.76]

file = open('files/bov.txt', 'w')
file.write(f'{ACOES[:]}')
file.close()