# Exercício 2 
# Calculadora de IMC: Crie um programa que peça peso (kg) e altura (m)
# calcule o IMC (peso / altura²) e exiba a classificação: abaixo do peso (< 18.5), peso normal (18.5 - 24.9), sobrepeso (25.0 - 29.9), obesidade (≥ 30.0)
# Exiba o resultado com 1 casa decimal.


def CalculadoraIMC(imc: float):
    
    if imc >= 30.0:

        return "Obesidade"
    
    elif imc >= 25.0:
        
        return "Sobrepeso"
    

    elif imc >= 18.5:

        return "Peso normal"
    
    elif imc < 18.5:

        return "Abaixo do peso"
    
  
    


peso_variavel = int(input("Seu peso: "))
altura_variavel = float(input("Sua altura(Metros): "))

altura_variavel = altura_variavel * altura_variavel

# peso = peso_variavel * 10

# altura2 = altura_variavel * altura_variavel

# altura2 = altura2 * 10

imc = peso_variavel / altura_variavel

print(f"{imc}")

print(CalculadoraIMC(imc))


