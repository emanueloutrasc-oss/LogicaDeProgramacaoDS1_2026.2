"""
EXERCÍCIO 03: Pares entre Cinco Números
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite 5 números inteiros ao usuário.
Utilize uma estrutura de repetição e um contador para verificar quantos números pares
foram digitados. Ao final, imprima a quantidade total.
"""

# TODO: Desenvolva o algoritmo abaixo:
lista_de_numeros=[]
for i in range(5):
    resposta=int(input("Digite um número inteiro:"))
    lista_de_numeros.append(resposta)
print("\n---- Analisando os números -----")
for n in lista_de_numeros:
    if  n % 2  == 1:
        print(f"esse numero é impar :{n}")
    else:
        print(f"esse número é par :{n}")