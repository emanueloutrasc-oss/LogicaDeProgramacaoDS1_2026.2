"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
print("\n-----PROJETO VIAGEM-----")
distancia_em_km = float(input("Digite a distancia da sua viagem: "))
consumo_em_km = float(input("Digite o consumo do carro (km/l): "))
preco_combustivel = float(input("Digite o preço do combustivel: "))
qtd_pessoas = float(input("Digite a quantidade de pessoas para sua viagem: "))
Dias = float(input("Digite a quantidade de dias da sua viagem: "))
Diaria_alimentacao = float(input("Digite a diária da sua alimentação por pessoa: "))

def calcular_custo_transporte(dist, consu, preco):
  return (dist / consu) * preco

custo1 = calcular_custo_transporte(
    distancia_em_km, consumo_em_km, preco_combustivel
)
def calcular_custo_alimentacao(qtd, dias, diarias):
  return qtd * dias * diarias

custo2 = calcular_custo_alimentacao(qtd_pessoas, Dias, Diaria_alimentacao)
print("\n----CUSTO POR TRANSPORTE----")
print(f"R$ {custo1:.2f}")

print("\n----CUSTO POR ALIMENTAÇÃO----")
print(f"R$ {custo2:.2f}")

print("\n----CUSTO TOTAL----")
print(f"R$ {custo1 + custo2:.2f}")