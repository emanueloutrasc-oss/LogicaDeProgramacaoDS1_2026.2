"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:



idade_do_visitante=int(input("Qual sua idade ?"))
if  idade_do_visitante <12:
    calculo=(100/2) 
    print(f"Infantil--> {calculo:.2f} R$".replace('.',','))
elif    idade_do_visitante >=60:
    calculo=(00)
    print(f"Melhor idade--> {calculo:.2f} R$".replace('.',','))
elif    idade_do_visitante >60:
    calculo=(100)
    print(f"Demais--> {calculo:.2f} R$".replace('.',','))