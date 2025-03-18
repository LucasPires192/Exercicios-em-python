altura = float(input("Digite seu altura: "))
sexo = int(input("Qual é o seu sexo? Digite 1 pra homem e 2 pra mulher: "))

if sexo == 1 :
    imc = (72.7 * altura) - 58
    print(sexo)
    print("O seu peso ideal é: " , imc)
else :
    imc = (62.1 * altura) - 44.7
    print(sexo)
    print("O seu peso ideal é: " , imc)