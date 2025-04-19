palavra = input("Insira uma palavra: ")

def palindromo (palavra):
    palavra = palavra.lower()
    return palavra == palavra[::-1]

if palindromo(palavra):
    print(f"A palavra {palavra} é um palindromo")
else:
    print(f"A palavra {palavra} não é um palindromo")
