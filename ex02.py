valor = float(input("Insira um valor para a conversão: "))
uni_medida = input("Qual a unidade de medida do valor inserido?: ")
uni_conver = input("Qual a unidade que você quer converter?: ")

def km_milha (valor):
    milha = valor * 0.6214
    return milha
def milha_km (valor):
    km = valor * 1.6093
    return km
def m_cm (valor):
    metro = valor * 100
    return metro
def cm_m (valor):
    centimetro = valor/100
    return centimetro
def l_ml(valor):
    litro = valor * 1000
    return litro
def ml_l(valor):
    mililitro = valor / 1000
    return mililitro

if uni_medida == "quilometro" and uni_conver == "milha":
    resultado = km_milha(valor)
    print(resultado)
elif uni_medida == "milha" and uni_conver == "quilometro":
    resultado = milha_km(valor)
    print(resultado)
elif uni_medida == "metro" and uni_conver == "centímetro":
    resultado = m_cm(valor)
    print(resultado)
elif uni_medida == "centímetro" and uni_conver == "metro":
    resultado = cm_m(valor)
    print(resultado)
elif uni_medida == "litro" and uni_conver == "mililitro":
    resultado = l_ml(valor)
    print(resultado)
elif uni_medida == "mililitro" and uni_conver == "litro":
    resultado = ml_l(valor)
    print(resultado)
else:
    print("Unidade de medida ou de conversão inválida")
