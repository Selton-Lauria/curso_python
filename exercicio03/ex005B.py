lista = []
total = 0
def caixa_mercado(a):
    lista.append(a)
    total = 1
    return  total
while True:
    compra = float(input("Qual o valor da compra? "))
    total += caixa_mercado(compra)
    continuar = input("Deseja adicionar mais compras? ").upper()
    if continuar == "SIM" or continuar == "S":
        print("Continuando...")
    else:
        print("Sem adicionar mais...")
        break
while True:
    print(f"O total arrecadado até agora foi de R${sum(lista)}")
    print(f"A quantidade de compras feitas até agora foi de {total}")
    escolha = input("Alguma compra foi cancelada? ").title()
    if escolha == "Sim" or continuar == "S":
        print(lista)
        remover = float(input("Qual o preço da venda cancelada? "))
        lista.remove(remover)
        total -= 1
        break
    else:
        print("Saindo...")
        break
print(f"O total arrecadado foi R${sum(lista)}")
print(f"A quantidade de compras feitas foi {total}")

