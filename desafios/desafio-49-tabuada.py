"""
Refaça o desafio 9
mostrando a tabuada de um número
que usuário escolher, só que agora
utilizando o for
"""
num = int(input('Digite seu número para sua tabuada. '))
for contador in range(1, 11):
        # numero     interador     resultado
    print(f'{num} x {contador} = {num*contador}')
    contador = contador + 1
