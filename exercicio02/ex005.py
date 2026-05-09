feijao = 8
arroz = 6.5
farinha = 5
total = 0
while True:
    print(f"O feijao esta R${feijao:.2f}")
    print(f"O arroz esta R${arroz:.2f}")
    print(f"A farinha esta R${farinha:.2f}")
    compra = input("Qual quer comprar? ").lower()
    if compra == "feijao":
        total += feijao
    elif compra == "arroz":
        total += arroz
    elif compra == "farinha":
        total += farinha
    else:
        print("Inválido!")
    escolha = input("Quer sair? (digite sair) ").title()
    if escolha != "Sair":
        print("Continuando...")
    else:
        print("Saindo...")
        break
print(f"O preço total foi de R${total:.2f}")