"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
Valor_de_A = float(input("digite um valor para a letra A: "))
Valor_de_B = float(input("digite um valor para a letra B: "))
Valor_de_C = float(input("digite um valor para a letra C: "))

Delta = (Valor_de_B**2) - (4 * Valor_de_A * Valor_de_C)

if Valor_de_A == 0 or Delta < 0:
    print("impossivel de Calcular")
    exit()
else:
  X1 = (-Valor_de_B + (Delta ** (1 / 2))) / (2 * Valor_de_A)
  X2 = (-Valor_de_B - (Delta ** (1 / 2))) / (2 * Valor_de_A)

print(f"X1 = {X1}")
print(f"X2 = {X2}")
