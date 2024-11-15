# 4. Criar a lista com nomes das bolsas de valores do mundo: 
# Bolsas = [‘dow’, ‘ibov’, ‘ftse’, ‘dax’, ‘nasdaq’, ‘cac’]. 
BOLSAS = ["dow", "ibov", "ftse", "dax", "nasdaq", "cac"]
BS = ["hong kong", "merval"]

# Fatiá-la conforme os itens a seguir.

# (a) Selecionar as três primeiras.
print("\n(a) Selecionar as três primeiras\n")

sub_a = BOLSAS[:3]
print(sub_a)

# (b) Incluir a sublista Bs = [‘hong kong’, ‘merval’] na lista anterior.
print("\n(b) Incluir a sublista Bs = [‘hong kong’, ‘merval’] na lista anterior\n")

sub_b = sub_a[:]
sub_b.extend(BS)
print(sub_b)

# (c) Descobrir qual o índice da ‘nasdaq’.
print("\n(c) Descobrir qual o índice da ‘nasdaq’\n")

nasdaq_idx = BOLSAS.index('nasdaq')
print(nasdaq_idx)

# (d) Remover ‘cac’ da lista.
print("\n(d) Remover ‘cac’ da lista\n")

BOLSAS.remove('cac')
print(BOLSAS)

# (e) Inserir “sp&500” como índice 2 na lista de bolsas, mas sem excluir nenhum elemento já inscrito.
print("\n(e) Inserir “sp&500” como índice 2 na lista de bolsas, mas sem excluir nenhum elemento já inscrito\n")

BOLSAS.insert(2, 's&p500')
print(BOLSAS)