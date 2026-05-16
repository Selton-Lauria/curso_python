lista = []
def cadastro_clientes(a):
    lista.append(a)
while True:
    nome = str(input("Digite o nome do cliente: ")).title()
    cadastro_clientes(nome)
    escolha = input("Você quer continuar cadastrando? ").lower()
    if escolha == "s" or escolha == "sim":
        print("Continuando...")
    else:
        print("Saindo...")
        break
print(lista)
print(f"Tem {len(lista)} clientes cadastrados.")
remover = input("Deseja remover algum cliente? ").lower()
if remover == "s" or remover == "sim":
    remover_cliente = str(input("Diga o nome do cliente que deseja remover: ")).title()
    lista.remove(remover_cliente)
    print("Cliente removido.")
else:
    print("Nenhum Cliente removido...")
print(lista)
print("Fim do programa...")

