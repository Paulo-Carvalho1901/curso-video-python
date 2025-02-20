"""
Refaça o desafio 51, lendo o primeiro
termo e a razao de uma PA, mostrando 10 primeiros termos da 
pregressão usando a estrutura while
"""
print('Gerador de PA')
print('=-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f' -> {termo}', end=' ')
    termo += razao
    cont += 1
print('Fim')
