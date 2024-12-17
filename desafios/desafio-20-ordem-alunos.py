"""
O mesmo professor do desafio anterior
quer sortear a ordem de apresentação de
trabalhos de alunos, Faça um programa
que leia o nome dos quatro alunos
e mostre a ordem sorteada

"""
import random
from random import shuffle

n1 = str(input('Digite o nome do aluno 1: '))
n2 = str(input('Digite o nome do aluno 2: '))
n3 = str(input('Digite o nome do aluno 3: '))
n4 = str(input('Digite o nome do aluno 4: '))

lista = [n1,n2,n3,n4]
random.shuffle(lista)

print('A ordem dos da apresentação dos aluno será: ')
print(lista)

