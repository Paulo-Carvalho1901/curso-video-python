# cont = 1
# while cont <= 10:
#     print(cont, '-> ', end=' ')
#     cont += 1
# print('Termino!')

# n = cont = 0
# while cont < 3:
#     n = int(input('Digite um número: '))
#     cont += 1

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999: # condicao de parada do loop
        break
    s += n
# s -= 999
print(f'A soma vale {s}')
