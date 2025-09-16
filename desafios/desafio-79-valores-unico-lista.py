"""
Crie uma programa que usúario possa digite
varios valores númericos e cadastra-os em uma
lista. Caso número já exista lá dentro. ele
não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
"""

# criando a lista vazia que sera populada
numeros = []

# criando um laço while, que terá uma condição de parada
while True:
    # solicitando ao usuario um valor inteiro
    n = int(input('Digite um valor: '))
    # checando se os numeros solicitados esta na lista
    if n not in numeros:
        numeros.append(n) # linha que adiciona os numeros na lista
        print('Número adicionado com sucesso!')
    else:
        print('Número duplicado, não vou adicionar!')
    