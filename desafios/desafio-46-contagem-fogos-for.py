"""
Faça um programa que mostre
ma tela uma contagem regressiva para o
estouro de fogos de artificio, indo de 10 até 0,
com uma pausa de 1 segundo entre elas

"""

import time
# from time import sleep 

print('-=-' * 20)
print('CONTAGEMN REGRESSIVA PARA VIRADA DE ANO')
print('-=-' * 20)

time.sleep(1)
for contador in range(10, -1, -1):
    time.sleep(1)
    print(contador)
print('BOM! BOM! FIM DE ANO CHEGOU VIVA 2025!!! 🎉 🎉 🎉 🎉')
    