"""
Tuplas variaveis compostas
AS TUPLAS SÃO IMURAVEIS
Tuplas sintax = nome + (conteudo)
"""

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])
print(lanche[-2])
print(lanche[1:3]) # efetuando fatiamento
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])

# TypeError: 'tuple' object does not support item assignment
# lanche[1] = 'Refrigerante'# tuplas são imútaveis


# Iteração sobre as tuplas
# for comida in lanche:
    # print(f'Eu vou comer {comida}')
print(len(lanche))
