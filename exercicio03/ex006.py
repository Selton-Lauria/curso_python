lista = []
def cadastro_funcionarios(a):
    lista.append(a)
while True:
    nome = input("Qual o nome do funcionário? ").title()
    cadastro_funcionarios(nome)
    continuar = input("Deseja adicionar mais funcionários? ").lower()
    if continuar == "sim" or continuar == "s":
        print("Continuando...")
    else:
        print("Sem adicionar mais...")
        break
print(f"Os funcionários cadastrados foram {lista}")