# TRABALAHNDO COM CORES NO TERMINAL EM PYTHON
# ANSI ESCAPE SEQUENCE
# \033[m

"""
CÓDIGOS DE ESTILOS
0 - none - sem estilo
1 - bold - negrito
4 - Sublinhado
7 - Inverter
"""

"""
COR DE TEXTO
30 - BRANCO
31 - VERMELHO
32 - VERDE
33 - AMARELO
34 - AZUL
35 - ROXO
36 - AQUAMARINHO
37 - CINZA
"""

"""
COR DE BACKGROUND
40 - BRANCO
41 - VERMELHO
42 - VERDE
43 - AMARELO
44 - AZUL
45 - ROXO
46 - AQUAMARINHO
47 - CINZA
"""

print('\33[0;31mOlá, mundo\33[m')
print('\33[0;32mOlá, mundo\33[m')
print('\33[0;33mOlá, mundo\33[m')
print('\33[0;34mOlá, mundo\33[m')
print('\33[0;35mOlá, mundo\33[m')
print('\33[0;36mOlá, mundo\33[m')
print('\33[0;37mOlá, mundo\33[m')

print('\33[0;31;41mOlá, mundo\33[m')
print('\33[0;32;42mOlá, mundo\33[m')
print('\33[0;33;43mOlá, mundo\33[m')
print('\33[0;34;44mOlá, mundo\33[m')
print('\33[0;35;45mOlá, mundo\33[m')
print('\33[0;36;46mOlá, mundo\33[m')
print('\33[0;37;47mOlá, mundo\33[m')

print('\33[1;32mOlá, mundo\33[m')
print('\33[4;33mOlá, mundo\33[m')
print('\33[7;40mOlá, mundo\33[m')