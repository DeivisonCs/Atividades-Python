# 3. Criar a lista de números num=[3, 3, 4, 1, 2, 1, 1, 2, 3, 4, 4, 1, 1, 5, 2] e fatiá-la conforme os itens a seguir:

NUM = [3, 3, 4, 1, 2, 1, 1, 2, 3, 4, 4, 1, 1, 5, 2]

# (a) Fatiar do elemento de índice 2 ao de índice 3.
print("\n(a) Fatiar do elemento de índice 2 ao de índice 3\n")

sub_a = NUM[2:4]
print(sub_a)

# (b) Fatiar do quinto elemento ao nono elemento.
print("\n(b) Fatiar do quinto elemento ao nono elemento\n")

sub_b = NUM[4:8]
print(sub_b)

# (c) Fatiar do elemento de índice 1 ao último.
print("\n(c) Fatiar do elemento de índice 1 ao último\n")

sub_c = NUM[1:]
print(sub_c)

# (d) Fatiar do primeiro elemento ao último.
print("\n(d) Fatiar do primeiro elemento ao último\n")

sub_d = NUM[:]
print(sub_d)

# (e) Fatiar do primeiro elemento ao último saltando de três em três elementos.
print("\n(e) Fatiar do primeiro elemento ao último saltando de três em três elementos\n")

sub_e = NUM[::3]
print(sub_e)

# (f) Selecionar o último elemento da lista.
print("\n(f) Selecionar o último elemento da lista\n")

sub_f = NUM[-1]
print(sub_f)

# (g) Selecionar os três últimos elementos da lista.
print("\n(g) Selecionar os três últimos elementos da lista\n")

sub_g = NUM[-3:]
print(sub_g)

# (h) Selecionar os quatro primeiros elementos da lista.
print("\n(h) Selecionar os quatro primeiros elementos da lista\n")

sub_h = NUM[:4]
print(sub_h)

# (i) Contar o número de elementos da lista.
print("\n(i) Contar o número de elementos da lista\n")

sub_i = len(NUM)
print(sub_i)

# (j) Contar quantas vezes aparece o número 1 na lista.
print("\n(j) Contar quantas vezes aparece o número 1 na lista\n")

sub_j = NUM.count(1)
print(sub_j)