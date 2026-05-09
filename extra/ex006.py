cont = 1
while cont != 2:
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite outro número inteiro: "))
    n3 = float(input("Digite um número real: "))
    print("O produto do dobro do primero e a metade do segundo é {}".format((n1*2)*(n2/2)))
    print("A soma do triplo do primeiro com o terceiro é {}".format((n1*3)+n3))
    print("o terceiro elevado ao cubo é {}".format(n3**3))
    cont = int(input("Deseja continuar? (1 - Continuar | 2 - Sair) "))
print("Fim do programa")