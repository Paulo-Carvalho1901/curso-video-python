"""
Crie um programa 
que tenha uma tupla
totalmente preenchida com uma contagem por
extenso de zero a vinte

seu programa deverá ler números pelo teclado
(entre 0 e 20) e mostra-lo por extenso

"""

# inserindo uma tupla
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nova', 
         'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesete', 'desessete', 'dezoito', 'dezenove', 'vinte')

# solicitando o números ao usuario e criando a condição de parada
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente. ', end=' ')
print(f'Você digitou um número {cont[numero]}')
