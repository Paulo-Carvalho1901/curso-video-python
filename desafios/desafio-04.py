"""
Faça um programa que leia algo pelo taclado
e mostre na tela  o seu tipo
primitivo e todos as informações possiveis 
sobre ela

"""
n = input('Digite alguma coisa: ')

print('O tipo primeitivo desse valor é? ', type(n))
print('Esse valor não contem espaços? ', n.isspace())
print('É um número? ', n.isnumeric())
print('É alfabético? ', n.isalpha())
print('É alnumerico? ', n.isalnum())
print('Contem maiuscula? ',n.isupper())
print('Contem minuscula? ', n.islower())
print('Está capitalizada? ', n.istitle())





