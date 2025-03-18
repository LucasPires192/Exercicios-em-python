nota1 = int(input("Digite a primeira nota:"))
nota2 = int(input("Digite a primeira nota:"))
nota3 = int(input("Digite a primeira nota:"))

media = float((nota1 + nota2 + nota3) / 3)

print("A média da nota é: ",  media)

if media >= 5:
    print("O aluno foi aprovado!")
else:
    print("O aluno foi reprovado!")