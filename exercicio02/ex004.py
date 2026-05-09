total = 0
while True:
    entregas = int(input("Quantas entregas foram feitas na viagem? "))
    if entregas == 0:
        break
    else:
        total += entregas
print(f"Foram feitas {total} entregas no total. ")