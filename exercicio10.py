import math


def calculadora_inss(salario_bruto: float):
 

    subtracao_final = 0
    
    # Faixa 1
    if salario_bruto > 0:

        variavel_descartavel = min(salario_bruto, 1518.00)
        subtracao_final += variavel_descartavel * 0.075


    # Faixa 2
    if salario_bruto > 1518.00:

        variavel_descartavel = min(salario_bruto, 2793.88)
        subtracao_final += (variavel_descartavel - 1518.00) * 0.09


    # Faixa 3
    if salario_bruto > 2793.88:

        variavel_descartavel = min(salario_bruto, 4190.83)
        subtracao_final += (variavel_descartavel - 2793.88) * 0.12


    # Faixa 4
    if salario_bruto > 4190.83:

        variavel_descartavel = min(salario_bruto, 8157.41)
        subtracao_final += (variavel_descartavel - 4190.83) * 0.14 

    return subtracao_final  


def base_ir():

    resultado = 0
    base = 0

    base += inss

    base += pensao_alimenticia

    base += numero_dependentes * 189.59

    if idoso == 1:
        
        base += 1903.98
    

    resultado = salario_bruto - base

    return resultado


def calculadora_ir(base):
    
    pipipipopopo = 0

    if base > 2259.20:
        
        variavel_descartavel = min(base, 2826.65)
        pipipipopopo += (variavel_descartavel - 2259.20) * 0.075
    
    if base > 2826.65:

        variavel_descartavel = min(base, 3751.05)
        pipipipopopo += (variavel_descartavel - 2826.65) * 0.15

    if base > 3751.05:

        variavel_descartavel = min(base, 4664.68)
        pipipipopopo += (variavel_descartavel - 3751.05) * 0.225
    
    if base > 4664.68:

        pipipipopopo += (base - 4664.68) * 0.275


    return pipipipopopo

        


salario_bruto = float(input("\nDigite seu salario bruto mensal: "))
numero_dependentes = int(input("\nDigite o numero de dependentes: "))
pensao_alimenticia = float(input("\nValor da pensao alimenticia(se não paga, digite 0):"))
idoso = int(input("\nVocê é um idoso? 1 para sim e 0 para não: "))



inss = calculadora_inss(salario_bruto)
base = base_ir()
ir = calculadora_ir(base)

menorop = min(inss, ir)
maiorop = max(inss, ir)
si = salario_bruto - (maiorop + menorop)

# print(f"\n{base_ir()}") # <- so pra ver se a base esta funcionando corretamente


print(f"\n\n\n\n\n[+] INSS: {inss:.2f}")

print (f"\n[+] IR: {ir:.2f}\n")

print (f"[+] Salário liquido: {si:.2f}\n")
