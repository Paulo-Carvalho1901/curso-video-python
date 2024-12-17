"""

Tratamento de string

"""

frase = 'Curso em video Python'
print((frase.replace('Python', 'Android')))
print(frase)
print('Curso' in frase)
print(frase.lower().find('video'))
print(frase.split())
print(frase.strip())

dividido = frase.split()
print(dividido[2][3])