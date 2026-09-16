"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:

n1=float(input("digite o número 2"))
n2=float(input("digite o número 3"))
n3=float(input("digite o número 5"))
media_da_nota=(n1 + n2 + n3) / 2 
print(f"a média é {media_da_nota:.2f}")

