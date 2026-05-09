viagens = int(input("Quantas viagens foram realizadas? "))
total = 0 
for i in range(0, viagens):
    entregas = int(input(f"Quantas entregas foram feitas na {i+1}° viagem? "))
    total += entregas
media = entregas/viagens
print(f"Foram feitas {entregas} entregas em {viagens} viagens. A média de entregas feitas por viagem é de {media}")