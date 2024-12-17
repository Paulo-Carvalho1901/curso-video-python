"""
Faça um programa que leia a largura
e a altura de uma parede
em metros, calcule a sua área e a
quantidade de tinta necessaria para
pinta-la, sabendo que cada litro
de tinta, pinta uma área de 2m2

"""
largura_parde = float(input('Digite a largura da parede: '))
altura_parede = float(input('Digite a altura da parede: '))
area = altura_parede * largura_parde

qtd_tinta = area / 2

print(f'Sua parede tema dimensão {largura_parde}x{altura_parede} e a sua área é de {area}m2')
print(f'Para pinta essa parede você precisa-ra de {qtd_tinta}l de tinta')



