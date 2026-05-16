lista = []
def vendas_loja(a):
    lista.append(a)
while True:
    vendas = float(input("Qual o valor da venda? "))
    total = vendas_loja(vendas)
    continuar = input("Deseja continuar? ").upper()
    if continuar == "SIM" or continuar == "S":
        print("Continuando...")
    else:
        print("Saindo...")
        break
lista.sort()
print(f"O total vendido é igual a R${sum(lista)}")
print(f"A maior venda foi R${max(lista)}")
print(f"A menor venda foi R${min(lista)}")