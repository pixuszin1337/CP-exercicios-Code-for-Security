def verificar_bissexto(ano):

    if ano % 400 == 0:
        return 1

    elif ano % 100 == 0:
        return 0

    elif ano % 4 == 0:
        return 1

    else:
        return 0


def dias_do_mes(mes, ano):

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30

    elif mes == 2:

        if verificar_bissexto(ano) == 1:
            return 29

        else:
            return 28


def verificar_data(dia, mes, ano):

    bissexto = verificar_bissexto(ano)

    if mes < 1 or mes > 12:
        print("mes invalido")
        return

    max_dias = dias_do_mes(mes, ano)

    if dia < 1 or dia > max_dias:
        print(f"data invalida, esse mes tem apenas {max_dias} dias")
        return

    print(f"data: {dia}/{mes}/{ano}")
    print(f"bissexto: {bissexto}")
    print("data valida")


dia = int(input("dia: "))
mes = int(input("mes: "))
ano = int(input("ano: "))

verificar_data(dia, mes, ano)
