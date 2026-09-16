"""
EXERCÍCIO 03: Conta do Nagoya Sushi House
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie um programa que:
1. Leia o valor total consumido no restaurante (em R$).
2. Aplique a taxa de 10% de serviço do garçom.
3. Exiba o valor final da conta a pagar com mensagem formatada.
"""

# TODO: Desenvolva o algoritmo abaixo:

valor_consumido = float(input("Digite o valor do prato que foi consumido: "))

# 2. Verificamos se o valor é maior que 0 usando o 'if' corretamente
if valor_consumido > 0:
    # Calculando a taxa e o total
    taxa_servico = valor_consumido * 0.10
    total_geral = valor_consumido + taxa_servico

    # 3. Formatamos os valores para o padrão de dinheiro R$
    taxa_formatada = f"R$ {taxa_servico:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
    total_formatado = f"R$ {total_geral:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
    
    # Mostrando o resultado detalhado
    print(f"Taxa de serviço (10%): {taxa_formatada}")
    print(f"O total a pagar é: {total_formatado} volte sempre !!")
else:
    print("Você não tem nada a pagar.")
