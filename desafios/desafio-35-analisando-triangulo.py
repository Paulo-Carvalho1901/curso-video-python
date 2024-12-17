"""
Desenvolva um programa que leia
o comprimento de três retas e diga ao
usuário se elas podem ou não 
formar um triângulo

"""
print('-=-'*20)
print('Analisador de triângulo')
print('-=-'*20)

r1 = float(input('Digite a reta1: '))
r2 = float(input('Digite a reta2: '))
r3 = float(input('Digite a reta3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo ')
else:
    print('Os seguimentos acima não podem forma um triânhulo')