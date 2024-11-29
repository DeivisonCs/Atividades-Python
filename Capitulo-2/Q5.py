# 5. Considere uma equação do segundo grau:
# + += 2 Ax Bx C 0

# Utilizando-se ∆ = B A − C 2 4 , escrever um programa em Python que calcule as
# raízes da equação tal que:

# (I) Se não há raízes (Δ < 0), o programa retorna um PRINT “não existem raízes
# reais”.

# (II) Se há uma única raiz (Δ = 0), o programa mostra ao usuário a única raiz calcu-
# lada como: x1 = −B / (2*A).

# (III) Se há duas raízes, mostre ao usuário calculando-as desta forma:

# (!fórmula no livro)

import math as mt

a, b, c = float(input("A = ")), float(input("B = ")), float(input("C = "))

delta = b**2-4*a*c

if delta > 0:
    x1 = (-b + mt.sqrt(delta))/(2 * a)
    x2 = (-b - mt.sqrt(delta))/(2 * a)
    print("Raiz 1 = ", x1, "Raiz de 2 = ", x2)
    
elif delta == 0:
    x1 = -b/(2 * a)
    print(f"Raizes = {x1}")
    
else:
    print("Não existem raízes iguais.")