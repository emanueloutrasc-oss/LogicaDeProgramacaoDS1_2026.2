"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
números = []
Positivos = []

for n in range(6):
    n = float(input("Digite um valor: "))
    números.append(n)  
for fx in números:
    if fx > 0:
        Positivos.append(fx)
    else:
        print(f"Infelizmente o número {fx} não pode ser calculado por ser negativo ou zero")

print("\n----Calculando média-----")


if len(Positivos) > 0:
    media = sum(Positivos) / len(Positivos)
    print(f"Esses são os valores positivos: {Positivos}")
    print(f"Essa é a média dos positivos: {media:.1f}")
else:
    print("Nenhum número positivo foi digitado para calcular a média.")
