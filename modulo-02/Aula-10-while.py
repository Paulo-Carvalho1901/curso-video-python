# for c in range(1, 10):
#     print(c)
# print('Fim')

# for c in range(1, 5):
#     n = int(input('Digite um valor: '))
# print('Fim')

# ESTRUTURA BASICA WHILE

# c = 1
# while c < 10:
#     print(c)
#     c += 1
# print('Fim')

# r = 'S'
# while r == 'S':
#     n = int(input('Digite um númnero: '))
#     r = str(input('Quer continuar? [S/N] ')).upper()
# print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Voce digitou {par} números pares e {impar} números impares. ')