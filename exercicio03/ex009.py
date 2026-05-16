lista = []
def controle_financeiro(a):
    lista.append(a)
    if a > 5000:
        print("Receita alta!")
    elif a >= 2000:
        print("Receita média")
    else:
        print("Receita baixa.")
while True:
    entrada = float(input("Qual a entrada financeira? "))
    controle_financeiro(entrada)
    continuar = input("Deseja adicionar mais entradas? ").lower()
    if continuar == "sim" or continuar == "s":
        print("Continuando...")
    else:
        print("Sem adicionar mais...")
        break
print("Fim do programa...")