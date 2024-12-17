"""
Faça um programa que leia a ano de nascimento de um jovem
e informe de acordo com sua idade

Se ele ainda vai se alistar ao serviço militar
Se é a hora de se alistar
Se já passou do tempo do alistamento

Seu programa também deverá mostrar o 
tempo que falta ou que passou do prazo

"""
from datetime import date
from datetime import datetime
import time
# atual = date.today().year - linha de código para se pegar o ano atual na máquina

nascimento = int(input('Informe seu ano de nascimento: '))
print('Porfavor aguarda para ver se seu status de alistamento para as forças armadas.')
print('Aguarde...')
time.sleep(3)

alistar = 2024 - nascimento

if alistar <= 17:
    print(f'Você está com {alistar} anos Ainda falta {18 - alistar} anos, não está na hora de se alista.')
elif alistar == 18:
    print(f'Está com {alistar} anos está na hora do alistamento PARABÉNS!.')
elif alistar >= 19:
    print(f'Você está coom {alistar} anos, ja passou {alistar - 18} anos do alistamento apresentese ao QG para justificativa.')
