for i in range(0, 5):
    altura = float(input("Qual a sua altura em metros? "))
    sexo = str(input("Qual o seu sexo? [M/F] ")).upper()
    if sexo == "M":
        peso_ideal = (72.7*altura)-58
        print("Seu peso ideal é {:.2f}".format(peso_ideal))
    elif sexo == "F":
        peso_ideal = (62.1*altura)-44.7
        print("Seu peso ideal é {:.2f}".format(peso_ideal))
    else: 
        print("Resultado inválidado.")
print("Fim do programa.")
