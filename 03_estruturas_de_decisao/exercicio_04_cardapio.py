"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:

# Tabela de preços: código -> preço
precos = {
    "Cachorro Quente": 4.00,
    "X-Salada" : 4.50,
    "X-Bacon": 5.00,
    "Torrada Simples": 2.00,
    "Refrigerante": 1.50
}

# Lendo o código e a quantidade consumida
codigo =(input("Digite o nome do item: "))
quantidade = int(input("Digite a quantidade: "))
if codigo in precos:
    total = precos[codigo] * quantidade
    print(f"Total: R$ {total:.2f}")
else:
    print("Código inválido!")


