"""
EXERCÍCIO 05: Gestão de Escopo Global e Local
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Declare a variável global total_inscritos = 0.
Crie a função `inscrever_aluno(quantidade)` utilizando a diretiva `global`
para atualizar a variável. Demonstre o valor de total_inscritos antes e depois da chamada.
"""

# TODO: Desenvolva o algoritmo abaixo:
total_inscritos=0
print(f"Valor antigo: {total_inscritos}")
while True:
    resposta=input("Quer se inscrever ?(sim) ou (não)")
    if resposta=="sim":
        print("Tmj ai meu brother")
        def inscrever_aluno(t):
            return(t+1)
        inscrever_aluno(total_inscritos)    
        print(f"Valor Atual: {inscrever_aluno(total_inscritos)}")
        break
    print("Se inscreve ai pô")
