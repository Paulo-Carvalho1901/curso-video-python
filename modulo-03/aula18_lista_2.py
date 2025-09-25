# mais sobre lista

teste = []
teste.append('Paulo')
teste.append(40)

galera = []
galera.append(teste[:]) # fazendo uma copia

teste[0] = 'Andreia'
teste[1] = 32
galera.append(teste[:]) # fazendo uma copia

print(galera)

grupo_pessoas = [['Andreia', 19], ['Davu', 10], ['Paulo', 11], ['Rosa', 22]]
# print(grupo_pessoas[0][0])
# print(grupo_pessoas[1][0])
# for pessoa in grupo_pessoas:
#     print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')


# criando duas lista e pedindo ao usuario que insira dados na mesma.

galera = []
dados = list()
