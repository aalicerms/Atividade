n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
n3 = float(input("Insira a terceira nota: "))

def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3)/3
    print(f"Média: {media:.2f}")

    if media >= 7:
        print("Você está acima da média! Parabens")
    else:
        print("Você está abaixo da média... Faça a recuperação e tente de novo")

calcular_media(n1, n2, n3)
