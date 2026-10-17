"""
EXERCÍCIO 03: Gerador de Alertas da Cagece
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Desenvolva um procedimento `emitir_alerta_fatura(nome_cliente, valor, data_vencimento)`
que imprima a mensagem:
"Prezado(a) [nome], sua fatura da Cagece no valor de R$ [valor] vence no dia [data]."
"""

# TODO: Desenvolva o procedimento abaixo:
nome_cliente=input("Seu nome: ")
valor=200
data="12/09/2026"
def emitir_alerta_fatura(nome,v,d):
    return(f"Prezado(a) {nome}, sua fatura da Cagece no valor de R$ {v} vence no dia {d}")
Alerta=emitir_alerta_fatura(nome_cliente,valor,data)
print(Alerta)