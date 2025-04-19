num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
operacao = input("Insira a operação desejada (soma, subtração, multiplicação ou divisão): ")

def soma (num1, num2):
    resultado = num1 + num2
    return resultado
def subtracao (num1, num2):
    resultado = num1 - num2
    return resultado
def multiplicacao (num1, num2):
    resultado = num1 * num2
    return resultado
def divisao (num1, num2):
    resultado = num1 / num2
    return resultado

if operacao == "soma":
    resultado = soma(num1, num2)
    print(resultado)
elif operacao == "subtração":
    resultado = subtracao(num1, num2)
    print(resultado)
elif operacao == "multiplicação":
    resultado = multiplicacao(num1, num2)
    print(resultado)
elif operacao == "divisão":
    resultado = divisao(num1, num2)
    print(resultado)
