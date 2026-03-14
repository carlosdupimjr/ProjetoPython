#Declaração de Variáveis

valor1: int = 0
valor2: int = 0
resultado: int = 0

#Início

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

if valor1 > valor2:
    resultado = valor1 - valor2
else:
    resultado = valor2 - valor1

print('O resultado da subtração do maior valor pelo menor valor é: ', resultado, '.')

#Fim