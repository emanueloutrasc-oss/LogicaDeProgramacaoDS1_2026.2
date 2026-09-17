"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
#Crio variáveis para Armazenar o valor 

n1=float(input("digite o número:  "))
n2=float(input("digite o número:  "))
n3=float(input("digite o número:  "))
peso1=(n1*2)
peso2=(n2*3)
peso3=(n3*5)
media_da_nota=(peso1 + peso2 + peso3 ) / 10 
print(f"a média é {media_da_nota:.2f}".replace('.',','))

