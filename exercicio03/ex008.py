lista = []
total = 0
def controle_pedidos(a):
    lista.append(a)
    total = 1
    return total
while True:
    pedido = input("Qual o pedido do cliente? ")
    total += controle_pedidos(pedido)
    continuar = input("Deseja continuar adicionando pedidos? ").title()
    if continuar == "Sim" or continuar == "S":
            print("Continuando...")
    else:
        print("Sem adicionar mais...")
        break
while True:
    remover = input("Deseja remover algum pedido? ").upper()
    if remover == "SIM" or remover == "S":
        print(f"A lista de pedidos é {lista}")
        print(f"O total de pedidos é {total}")
        escolha = input("Qual deseja remover? ")
        lista.remove(escolha)
        print("Pedido removido...")
        total -= 1
    else:
        print("Sem remover...")
        break
print(f"A lista de pedidos é {lista}")
print(f"O total de pedidos é {total}")
     
