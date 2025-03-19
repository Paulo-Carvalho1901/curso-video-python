""""
Crie um programa que tenha uma tupla com varias palavras
(não usar acentos) depois disso,
voce deve mostrar, para cada palavra,
quais são as suas vogais
"""

palvras = ('aprender', 'linguagem', 'programar', 'python',
           'curso', 'gratis', 'estudar', 'pratica', 
           'trabalhar', 'mercado', 'programador', 'futuro')

for p in palvras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
