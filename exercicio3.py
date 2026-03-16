import os

def conversor(escolha_conversao, quantidade_dinheiro = float):

    if escolha_conversao == 1:
    
        os.system('cls')
        return quantidade_dinheiro * 5.15
    
    elif escolha_conversao == 2:

        os.system('cls')
        return quantidade_dinheiro * 5.55
    
    elif escolha_conversao == 3:
        
        os.system('cls')
        return quantidade_dinheiro * 6.45
    
    else:
        
        return "opcao invalida"
    

quantidade_dinheiro = float(input(" Digite a quantidade que voce quer converter: "))

escolha_conversao = int(input(" [1] REAL -> DOLAR \n [2] REAL -> EURO \n [3] REAL -> LIBRA\n\n"))

print(f'Conversao: {conversor(escolha_conversao, quantidade_dinheiro)}')