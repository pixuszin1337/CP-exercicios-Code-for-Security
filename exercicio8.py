def calcular_horas(entrada, saida):

    if saida >= entrada:
        return saida - entrada

    else:
        return (24 - entrada) + saida


def calcular_estacionamento(entrada, saida, placa, dia):

    horas = calcular_horas(entrada, saida)

    if horas == 0:
        horas = 1

    if horas == 1:
        total = 10.00

    else:
        total = 10.00 + (horas - 1) * 5.00

    adicional_noturno = 0

    hora_atual = entrada
    for i in range(horas):
        hora_atual = (entrada + i) % 24
        if hora_atual >= 22 or hora_atual < 6:
            adicional_noturno = total * 0.50
            total = total + adicional_noturno
            break

    desconto = 0

    if dia == "segunda" and placa % 2 == 0:
        desconto = total * 0.10
        total = total - desconto

    print(f"entrada: {entrada}h saida: {saida}h")
    print(f"horas: {horas}")
    print(f"total base: {total}")
    print(f"adicional noturno: {adicional_noturno}")
    print(f"desconto segunda: {desconto}")
    print(f"total final: {total}")


entrada = int(input("hora de entrada: "))
saida = int(input("hora de saida: "))
placa = int(input("ultimo numero da placa: "))
dia = input("dia da semana: ")

calcular_estacionamento(entrada, saida, placa, dia)
