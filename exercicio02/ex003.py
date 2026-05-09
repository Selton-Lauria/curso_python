total = 0
while True:
    compra = float(input("Qual o valor da compra? "))
    if compra == 0:
        break
    else:
        total += compra
print(f"O total do dia foi: R${total:.2f}")