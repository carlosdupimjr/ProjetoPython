#Declaração de variáveis

valor1: int = 0
valorCalc: float = 1

#Início

valor1 = int(input('Indique o valor para cálculo: '))

for i in range (1, valor1+1, 1):
    valorCalc = valorCalc + (1/i)

print('O valor do cálculo é igual a:',valorCalc,'.')


#Fim