"""
Crie um programa que leia
o nome completo de uma pessoae mostre:

o nome com todos as letras maiusculas

o nome com todas as letras minusculas

quantas letras ao todo sem considerar os espaços

quantas letra tem o primeiro nome

"""

nome = str(input('Digite seu nome completo: ')).strip()
nome_sem_espaco = nome.replace(" ", "")
numero_caractere = len(nome_sem_espaco) 

print(nome.upper())
print(nome.lower())
print(f'O nome completo {nome} tem {numero_caractere} caracteres')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')
