lista = []
def controle_estoque(a):
    lista.append(a)
while True:
    produto = input("Qual produto deseja cadastrar? ")
    controle_estoque(produto)
    print("Item adicionado...")
    continuar = input("Quer continuar adicionando itens ao estoque? ").lower()
    if continuar == "sim" or continuar == "s":
        print("Continuando...")
    else:
        print("Sem adicionar mais...")
        break
print(f"O estoque completo tem: {lista}")