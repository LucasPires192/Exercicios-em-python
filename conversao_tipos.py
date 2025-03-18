altura = float(input("Digite a sua altura: "))
peso = input("Digite seu peso: ")
imc = int(peso) / (altura ** 2)

print("Seu IMC é: " , round(imc, 2))