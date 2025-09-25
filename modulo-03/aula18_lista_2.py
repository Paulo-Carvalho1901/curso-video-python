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

# solicitando dados ao usuario com for
total_maior = total_menor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:]) # fazendo uma copia raza dos dados em galera
    dados.clear()
print(galera)

# exibindo com condicionais

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor += 1

print(f'Temos {total_maior} maiore e {total_menor} menor de idade')
