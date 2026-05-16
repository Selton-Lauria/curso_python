lista = []
def controle_comissoes(a):
    lista.append(a)    
while True:
    venda = float(input("Qual o valor da venda? "))
    controle_comissoes(venda)
    continuar = input("Deseja adicionar mais vendas? ").upper()
    if continuar == "SIM" or continuar == "S":
        print("Continuando...")
    else:
        print("Sem adicionar mais...")
        break
print(f"foram feitas {len(lista)} vendas")
for i in range(len(lista)):
    comissao = lista[i] * 0.1
    print(f"A comissão pela {i+1}° venda foi de R${comissao:.2f}")
print("Fim das comissões...")
 