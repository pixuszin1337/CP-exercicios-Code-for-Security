def defidor_de_idade(pessoa_idade_meses: int, idade_em_meses: int = 0):

    idade_em_meses = int(idade_em_meses)
 
    # considere os meses e se o mes for < 0 ou > que 12 devolva o erro "Mes Invalido"

    if pessoa_idade_meses < 0 or pessoa_idade_meses > 12:
        return "Meses Invalidos"

    if idade_em_meses < 0 or idade_em_meses > 1440:

        return "Idade inválida"

    elif idade_em_meses <= 132:

        return "Criança"

    elif idade_em_meses <= 204:

        return "Adolescente"

    elif idade_em_meses <= 708:

        return "Adulto"

    else:

        return "Idoso"
 
pessoa_idade = int(input("Digite sua idade(Anos): "))
pessoa_idade_meses = int(input("Digite sua idade(Meses): "))

meses_totais = pessoa_idade * 12 

meses_totais = meses_totais + pessoa_idade_meses


print(defidor_de_idade(pessoa_idade_meses, meses_totais))
 