altura = float(input("Qual a sua altura em metros? "))
while True:
    sexo = str(input("Qual o seu sexo? [M/F] ")).upper()
    if sexo == "M":
        peso_ideal = (72.7*altura)-58
        print("Seu peso ideal é {:.2f}".format(peso_ideal))
        break
    elif sexo == "F":
        peso_ideal = (62.1*altura)-44.7
        print("Seu peso ideal é {:.2f}".format(peso_ideal))
        break
    else: 
        print("Inválido. Coloque novamente")