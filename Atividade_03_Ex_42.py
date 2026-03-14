#Declaração de variáveis

valorNum: int = 2
valorDenom: int = 3
valorResult: float = 0
total: float = 1

#Início

while (valorNum < 51):
    valorResult = (valorNum/valorDenom)
    total = total + (valorResult)    
    print(valorResult)
    valorNum = valorNum + 1
    valorDenom = valorDenom + 2
    

print('O valor resultante é:',total)


#Fim