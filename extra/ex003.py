for i in range(0, 3):
    lado = int(input(f"Qual o lado do {i+1}° quadrado? (em cm) "))
    area = (lado * lado) * 2
    print(f"O dobro da área correspondente é {area:.2f}cm²")
print("Fim do programa.")