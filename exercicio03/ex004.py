lista = []
def folha_pagamento(a):
    lista.append(a)
    if a < 2500:
        print("Classe E")
    elif a < 7000:
        print("Classe D")
    else:
        print("Classe C")
while True:
    salario = float(input("Digite o salário: "))
    folha_pagamento(salario)
    continuar = input("Deseja continuar? ").title()
    if continuar == "Sim" or continuar == "S":
        print("Continuando...")
    else:
        print("Saindo...")
        break
print(f"todos os salários adicionados: {lista}")
