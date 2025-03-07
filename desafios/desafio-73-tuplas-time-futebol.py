"""
Crie uma tupla preenchida com os 20
primeiros colocados na tabela do
campeonato brasileiro de futebol,
na ordem colocação 
depois mostre:

a) Apenas os 5 primeiros colocados
b) Os últimos 4 colocados na tabela
c) Uma lista com os times em ordem 
alfabetica
d) Em que posição na tabela está
o time de chopecoense
"""
times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio',
        'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
        'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
        'São Paulo', 'Fluminense', 'Sport Recife',
        'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
        'Atlético-GO')

print(f'Lista de time {times}')

print()

print('Os primeiros 5 colocados são: ')
primeiro_colocado = times[0:5]
for cinco_colocados in primeiro_colocado:
    print(cinco_colocados)

print()

print('Os 4 últimos colocados na tabela são')
quatro_ultimos_colocados = times[-4:]
print(quatro_ultimos_colocados)

print()

print('Uma lista de times em ordem alfabetica são: ')
ordem_times = sorted(times)
for ordem in ordem_times:
    print(ordem)

print()

print(f'O chapecoense está na {times.index('Chapecoense')} posição.')
