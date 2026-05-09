peso = float(input("Qual o seu peso?(em kg) "))
altura = float(input("Qual a sua altura?(em metros) "))
imc = peso / (altura**2)
if imc <= 18.5:
    print(f"Seu imc é {imc:.2f}, você está abaixo do peso! ")
elif imc < 25:
    print(f"Seu imc é {imc:.2f}, você está no peso normal ")
elif imc < 30:
    print(f"Seu imc é {imc:.2f}, você está com sobrepeso ")
else: 
    print(f"Seu imc é {imc:.2f}, você está com obesidade")
