login = "admin"
senha = "1234"
while True:
    logusu = input("Qual é o login? ")
    senusu = input("Qual a senha? ")
    if logusu == login and senusu == senha:
        print("Acesso liberado.")
        break
    else:
        print("Login ou senha incorretos.")
        print("Tente novamente")
