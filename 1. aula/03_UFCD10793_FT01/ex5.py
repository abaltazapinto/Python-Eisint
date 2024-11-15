import math


a = float(input("Introduza o valor do medida do comprimento do cateto 1:\n->"))

b = float(input("Introduza o valor do medida do comprimento do cateto 2:\n->"))

hipotenusa = math.sqrt(a**2+b**2)

print("A hipotenusa mede: ", round(hipotenusa,2))
