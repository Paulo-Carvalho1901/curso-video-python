"""
Escreva um programa que leia um numero inteiro
qualquer e peça para o usuario escolher qual será a base de conversão

1 para binário
2 para octal
3 para hexadecimal

"""

numero = int(input('Digite um numero inteiro: '))
print('Escolha um número para conversão:')
print('[ 1 ] Converter em BINÁRIO ')
print('[ 2 ] Converter em OCTAL ')
print('[ 3 ] Converter em HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'numero {numero} convertido para BINÁRIO é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'Número {numero} convertido para OCTAL é {oct(numero)[2:]}')
elif opcao == 3:
    print(f'Número {numero} convertido para {hex(numero)[2:]}')
else:
    print('Você digitou uma opção invalida, favor digite apenas de 1 a 3.')

