"""
Operadores aritiméticos

+ adição
- subtração
* multiplicação
/ divisão
** potencia
// divisão inteiro
% modulo, resto da divisão

"""

adicao = 5 + 2 
subtracao = 5 - 2
multiplicacao = 5 * 2
divisao = 5 / 2
potencia = 5 ** 2
divisao_inteira = 5 // 2
resto = 5 % 2

# print(adicao)
# print(subtracao)
# print(multiplicacao)
# print(divisao)
# print(potencia)
# print(divisao_inteira)
# print(resto)


"""
Ordem de precedencia dos operadores

1° () = parentes
2° ** = potencias
3° * / // % = multiplicação, divisão, divisão inteira, resto
4° + - = adição, subtração

"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n2 // n2
e = n1 ** n2
print(f'A soma é {s}, o produto é {m}\n e a divisão é {d:.3f}' )
print(f'divisao inteira {di} e potencia {e}')


