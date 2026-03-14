#Declaração de variáveis

valorN: int = 0
denominador: int = 1
valorCalc: float = 1

#Início

valorN = int(input('Indique o valor para o cálculo: '))

for i in range (1, valorN+1, 1):
    denominador = denominador * i
    valorCalc = valorCalc + (1/denominador)

print('O valor do cálculo é igual a:',valorCalc,'.')

#Fim