"""

Faça um algoritimo que leia
o preso  de um produto e mostre seu
novo preço, com 5% de desconto

"""

preco = float(input('Digite o valor do produto R$: '))

preco_desconto = 0.05 * preco
valor_final = preco - preco_desconto

print(f'O preco do produto é R${preco} e preco com desconto é R${preco_desconto} valor final R${valor_final}')