"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:

distancia_total=float(input("Qual é a distância total pecorrida em km de uma viagem, partindo de Tianguá para o Beach Park(Aquiraz)?"))
total_combustivel=float(input("Agora quantos litros seriam gastos ao total dessa viagem ? "))
consumo_medio=distancia_total / total_combustivel
print(f"O consumo médio de sua viagem é de {consumo_medio:.2f} por km/l")
