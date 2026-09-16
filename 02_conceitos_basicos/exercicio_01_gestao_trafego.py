
"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: Desenvolva o algoritmo abaixo:

# Primeiramente crio variaveis para armazenar os valores 
valor_investido = float(input("Qual foi o valor total investido na campanha? R$ "))

# Formato a entrada de dados. Como cliques são contados em unidades inteiras, usamos int()
numero_total_cliques = int(input("Qual o número total de cliques obtidos? "))

# Verifico se o número de cliques é maior que zero para evitar o erro de divisão por zero
if numero_total_cliques > 0:
    # Crio uma variavel para armazenar o resultado da operação entre as variaveis anteriores
    Custo_por_clique = valor_investido / numero_total_cliques
    
    # Por último, mostro o resultado na tela e adiciono na formmatação pedida
    print("O Custo por Clique (CPC) médio da campanha é R$ {Custo_por_clique:.2f})".replace('.',','))
else:
    # Caso a campanha tenha 0 cliques, o CPC também é zero
    print("A campanha ainda não obteve cliques. O CPC médio é R$ 0,00")
