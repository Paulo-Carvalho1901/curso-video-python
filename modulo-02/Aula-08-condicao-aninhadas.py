#Estrutura condicional aninhadas if else e elif

nome = str(input('Digite seu nome:'))
if nome == 'Paulo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é popular no brasil')
elif nome in 'Ana Julia Jessica Andreia':
    print('Belo nome femonino!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}')