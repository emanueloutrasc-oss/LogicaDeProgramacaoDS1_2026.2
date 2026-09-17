"""
DESAFIO 01: O BUG MATEMÁTICO DA MÉDIA ESCOLAR
Disciplina: Lógica de Programação com Python
EEEP Professor Sebastião Vasconcelos Sobrinho

RELATÓRIO DA INVESTIGAÇÃO:
Um estagiário do sistema acadêmico tentou implementar o cálculo da média semestral
de um aluno, mas o sistema apresentou resultados bizarros devido a erros de tipagem
e precedência de operadores.

SUA MISSÃO:
1. Identifique e corrija os erros de tipagem (casting) e precedência.
2. Faça o programa calcular e exibir a média correta formatada com 1 casa decimal.
"""

# CÓDIGO ORIGINAL COM BUG (Analise e corrija):
# nota1 = input("Digite a primeira nota: ")
# nota2 = input("Digite a segunda nota: ")
# media = nota1 + nota2 / 2
# print("A média do aluno é:", media)

# TODO: Escreva aqui o código corrigido:
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a primeira nota:"))
media = (nota1 + nota2) / 2 
print("A média do aluno é:", media)
#Além de ser necessário do dado ser recebido em float ao invés de str 
#O ERRO estava na operação por falta de um parêntese 
#fazendo com que a prioridade fosse da divisão e não da soma