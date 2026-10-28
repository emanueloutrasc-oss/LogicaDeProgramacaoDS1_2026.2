valor_conta = float(input("Digite o valor total da conta (R$): "))
qtd_amigos = int(input("Digite a quantidade de amigos para dividir a conta: "))
valor_por_pessoa = valor_conta / qtd_amigos
print(f"Cada amigo deve pagar: R$ {valor_por_pessoa:.2f}")