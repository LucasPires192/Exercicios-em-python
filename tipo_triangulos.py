lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 == lado2 == lado3 :
    print("Triângulo Equilátero")
if lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado1 == lado3 != lado2:
    print("Triângulo Isóscele")
if lado1 != lado2 != lado3:
    print("Triângulo Escaleno")