lado = int(input("Digite a quantidade de lados do poligono: "))
tam = float(input("Digite a medida dos lados do poligono: "))

if lado < 3 :
    print("NÃO É POLIGONO")
if lado == 3 :
    area = tam ** 3
    print("TRIANGULO: " , area)
if lado == 4 :
    area = tam ** 2
    print("QUADRADO: " , area)
if lado == 5 :
    print("PENTÁGONO")
if lado > 5:
    print("POLÍGONO NÃO IDENTIFICADO")