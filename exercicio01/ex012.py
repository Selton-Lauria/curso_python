cadastrada  = '1234'
senha = str(input("Qual a senha? "))
if senha == cadastrada:
    print("Acesso permitido. ")
elif senha == "":
    print("Senha inválida")
else: 
    print("Acesso negado. ")