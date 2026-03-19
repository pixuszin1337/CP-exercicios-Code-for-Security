def calcular_desconto(valor, vip):

    desconto = 0

    if valor < 0:
        return "Valor invalido"

    if valor <= 100:
        desconto = 0

    elif valor <= 300:
        desconto = valor * 0.10

    elif valor <= 500:
        desconto = valor * 0.15

    else:
        desconto = valor * 0.20

    desconto_vip = 0

    if vip == "sim":
        desconto_vip = valor * 0.05

    valor_final = valor - desconto - desconto_vip

    print(f"valor original: {valor}")
    print(f"desconto: {desconto}")
    print(f"desconto vip: {desconto_vip}")
    print(f"valor final: {valor_final}")


valor = float(input("valor da compra: "))
vip = input("cliente vip? sim ou nao: ")

calcular_desconto(valor, vip)
