"""
Crie um programa que leia o nome de pessoa e diga
se ela tem 'Silva' no nome

"""

nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome tem a palavra silva? {'SILVA' in nome.upper()}') 