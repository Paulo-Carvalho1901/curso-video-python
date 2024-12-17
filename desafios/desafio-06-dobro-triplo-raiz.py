"""
Crie um algoritmo que leia um número e
mostre seu dobro triplo e raiz quadrada

"""
n = int(input('Digit um número: '))

d = n * 2 
t = n * 3
r = n ** (1/2)

print(f'0 dublo do numero é {d} o triplo do número é {t} a raiz do número é {r:.2f}')