
ana = 0
joao = 0
maria = 0
while True:
    print("\n--- URNA ELETRÔNICA ---")
    print("1 - Ana")
    print("2 - Joao")
    print("3 - Maria")
    print("0 - Encerrar votação")
    voto = int(input("Digite o número do seu candidato: "))
    if voto == 1:
        ana += 1
        print("Voto confirmado para Ana!")
    elif voto == 2:
        joao += 1
        print("Voto confirmado para Joao!")
    elif voto == 3:
        maria += 1
        print("Voto confirmado para Maria!")
    elif voto == 0:
        print("\nVotação encerrada!")
        break
    else:
        print("Opção inválida! Digite um número de candidato existente (1, 2, 3) ou 0 para sair.")
print("\n=== RESULTADO DA VOTAÇÃO ===")
print(f"Ana: {ana} voto(s)")
print(f"Joao: {joao} voto(s)")
print(f"Maria: {maria} voto(s)")
maior_voto = max(ana, joao, maria)
if ana == joao == maria == 0:
    print("Nenhum voto foi registrado.")
elif ana > joao and ana > maria:
    print(f"O vencedor foi: Ana ({ana} votos)")
elif joao > ana and joao > maria:
    print(f"O vencedor foi: Joao ({joao} votos)")
elif maria > ana and maria > joao:
    print(f"O vencedor foi: Maria ({maria} votos)")
else:
    print(f"Houve um empate com {maior_voto} voto(s)!")