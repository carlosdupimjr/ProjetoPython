#Declaração de variáveis

valor1: int = 0
valor2: int = 0
numPrimo: int = 0
raizNum: int = 0
indice: int = 0
contador: int = 0
valorTroca: int = 0

#Início

valor1 = int(input('Indique o primeiro valor: '))
valor2 = int(input('Indique o segundo valor: '))

if (valor1 > valor2):
    valorTroca = valor1
    valor1 = valor2
    valor2 = valorTroca

if (valor1 <= 0):
    numPrimo = 2
else:
    numPrimo = (valor1 + 1)

while (numPrimo < valor2):
    contador = 0
    raizNum = int(numPrimo ** 0.5)
    indice = raizNum

    while (indice > 1):
        if ((numPrimo % indice) == 0):
            contador += 1
        indice -=1

    if contador == 0:
        print(numPrimo)

    numPrimo = numPrimo + 1

#Fim
