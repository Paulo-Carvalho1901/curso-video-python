"""
Crie um programa 
que leia dois valores e mostre um menu
na tela

[1] somar
[2] multipllicar
[3] maior
[4] novos números
[5] sair do programa
 
seu programa deverá
realizar a operação solicitando em casa caso
"""
from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa
    ''')
    opcao = int(input('Qual é sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma dos números {n1} e {n2} = {soma}')
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação dos números {n1} e {n2} = {multiplicar}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior numero entre {n1} e {n2} é {maior}')
    elif opcao == 4:
        print('Informe os números novamente!')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Fizalizando o programa....')
    else:
        print('Opção invalida tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')