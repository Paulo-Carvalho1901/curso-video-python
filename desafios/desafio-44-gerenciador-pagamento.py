"""
Elabore um programa
que calcule o valor a ser pago por um
produto, considerando seu preço normal e 
condição de pagamento:

A vista dinheiro/cheque: 10% de desconto
A vista no cartão: 5% de desconto
em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros

"""
print(f'Lojas Carvalho')
total_compra = float(input('Digite o valor total de suas compras: '))

print('[ 1 ] A vista dineheiro/chque desconto de 10%: ')
print('[ 2 ] A vista no cartão desconto de 5%: ')
print('[ 3 ] 2x no cartão preço normal: ')
print('[ 4 ] 3x ou mais no cartão 20% de juros: ')
opcao = int(input('Escolha uma opção para pagamento: '))

if opcao == 1:
    desconto_10 = total_compra * 0.10
    print(f'Sua compra no dinheiro ou cheque será de: R${total_compra - desconto_10} reais com 10% de desconto.' )
elif opcao == 2:
    desconto_5 = total_compra * 0.05
    print(f'Sua compra avista no cartão será de: R${total_compra - desconto_5} reais com 5% de desconto.')
elif opcao == 3:
    parcela = total_compra / 2
    print(f'Sua compra será parcelada em 2x sem juros e sua parcela será R${parcela} reais e sua compra total será de R${total_compra} reais.')
elif opcao == 4:
    total_20 = total_compra + (total_compra * 20 / 100)
    total_pacelas = int(input('Quantas parcelas? '))
    parcela = total_20 / total_pacelas
    print(f'Será divido em {total_pacelas}x e o valor a ser pago das parcelas será de R${parcela:.2f}')
    print(f'Sua compra é de R${total_compra} reais e vai custar R${total_20} reais no final.')
else:
    opcao = 0
    print('Opção INVALIDA, porfavor tente novamento.')
    print(f'Sua compra será de R${total_compra} reais')