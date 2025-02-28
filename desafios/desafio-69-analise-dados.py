"""
crie um programa que leia a idade e o sexo de varias pessoas
a cada pessoa cadastrada, o programa deverá perguntar se o usuario
quer ou não continuar. No final, mosttre:

a) quantas pessoas tem mais de 18 anos
b) quanrtos homens foram cadastrados
c) quantas mulheres tem menos de 20 anos
"""
while True: # Criando loop infinito
    idade = int(input('Digite sua idade: '))
    sexo = '' # variavel vazia
    while sexo not in 'MF': # condição criada para validar o sexo
        sexo = str(input('Digite seu sexo [F/M]')).strip().upper()[0] # solicitando o sexo apenas a primeira letra

    resp = ''
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    

