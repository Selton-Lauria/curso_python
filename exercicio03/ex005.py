lista = []
total = 0
quant_aprovados = 0
quant_reprovados = 0
def controle_notas(a):
    lista.append(a)
    total = 1
    return total
while True:
    nota = float(input("Qual a nota do aluno? "))
    total += controle_notas(nota)
    if nota >= 7:
        print("Aluno aprovado!")
        quant_aprovados += 1
    else:
        print("Aluno reprovado.")
        quant_reprovados += 1
    continuar = input("Deseja adicionar mais notas? ").lower()
    if continuar == "sim" or continuar == "s":
        print("Continuando...")
    else:
        print("Sem adicionar mais...")
        break
soma = sum(lista)
print(f"A média da turma foi {soma/total}")
print(f"A quantidade de aprovados foi {quant_aprovados}")
print(f"A quantidade de reprovados foi {quant_reprovados}")
 