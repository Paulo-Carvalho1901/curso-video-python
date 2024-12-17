"""
Estrutura de condições

"""

# nome = str(input('Digite seu nome: ')).strip()
# if nome == 'Paulo':
#     print('Oh, seja Bem vindo meu padrão!')
# else:
#     print('Seu nome é tão normal')
# print(f'Bom dia! {nome}')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2
print(f'A sua media foi {m:.1f} ')


if m >= 6.0:
    print('Aluno aprovado, PARABÉNS!')
else:
    print('Aluno reprovado, estude mais!')

