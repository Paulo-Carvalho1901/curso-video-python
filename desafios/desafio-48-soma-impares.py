"""
Faça um programa que calcule a soma entre todos os 
números impares que são multiplos de três e que se encontram
no intervalo de 1 até 500
"""
soma = 0 # VARIAVEL PARA ACUMULAR VALOR
cont = 0 # VARIAVEL PARA CONTAR SUA ITERAÇÃO

for contador in range(1, 501, 2): # ITERAÇÃO
    if contador % 3 == 0: # TESTANDO A CONDIÇÃO NESSE CASO SE O RESTO DA DIVISÃO POR 3 É IGUAL A ZERO NÚMEROS IMPARES
        cont += 1 # CONTANDO QUANTAS VEZES - CONTADOR GERALMENTE SOMA +1
        soma += contador # FAZENDO O CALCULO DO VALOR - ACUMULADOR GERALMENE SOMA UM VALOR
print(f'O número de vezes foi calculados foram {cont}')
print(f'O resultado da soma de todos os valores é {soma}') # APRESENTANDO RESULTADO NA TELA
    