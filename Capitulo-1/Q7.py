# 7. Observar a seguinte lista de dados, 
# lista= [2, 2, 3, 3, 3, −1, −1, −2, 0, 0, 0, 2, 4, 5, 1, 2, 2, 0, 0, 0,2 ,1, 5, 5, 7, 6, 5, 0, 0].
lista= [2, 2, 3, 3, 3, -1, -1, -2, 0, 0, 0, 2, 4, 5, 1, 2, 2, 0, 0, 0,2 ,1, 5, 5, 7, 6, 5, 0, 0]

# Programar o Console para encontrar as seguintes medidas estatísticas:
import statistics as st

# (a) Soma de todos os elementos.
print("\n(a) Soma de todos os elementos\n")

sum = sum(lista)
print(sum)

# (b) Máximo elemento da lista.
print("\n(b) Máximo elemento da lista\n")

max = max(lista)
print(max)

# (c) Mínimo elemento da lista.
print("\n(c) Mínimo elemento da lista\n")

min = min(lista)
print(min)

# (d) Média dos elementos da lista.
print("\n(d) Média dos elementos da lista\n")

media = st.mean(lista)
print(media)

# (e) Mediana dos elementos da lista.
print("\n(e) Mediana dos elementos da lista\n")

mediana = st.median(lista)
print(mediana)

# (f) Moda dos elementos da lista.
print("\n(f) Moda dos elementos da lista\n")

moda = st.mode(lista)
print(moda)

# (g) Desvio-padrão amostral.
print("\n(g) Desvio-padrão amostral\n")

desvio_pttr = st.stdev(lista)
print(desvio_pttr)

# (h) Desvio-padrão populacional.
print("\n(h) Desvio-padrão populacional\n")

desvio_ppl = st.pstdev(lista)
print(desvio_ppl)

# (i) Contar o número de vezes que aparece o número 0.
print("\n(i) Contar o número de vezes que aparece o número 0\n")

qtd_0 = lista.count(0)
print(qtd_0)

# (j) Contar o número de vezes que aparece o número 5.
print("\n(j) Contar o número de vezes que aparece o número 5\n")

qtd_5 = lista.count(5)
print(qtd_5)

# (k) Ordenar a lista em ordem crescente.
print("\n(k) Ordenar a lista em ordem crescente\n")

lista.sort()
print(lista)

# (l) Ordenar a lista em ordem decrescente.
print("\n(l) Ordenar a lista em ordem decrescente\n")

lista.sort(reverse=True)
print(lista)