"""
Desenvolva um programa que leia
o nome, idade e sexo de 4 pessoas
no final do programa mostre:

A media de idade do grupo

Qual o nome do homem mais velho

Quantas mulheres tem menos de 20 anos

"""
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for cont in range(1, 5):
    print('-=-'*10)
    print(f'Analise da {cont}° pessoa. ')
    print('-=-'*10)
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input(f'Digite sua idade: '))
    sexo = str(input('Digite o sexo [F/M]: ')).strip()
    somaidade += idade 

    if cont == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho =  nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem =  idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
        
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} e se chamma {nomevelho}')
print(f'Ao todo são {totmulher} mulheres com menos de 20 anos. ')