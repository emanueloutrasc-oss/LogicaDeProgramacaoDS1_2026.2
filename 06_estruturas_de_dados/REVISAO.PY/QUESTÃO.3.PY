maior_peso = 0
menor_peso = 0
quantidade_de_pecas = int(input("Informe a quantidade de peças: "))
for n in range(quantidade_de_pecas):
    valores = float(input(f"Digite o valor da {n+1}ª peça: "))
    if n == 0:
        maior_peso = valores
        menor_peso = valores
    else:
        if valores > maior_peso:
            maior_peso = valores
        elif valores < menor_peso:
            menor_peso = valores
print(f"\nMaior peso: {maior_peso}, Menor peso: {menor_peso}")