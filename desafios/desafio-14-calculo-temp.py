"""
Esvreva um programa que converta uma temperatura
digitada em °C e converta em F

"""

grau_c = float(input('Digite a temperatura em °C: '))
grau_f = grau_c * 1.8 + 32

print(f'A temperatura convertida de {grau_c}°C é de {grau_f:.2f}F ')
