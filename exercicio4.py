def classificador(valor_triangulo_1, valor_triangulo_2, valor_triangulo_3):

    if valor_triangulo_1 <= 0 or valor_triangulo_2 <= 0 or valor_triangulo_3 <= 0:

        return "nao forma triangulo(Lado zero)"
    
    elif valor_triangulo_1 + valor_triangulo_2 < valor_triangulo_3 or valor_triangulo_2 + valor_triangulo_3 < valor_triangulo_1 or valor_triangulo_1 + valor_triangulo_3 < valor_triangulo_2:

        return "nao forma triangulo"
    
    elif valor_triangulo_1 == valor_triangulo_2 == valor_triangulo_3:

        return "Triangulo Equilatero"
    
    elif valor_triangulo_1 == valor_triangulo_2 or valor_triangulo_1 == valor_triangulo_3 or valor_triangulo_2 == valor_triangulo_3:

        return "Triangulo Isosceles"
    
    elif valor_triangulo_3 != valor_triangulo_2 != valor_triangulo_3:

        return "Triangulo Escaleno"


valor_triangulo_1 = int(input("Digite o primeiro valor do triangulo: "))
valor_triangulo_2 = int(input("Digite o segundo valor do triangulo: "))
valor_triangulo_3 = int(input("Digite o terceiro valor do triangulo: "))


print(classificador(valor_triangulo_1, valor_triangulo_2, valor_triangulo_3))