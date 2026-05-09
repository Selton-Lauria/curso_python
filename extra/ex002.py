raio = 1 
while raio != 0:
    raio = int(input("Qual o raio do círculo? (em cm) "))
    area = 3.14 * (raio ** 2)
    print(f"A área correspondente é {area:.2f}cm²")
    print("(para encerrar o programa, digite 0)")
print("Fim do programa.")