"""
Crie um programa onde o usúario possa
digitar cinco valores númericos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar sort())

No final, mostre a lista ordenada na tala
"""

# def ordenar_lista_sem_sort(lista):
#     n = len(lista)
#     lista_ordenada = lista[:]  # Cria uma cópia da lista original para não modificá-la

#     for i in range(n):
#         # Encontra o índice do menor elemento no restante da lista
#         indice_menor = i
#         for j in range(i + 1, n):
#             if lista_ordenada[j] < lista_ordenada[indice_menor]:
#                 indice_menor = j

#         # Troca o menor elemento com o elemento na posição i
#         lista_ordenada[i], lista_ordenada[indice_menor] = lista_ordenada[indice_menor], lista_ordenada[i]

#     return lista_ordenada

# # Exemplo de uso:
# minha_lista = [5, 2, 8, 1, 9, 4]
# lista_ordenada = ordenar_lista_sem_sort(minha_lista)
# print(f"Lista original: {minha_lista}")
# print(f"Lista ordenada: {lista_ordenada}")


