numero=float(input("Digite um valor: "))
calculo_acrescimo= lambda a: a*0.10+a
print(f"Esse é o preço: {calculo_acrescimo(numero):.2f} R$")