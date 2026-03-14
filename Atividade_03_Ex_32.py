#Declaração de variáveis

valor1: int = 0
contador = 1
valorFinal: int = 1

#Início

valor1 = int(input('Indique o valor inteiro: '))

if (valor1 != 0):
    while (contador <= valor1):
          valorFinal = contador * valorFinal
          contador += 1
    print('O valor fatorial de',valor1,'! é igual a',valorFinal,'.')
else:
     print('O fatorial de 0 é igual a 0.')

#Fim