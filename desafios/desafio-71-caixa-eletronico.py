"""
Crie um programa que simule funcionamento de um caixa eletronico
no inicio perhunte ao usuario qual será o valor a ser sacado
(números inteiro) e o programa vai imformar quantas cedulas de cada valor serão
entregues

OBS: Considere que o caixa possui cédulas 
de R$50, R$20, R$10 e R$1

"""
print('=' * 30)
print('Banco caixa eletronico')
print('=' * 30)

valor = int(input('Qual o valor do saque? R$. '))
total = valor 
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        print(f'Total {total_ced} cédulas de R${ced} reais.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break    
        