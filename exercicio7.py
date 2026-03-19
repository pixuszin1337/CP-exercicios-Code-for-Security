def calcular_cedulas(valor):

    if valor <= 0:
        return "valor invalido"

    if valor % 10 != 0:
        return "valor invalido, precisa ser multiplo de 10"

    cedula_200 = valor // 200
    valor = valor - cedula_200 * 200

    cedula_100 = valor // 100
    valor = valor - cedula_100 * 100

    cedula_50 = valor // 50
    valor = valor - cedula_50 * 50

    cedula_20 = valor // 20
    valor = valor - cedula_20 * 20

    cedula_10 = valor // 10

    total = cedula_200 + cedula_100 + cedula_50 + cedula_20 + cedula_10

    print(f"R$200: {cedula_200}")
    print(f"R$100: {cedula_100}")
    print(f"R$50: {cedula_50}")
    print(f"R$20: {cedula_20}")
    print(f"R$10: {cedula_10}")
    print(f"total de cedulas: {total}")


valor = int(input("valor do saque: "))

resultado = calcular_cedulas(valor)

if resultado:
    print(resultado)
