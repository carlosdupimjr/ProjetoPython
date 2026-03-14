#Declaração de variáveis

valorN: int = 0
maiorValor: int = 0
menorValor: int = 0
quantNumeros: int = 1

#Início

while (quantNumeros <=100):
    valorN = int(input('Indique um valor inteiro real: '))
    if (quantNumeros == 1):
         menorValor = valorN
         maiorValor = valorN
    else:
        if valorN > maiorValor:
                maiorValor = valorN
        else:
            if valorN < menorValor:
                menorValor = valorN
    quantNumeros +=1

print('O menor valor é:',menorValor)
print('O maior valor é:',maiorValor)


#Fim