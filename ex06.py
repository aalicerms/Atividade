frase = input("Escreva uma frase: ")

def contar(frase):
    vogais = "AaeEiIOoUu"
    contador = sum(1 for letra in frase if letra in vogais)
    return contador

print(f"A quantidade de vogais na frase é: {contar(frase)}")
