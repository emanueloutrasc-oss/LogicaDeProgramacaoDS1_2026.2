def preco_por_km(km):
    return km * 0.50

def adicionar_taxa(valor_atual, km):
    if km > 100:
        return valor_atual + 15.00
    return valor_atual

distancia = float(input("Digite a distancia (em Km): "))
cliente = input("Voce é um cliente 'VIP' ou 'Padrão': ")
preco_base = preco_por_km(distancia)
preco_com_taxa = adicionar_taxa(preco_base, distancia)
if cliente.upper() == "VIP":
    preco_final = preco_com_taxa - (preco_com_taxa * 0.20)
else:
    preco_final = preco_com_taxa
print(f"Esse é o valor do frete: R$ {preco_final:,.2f}")

