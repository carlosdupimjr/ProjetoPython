#Declaração de variáveis

valor1: int = 0
valor2: int = 0
indice: int = 0
somaImpar: int = 0

#Início

valor1 = int(input('Indique o primeiro valor: '))
valor2 = int(input('Indique o segundo valor: '))

if (valor1 > valor2):
    if (valor2 % 2 == 0):
        indice = valor2 + 1
    else:
        indice = valor2 + 2
    while indice < valor1:
        somaImpar = (indice + somaImpar)
        indice += 2
    print('A soma de números ímpares entre',valor2,'e',valor1,'é igual a',somaImpar,'.')
elif (valor1 < valor2):
    if (valor1 % 2 == 0):
        indice = valor1 + 1
    else:
        indice = valor1 + 2
    while (indice < valor2):
        somaImpar = (indice + somaImpar)
        indice +=2
    print('A soma de números ímpares entre',valor1,'e',valor2,'é igual a',somaImpar,'.')

else:
    print('Os valores são idênticos.')

#Fim