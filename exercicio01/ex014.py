visu = int(input("Quantas visualizações o vídeo teve? "))
ganho = 0
if visu > 500000:
    ganho += 500
if visu > 1000000:
    ganho += visu * 0.05
    print(f"Seu ganho é R${ganho:.2f}")
elif visu > 100000:
    ganho += visu * 0.03
    print(f"Seu ganho é R${ganho:.2f}")
elif visu > 10000:
    ganho += visu * 0.02
    print(f"Seu ganho é R${ganho:.2f}")
else:
    print("Não há monetização")