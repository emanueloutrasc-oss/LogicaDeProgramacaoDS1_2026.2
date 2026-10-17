n2=[]
soma=0
numero=int(input("digite um numero intero(ou 0 para parar): "))
while numero !=0:
    n2.append(numero)
    soma=sum(n2)
    numero=int(input("Digite mais um número(ou 0 para parar): "))
print(f"Essa é a soma dos números digitados: {soma}")
