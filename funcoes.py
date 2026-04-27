def calcular_media(nota1, nota2, nota3):
    soma = nota1 + nota2 + nota3
    media = soma / 3
    return media
#Programa Principal (Fora de função)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

resultado = calcular_media(nota1, nota2, nota3)
print(f"A média das notas é: {resultado:.2f}")