# Listas -  as listas são mutaveis
# criando uma lista

num = [2, 5, 9, 1] # lista
num[2] = 3 # adicionando intem na lista
num.append(7) # adicionando item na lista utilmo indice
num.sort(reverse=True) # revertendo a ordem da lista
num.insert(2, 2) # inserindo item na lista de acordo com indice
# num.pop(2) # removendo item na lista de acordo com indice e se não for passado indice remove o ultimo elemento
# num.remove(4) # remove ele procura do inicio na lista aprimeira ocorrencia e remove
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4!')
print(num)
# print(f'Essa lista tem len{num} elementos.')

print()

palavras = ['programar', 'computador', 'trabalho', 'tecnologia']
	
# alterando uma lista
palavras[0] = 'programação'
print(palavras)

# adicionar algo na lista no final da lista
palavras.append('teclado')
print(palavras)

# inserindo itens em qualquer parte da lista
palavras.insert(0, 'monitor')
print(palavras)

# apagando itens da lista
del palavras[0]
print(palavras)
palavras.pop()# metodo pop apaga o ultimo item da lista
print(palavras) 
palavras.remove('programação') # indicando o valor a ser eliminado
print(palavras)

valores = list(range(4, 11))
print(valores)

# ordenando metodo sort
lista = [8, 2, 5, 4, 9, 3, 0]
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
print(len(lista))

print()
print('Novos valores da lista')

valores = []

# for count in range(0, 5):
#     # valores.append(int(input('Digite os valores para lista: ')))

# # valores.append(5)
# # valores.append(9)
# # valores.append(4)

# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Cheguei ao final na lista!')

print()

a = [2, 3, 4, 7]
b = a[:]

b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
