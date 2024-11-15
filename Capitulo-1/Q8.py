# 8. Os dados a seguir representam os preços diários de fechamentos no pregão da
# Bovespa entre os meses de setembro e outubro de 2019. A coluna A do Excel se
# refere a VALE3 (Vale do Rio Doce) e a coluna B indica GGBR4 (Gerdau). Os dados
# estão em um arquivo Excel na planilha denominada Plan1.

# (imagem na questão)

# Deseja-se, então, que esses dados sejam importados para o Python com a biblioteca xlrd e que se responda aos itens a seguir.
import openpyxl
import numpy as np
import math
import matplotlib.pyplot as plt

# (a) Importar os dados do Excel e transformar a coluna A em uma variável que represente a Vale e a coluna B em outra variável que represente a coluna B.

file = openpyxl.load_workbook('files/bov_set_out_2019.xlsx')

sheet = file.active

col_a = [cell.value for cell in sheet['A']]
col_b = [cell.value for cell in sheet['B']]

VALE3 = [float(valor.replace(',', '.')) for valor in col_a]
GGBR4 = [float(valor.replace(',', '.')) for valor in col_b]

# (b) Transformar as variáveis em vetores usando a biblioteca numpy.

VALE3 = np.array(VALE3)
GGBR4 = np.array(GGBR4)

# (c) Fazer os dois gráficos dos preços da Vale e da Gerdau usando subplot. Colocar a Vale na parte superior da figura e a Gerdau na parte inferior.

fig, axs = plt.subplots(2, 1, figsize=(10, 8))
axs[0].plot(VALE3, label="Preço da Vale", color='blue')
axs[0].set_title("Preço da Vale")
axs[0].set_ylabel("Preço (R$)")
axs[0].legend()

axs[1].plot(GGBR4, label="Preço da Gerdau", color='green')
axs[1].set_title("Preço da Gerdau")
axs[1].set_ylabel("Preço (R$)")
axs[1].legend()

plt.savefig('files/grafico.png', dpi=300)
plt.close()

# (d) Calcular os retornos das duas empresas e plotar os quatro gráficos (preço da
# Vale e seu retorno; preço da Gerdau e seu retorno) no formato de uma matriz com 2×2 elementos.

retornos_vale = np.diff(np.log(VALE3))
retornos_gerdau = np.diff(np.log(GGBR4)) 

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs[0, 0].plot(VALE3, label="Preço da Vale", color='blue')
axs[0, 0].set_title("Preço da Vale")
axs[0, 0].set_ylabel("Preço (R$)")
axs[0, 0].legend()

axs[0, 1].plot(retornos_vale, label="Retorno da Vale", color='blue')
axs[0, 1].set_title("Retorno da Vale")
axs[0, 1].set_ylabel("Retorno")
axs[0, 1].legend()

axs[1, 0].plot(GGBR4, label="Preço da Gerdau", color='green')
axs[1, 0].set_title("Preço da Gerdau")
axs[1, 0].set_ylabel("Preço (R$)")
axs[1, 0].legend()

axs[1, 1].plot(retornos_gerdau, label="Retorno da Gerdau", color='green')
axs[1, 1].set_title("Retorno da Gerdau")
axs[1, 1].set_ylabel("Retorno")
axs[1, 1].legend()

plt.savefig('files/AnáliseGeral.png', dpi=300)
plt.close()