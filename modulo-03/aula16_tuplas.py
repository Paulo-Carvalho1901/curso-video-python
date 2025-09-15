"""
Tuplas variaveis compostas
AS TUPLAS SÃO IMURAVEIS
Tuplas sintax = nome + (conteudo)
"""

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# print(lanche[1])
# print(lanche[-2])
# print(lanche[1:3])
# print(lanche[2:])
# print(lanche[:2])
# print(lanche[-2:])
# print(lanche[-3:])

# TypeError: 'tuple' object does not support item assignment
# lanche[1] = 'Refrigerante'# tuplas são imútaveis


# Iteração sobre as tuplas
# for comida in lanche:
    # print(f'Eu vou comer {comida}')


# for comida in lanche:
#     print(comida)


# for cont in range(0, len(lanche)):
#     print(cont, lanche[cont])


# for pos, comida in enumerate(lanche):
#     print(f'Comi muito {comida}, na posição {pos}')

# print(cont) # contador
# print(lanche) # tupla de lanche

# print(sorted(lanche))

a = (2, 5, 4)
b = (5, 2, 1, 2)
c = b + a

print(c)
print(len(c))
print(c.count(2)) # contar os itens
print(c.index(2)) # index utilizando para ver a posição da tupla

pessoa = ('Paulo', 36, 'M', 92.80)

print(pessoa)
