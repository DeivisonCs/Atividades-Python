# 2. Assumir como constante no comando de linha do Python x = 3 e y = 6 e imprimir
# usando PRINT( ) o resultado das equações seguintes:
import math

X = 3
Y = 6

# (a) w = e^x − ln(y)
print("\n(a) w = e^x − ln(y)\n")

w = math.exp(X) - math.log(Y)
print(w)

# (b) z = x*y^2 + y*cos(x)
print("\n(b) z = x*y^2 + y*cos(x)\n")

z = X * math.pow(Y, 2) + Y * math.cos(X)
print(z)

# (c) s = √(x/2) + ln(x+y) + tan(x)
print("\n(c) s = √(x/2) + ln(x+y) + tan(x)\n")

s = math.sqrt((X/2) + math.log(X+Y) + math.tan(X))
print(s)