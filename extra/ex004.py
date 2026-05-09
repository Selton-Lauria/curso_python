cont = 1
while cont != 0:
    ganha = float(input("Quanto você ganha por hora? "))
    horas = int(input("Quantas horas você trabalhou nesse mês? "))
    salario = ganha * horas
    print(f"Seu salário é R${salario}")
    cont = int(input("Deseja continuar? (0 - sair | 1 - Continuar) "))
print("Fim desse programa.")
while True:
   graus = float(input("Qual a temperatura em graus Fahrenheit? "))
   celsius = 5 * ((graus - 32)/9)
   print(f"A temperatura em celsius é {celsius}°C") 
   break
