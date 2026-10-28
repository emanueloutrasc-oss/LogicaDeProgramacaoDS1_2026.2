def calcular_juros(v,t,nm):
    juros=v*(1+(nm))**t
    return juros
juros=float(input("Digite o valor da taxa a ser aplicada(%):"))
valor_inicial=int(input("Digite o valor inicial a ser calculado: "))
tempo=int(input("Digite o tempo de aplicação (em meses): "))
calcular_juros(valor_inicial,juros,tempo)
for n in range(1,tempo+1):
    print(f"Mês {n} de {tempo}: {calcular_juros(valor_inicial,juros,tempo)-valor_inicial:,.2f}")
