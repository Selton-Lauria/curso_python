for i in range(0, 4):
    temp = float(input(f"Qual a temperatura da {i+1}° pessoa? "))
    conversor = ((temp * 9)/5)+32
    print(f"O valor convertido para Fahrenheit é {conversor}°F")