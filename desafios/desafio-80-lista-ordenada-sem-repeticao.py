"""
Crie um programa onde o usúario possa
digitar cinco valores númericos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar sort())

No final, mostre a lista ordenada na tala
"""

lista = []

for count in range(0, 5):
    n = int(input('Digite um valor: '))
    if count == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados em ordem foram {lista}')