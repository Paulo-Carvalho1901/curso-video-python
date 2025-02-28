"""
Crie um programa 
que tenha uma tupla
totalmente preenchida com uma contagem por
extenso de zero a vinte

seu programa deverá ler números pelo teclado
(entre 0 e 20) e mostra-lo por extenso

"""

# inserindo uma tupla
count = ('zero', 'un', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nova', 
         'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesete', 'dezoito', 'dezenove', 'vinte')

# solicitando o números ao usuario e criando a condição de parada
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')

# número por extenso
print(f'Você digitou um número {count[num]}')