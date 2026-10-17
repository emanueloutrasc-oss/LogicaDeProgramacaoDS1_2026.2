"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo:
def calcular_preco_final(preco_base, taxa_desc, taxa_imp):
    valor_desconto = preco_base * taxa_desc
    valor_imposto = preco_base * taxa_imp
    preco_final = preco_base - valor_desconto + valor_imposto
    return preco_final

def exibir_relatorio_item(numero_item, preco_final):
    print(f"--- Relatório do Item ---")
    print(f"Item Número: {numero_item}")
    print(f"Preço Final: R$ {preco_final:.2f}")
    print("-------------------------")

numero = 1
preco_inicial = 150.00
desconto = 0.15  
imposto = 0.08 

preco_calculado = calcular_preco_final(preco_inicial, desconto, imposto)
exibir_relatorio_item(numero, preco_calculado)

