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
    n = int(input('Digite o valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Não adionado com sucesso')
        pergunta = str(input('Deseja continuar? [S/N]: '))
        if pergunta in 'Nn':
            break
print(numeros)