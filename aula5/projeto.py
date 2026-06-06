pacientes = []
consultas = []
medicos = []
def NovoPaciente():
    paciente = {
        "Id": len(pacientes) + 1,
        "Nome": input("Qual o nome do paciente? ").title(),
        "CPF": input("CPF do cliente: "),
        "Data_Nascimento": input("Qual a data de nascimento? "),
        "Telefone": input("Telefone do paciente: "),
        "Email": input("Qual o email? "),
        "Endereço": input("Qual o endereço? ")
    }
    pacientes.append(paciente)
def NovoMedico():
    medico = {
        "Id": len(medicos) + 1,
        "Nome": input("Qual o nome do Médico? ").title(),
        "CRM": input("CRM do Médico: "),
        "Especialidade": input("Qual a Especialidade do Médico? "),
        "Telefone": input("Telefone do Médico: "),
        "Email": input("Qual o email? ")
    }
    medicos.append(medico)
def NovaConsulta():
    print("Id's dos pacientes registrados")
    for paciente in pacientes:
        print(paciente["Nome"], paciente["Id"])
    id_paciente = input("Qual o id do paciente? ")
    print("Id's dos médicos registrados")
    for medico in medicos:
        print(medico["Nome"], medico["Id"])
    id_medico = input("Qual o id do médico? ")
    consulta = {
        "Id": len(consultas) + 1,
        "Data": input("Qual a data da consulta? "),
        "Hora": input("Que horas é a consulta? "),
        "Observacao": input("Observação: "),
        "Paciente_id": int(id_paciente),
        "Medico_id": int(id_medico)
    }
    consultas.append(consulta)
while True:
    print("MENU")
    opcao = int(input("O que você quer registrar?\n[1] Novo Paciente\n[2] Novo Médico\n[3] Consulta\n[4] Sair\n"))
    match opcao:
        case 1:
            print("Registrando Novo Paciente...")
            NovoPaciente()
            print("Todos os pacientes registrados: ")
            for paciente in pacientes:
                print(paciente["Nome"])
        case 2:
            print("Registrando Novo Médico...")
            NovoMedico()
            print("Todos os médicos registrados: ")
            for medico in medicos:
                print(medico["Nome"])
        case 3:
            if len(medicos) == 0 or len(pacientes) == 0:
                print("Registre médicos ou pacientes primeiro...")
            else:
                print("Marcando Consulta...")
                NovaConsulta()
        case 4: 
            print("Saindo...")
            break
        case _:
            print("Opção inválida!")
while True:
    print("Banco de Dados: ")
    opcao = int(input("O que você quer ver?\n[1] Pacientes\n[2] Médicos\n[3] Consultas\n[4] Sair\n"))
    match opcao:
        case 1:
            for paciente in pacientes:
                print("Informações sobre o paciente")
                print(f"Nome: {paciente["Nome"]}")
                print(f"Id: {paciente["Id"]}")
                print(f"CPF: {paciente["CPF"]}")
                print(f"Data de Nascimento: {paciente["Data_Nascimento"]}")
                print(f"Telefone: {paciente["Telefone"]}")
                print(f"Email: {paciente["Email"]}")
                print(f"Endereço: {paciente["Endereço"]}")
                print("-"*40)
        case 2: 
            for medico in medicos:
                print("Informações sobre o médico: ")
                print(f"Nome: {medico["Nome"]}")
                print(f"Id: {medico["Id"]}")
                print(f"CRM: {medico["CRM"]}")
                print(f"Especialidade: {medico["Especialidade"]}")
                print(f"Telefone: {medico["Telefone"]}")
                print(f"Email: {medico["Email"]}")
                print("-"*40)
        case 3:
            for consulta in consultas:
                print("Informações sobre a consulta: ")
                print(f"Id: {consulta["Id"]}")
                print(f"Data: {consulta["Data"]}")
                print(f"Hora: {consulta["Hora"]}")
                print(f"Observação: {consulta["Observacao"]}")
                for i in medicos:
                    if i["Id"] == consulta["Medico_id"]:
                        print(f"Médico responsável: {i["Nome"]}")
                    else:
                        pass
                for i in pacientes:
                    if i["Id"] == consulta["Paciente_id"]:
                        print(f"Paciente: {i["Nome"]}")
                    else:
                        pass
                print("-"*40)
        case 4:
            print("Saindo...")
            break
print("Fim do Programa....")
