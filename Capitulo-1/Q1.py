# 1. Usar a biblioteca correta e as funções matemáticas do Python, quando necessárias,
# para resolver as seguintes expressões:
import math

# (a) y = 43 − 22
print("\n(a) y = 43 − 22\n")

y = 43 - 22
print(y)

# (b) x = sen(2) − cos(4.2)
print("\n(b) x = sen(2) − cos(4.2)\n")

x = math.sin(2) - math.cos(4.2)
print(x)

# (c) z = cos(sen(3.7) − tan(1.3))
print("\n(c) z = cos(sen(3.7) − tan(1.3))\n")

z = math.cos(math.sin(3.7) - math.tan(1.3))
print(z)

# (d) Resto da divisão de 26 por 4.
print("\n(d) Resto da divisão de 26 por 4\n")

resto = 26 % 4
print(resto)

# (e) Converter x = 46.2° para radianos.
print("\n(e) Converter x = 46.2° para radianos\n")

x = math.radians(46.2)
print(x)

# (f) Converter y = 3.1 rad para graus.
print("\n(f) Converter y = 3.1 rad para graus\n")

y = math.degrees(3.1)
print(y)