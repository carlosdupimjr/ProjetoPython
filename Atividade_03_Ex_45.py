#Declaração de variáveis

valorNum: int = 2
valorDenom: int = 4
valorResult: float = 0
total: float = 1
indice: int = 3

#Início

while (valorNum <= 15):
    valorResult = (valorNum/valorDenom)
    if (valorNum%2 == 0):
        total = total - (valorResult)
    else:
        total = total + (valorResult)
    print(valorResult)
    indice = indice + 2
    valorNum = valorNum + 1
    valorDenom = valorDenom + indice
    

print('O valor resultante é:',total)


#Fim