compras = int(input("Quantas compras foram feitas no dia? "))
total = 0
for i in range(0, compras):
    valor = float(input(f"Qual o valor da {i+1}° compra? "))
    total += valor
print(f"O valor total faturado foi de R${total:.2f}")

