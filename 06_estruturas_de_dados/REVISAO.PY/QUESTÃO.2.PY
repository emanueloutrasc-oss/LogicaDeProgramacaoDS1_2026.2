import random
qtd_perigos = 0
variacao_de_temperatura = 0.0
gatilho = "sim"
while True:
    valores = random.uniform(5, 40)
    variacao_de_temperatura += valores  
    if valores >= 35.0:
        print(f"Marca de Perigo! Valor gerado: {valores:.2f}")
        qtd_perigos += 1 
        gatilho = input("Quer continuar? (sim/não): ").strip().lower()
        if gatilho != "sim":
            break
    else:
        continue
if qtd_perigos > 0:
    media = variacao_de_temperatura / qtd_perigos
    print(f"\nMédia calculada: {media:.2f}")
else:
    print("\nNenhum perigo foi registrado durante a execução.")