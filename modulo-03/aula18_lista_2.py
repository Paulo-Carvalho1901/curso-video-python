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
print(grupo_pessoas)