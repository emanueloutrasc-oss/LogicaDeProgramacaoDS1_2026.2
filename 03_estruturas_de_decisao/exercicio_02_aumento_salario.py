"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:

salario=float(input("Digite seu salário: " ))
if  0.01<= salario <400.00:
    salario_aplicado= salario * 0.15
    print(salario + salario_aplicado) 
elif    400.01<= salario <800.00:
    salario_aplicado=salario * 0.12
    print(salario + salario_aplicado)
elif    800.01<=salario <1200:
    salario_aplicado=salario * 0.08
    print(salario + salario_aplicado)
elif    1200.01<= salario <2000.00:
    salario_aplicado=salario * 0.07
    print(salario + salario_aplicado)
elif    salario >2000.01:
    salario_aplicado=salario * 0.04
    print(salario + salario_aplicado)




