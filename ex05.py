num = int(input("Insira um número: "))

def tabuada(num):
    for i in range (1, 11):
        print(f"{num} x {i} = {num * i}")

tabuada(num)
