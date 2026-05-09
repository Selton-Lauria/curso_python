quant_crianca = 0
quant_adolescente = 0
quant_adulto = 0
quant_idoso = 0
while True:
    idade = int(input("Qual a sua idade? "))
    if idade <= 12:
        print("Você é uma criança")
        quant_crianca += 1
    elif idade <= 17:
        print("Você é um adolescente")
        quant_adolescente += 1
    elif idade <= 59:
        print('Você é um adulto')
        quant_adulto += 1
    else: 
        print("Você é um idoso")
        quant_idoso += 1
    cont = input("Deseja continuar? (s/n) ").lower()
    if cont == "sim" or cont == "s":
        print("Continuando...")
    else:
        print("Saindo...")
        break
print("Foram regsitrados...: ")
print(f"{quant_crianca} crianças")
print(f"{quant_adolescente} adolescentes")
print(f"{quant_adulto} adultos")
print(f"{quant_idoso} idosos")
print("Fim do programa.")