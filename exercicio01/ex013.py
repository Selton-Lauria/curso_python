conta = int(input("Qual o tipo da sua conta? (1 - conta comum | 2 - conta premium) "))
saldo = float(input("Qual o seu saldo médio? (em R$) "))
if conta == 1:
    if saldo >= 5000:
        print("Insento de tarifa")
    elif saldo >= 1000:
        print("Tarifa de R$15.00")
    else:
        print("Tarifa de R$25.00")
elif conta == 2:
    if saldo >= 5000:
        print("Insento de tarifa")
    else: 
        print("Tarifa de R$20.00")
else:
    print("Inválido.")
