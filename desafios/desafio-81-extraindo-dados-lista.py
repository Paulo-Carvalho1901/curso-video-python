"""
Crie uma programa que vai ter vários números
e colocar em uma lista

depois disso, mostre:

A) Quantos números foram digitados

B) A lista de valores, ordenadas de forma decrecente

C) Se o valor 5 foi digitada e está ou não na lista

"""

numeros = []

while True:
        numeros.append(int(input('Digite um valor: ')))
        pergunta = str(input('Deseja continuar? [S/N]: '))
        if pergunta in 'Nn':
            break
print('=-' * 30)
print(f'Você digitou {len(numeros)} elementos')
numeros.sort(reverse=True)
print(f'A lista em ordem decrescente são {numeros}')
if 5 in numeros:
    print('Números 5 está na lista.')
else:
    print('Números 5 não esta na lista.')