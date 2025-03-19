# Listas -  as listas são mutaveis
# criando uma lista
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

