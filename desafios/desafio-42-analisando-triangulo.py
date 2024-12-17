"""
Refaça o desafio 035 dos triânhulos
acrescentando o recurso de mostrar
que tipo de triângulo será formado

Equilátero: todos os lados iguais
Isóscelos: dois lados iguais
Escaleno: todos os lados diferentes
"""

print('-' * 35)
print('Analisando lado os triângulos')
print('-' * 35)
print('-' * 35)
print()

l1 = int(input('Digite o lado1 do triângulo: '))
l2 = int(input('Digite o lado2 do triângulo: '))
l3 = int(input('Digite o lado3 do triângulo: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os lados acima podem forma um TRIÂNGULO.')
    if l1 == l2 == l3:
        print('Esse valores formarão um TRIÂNGULO EQUILÁTERO. ')
    elif l1 == l2 != l3:
        print('Esse valores formarão um TRIÂNGULO ISÓSCELOS. ')
    elif l1 != l2 != l3:
        print('Esses valores formarão um TRIÂNGULO ESCALENO. ')
else:
    print('Os lados acima não podem formar um TRIÂNGULO.')
