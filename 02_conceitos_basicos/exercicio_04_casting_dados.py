"""
EXERCÍCIO 04: Casting de Dados e Idade em 2026
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba do usuário o ano de nascimento como texto (str).
Converta essa entrada para inteiro (int) utilizando o conceito de casting
e calcule a idade que a pessoa completará até o final de 2026.
Imprima a idade calculada com uma mensagem personalizada.
"""

# TODO: Desenvolva o algoritmo abaixo:

# 1. Recebe o ano de nascimento como texto (str)
ano_de_nascimento = input("Digite seu ano de nascimento: ")

# 2. Converte a entrada para inteiro (int) usando casting
ano_de_nascimento_inteiro = int(ano_de_nascimento)

# 3. Calcula a idade correta que a pessoa completará em 2026
idade = 2026 - ano_de_nascimento_inteiro

# 4. Imprime a idade com uma mensagem personalizada
print(f"Até o final de 2026, você completará {idade} anos de idade!")
