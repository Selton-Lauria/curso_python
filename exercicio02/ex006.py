while True:
    print("="*25)
    print("CADASTRO DE ALUNOS")
    print("="*25)
    nome = input("Qual o nome do aluno? ").title()
    nota1 = float(input("Qual a primeira nota? "))
    nota2 = float(input("Qual a segunda nota? "))
    media = (nota1 + nota2) / 2
    if media >= 7:
        situacao = "Aprovado(a)"
    elif media >= 4:
        situacao = "de Recuperação"
    else:
        situacao = "Reprovado(a)"
    print(f"O aluno(a) {nome} teve a média {media} e está {situacao}.")
    break
while True:
    print("="*25)
    print("CADASTRO DE PROFESSORES")
    print("="*25)
    nome = input("Qual o nome do professor? ").title()
    titulacao = input("Qual a titulação dele? ").title()
    if titulacao == "Mestrado" or titulacao == "Doutorado":
        print(f"O professor(a) {nome} pode orientar Projetos.")
    elif titulacao == "Graduação":
        print(f"O professor(a) {nome} pode apenas ministrar aulas básicas.")
    else:
        print("Titulação inválida.")
    break
while True:
    print("="*25)
    print("SETOR FINANCEIRO")
    print("="*25)
    categoria = input("Você é aluno ou professor? ").title()
    if categoria == "Aluno":
        print("A mensalidade é R$800.00")
        print("Pague a mensalidade por favor...")
        valor = float(input("Quanto você vai pagar? "))
        if valor >= 800:
            print("Pagamento feito! ")
            break
        else:
            falta = 800 - valor
            print("Valor inválido")
            print(f"Falta R${falta:.2f}")
            pagar = input("Quer pagar o que falta? (s/n) ").lower()
            if pagar == "s":
                print("Obrigado pelo pagamento!")
            else:
                print("Você está em dívida...")
                break
    elif categoria == "Professor":
        print(f"Seu salário base é R$1500.00")
        hora = int(input("Quantas horas extras você fez? "))
        total = (((1500/160)*hora)*1.5)+1500
        print(f"Você receberá o total de R${total:.2f}")
        break
    else:
        print("Inválido, coloque novamente...")
print("Programa encerrado.") 
