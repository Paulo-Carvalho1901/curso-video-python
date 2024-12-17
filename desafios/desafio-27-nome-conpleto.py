"""
faça um programa que leia um nome completo
de uma pessoa, mostrando em seguinda o primeiro e o
último nome separadamente

"""

nome = str(input('Digite seu nome completo: ')).strip()
print(f'Muito prazer em te conhecer {nome}')
lista = nome.split()
print(f'Seu primeiro nome é {lista[0]}')
print(f'Seu último nome é {lista[-1]}')