# import math
# num = int(input('Digite um número: '))
# raiz = math.sqrt(num)
# print(f'A raiz do {num} o resultado é {math.ceil(raiz)}')

#função ciel arredondamento para cime
#função floor arredondamento para baixo

from math import sqrt

num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz do número {num} o resultado é {raiz:.2f}')

