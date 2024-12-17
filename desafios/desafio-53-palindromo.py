"""
Crie um programa que leia
uma frase qualquer e diga se ela é
um palindromo, desconsiderando os espaços

EX:

APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARRATONA

"""

"""
Funções inportantes no poython
upper() para deixa todas as frases maiusculas
split() para deixa as palavras em listas separadas 
''.join() para tirar os espaços
.strip() para eliminar espaços antes e depois

"""

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
# inverso = junto[::-1] Fatiamento de string
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palimetro')