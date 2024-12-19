"""
Faça um programa que leio o sexo
de uma pessoa, nas só aceita os valores
F ou M.
Caso esteja errado peça a digitação
novamente até ter um valor correto

"""
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
