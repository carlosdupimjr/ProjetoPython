#Declaração de variáveis

numBase: float = 0
numExpoente: int = 0
numPotencia: float = 0

#Início

numBase = float(input('Indique o valor da base: '))
numExpoente = int(input('Indique o valor do expoente: '))

numPotencia = numBase

for i in range (numExpoente,1,-1):
    numPotencia = numPotencia * numBase

print('A potência de',numBase,'elevado a',numExpoente,'é igual a',numPotencia)

#Fim