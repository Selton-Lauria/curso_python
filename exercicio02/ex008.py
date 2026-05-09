lotes = int(input("Quantos lotes chegaram? "))
total = 0
for i in range(0, lotes):
    itens = int(input(f"Quantos itens chegaram no {i+1}° lote? "))
    total += itens
print(f"Foram adicionados {total} itens ao estoque!")