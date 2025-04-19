frase = input("Insira uma frase ou palavra: ")

def contar(frase):
    frase = frase.replace(" ", "")
    return len(frase)

qtd_caracteres = contar(frase)
print(f"A quantidade de caracteres da frase, sem os espaços é: {qtd_caracteres}")
