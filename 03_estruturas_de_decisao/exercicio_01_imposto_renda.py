"""
EXERCÍCIO 01: Imposto de Renda de Lisarb
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de uma pessoa em Rombus (R$).
- Até R$ 2000.00: Isento
- De R$ 2000.01 até R$ 3000.00: 8% sobre o excedente de R$ 2000.00
- De R$ 3000.01 até R$ 4500.00: 18% sobre o excedente de R$ 3000.00 + 8% da faixa anterior
- Acima de R$ 4500.00: 28% sobre o que ultrapassar R$ 4500.00 + impostos anteriores

Imprima "Isento" ou o valor total do imposto formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
valor_1 = float(input("Digite o salário: "))

if valor_1 <= 2000:
    print("Isento")
elif 2000 < valor_1 <= 3000:
    imposto = (valor_1 - 2000) * 0.08
    print(f"R$ {imposto:.2f}")
elif 3000 < valor_1 <= 4500:
    # 80.00 é o imposto fixo da faixa anterior (1000 * 0.08)
    imposto = 80.00 + (valor_1 - 3000) * 0.18
    print(f"R$ {imposto:.2f}")
elif valor_1 > 4500:
    # 350.00 é a soma do imposto fixo das duas faixas anteriores (80.00 + 270.00)
    imposto = 350.00 + (valor_1 - 4500) * 0.28
    print(f"R$ {imposto:.2f}")
