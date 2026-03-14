#Declaração de variáveis

valor1: int = 0
valorTabuada: int = 0
#Início

valor1 = int(input('Indique o valor para cálculo da tabuada: '))

for i in range (1, 11, 1):
    valorTabuada = (valor1*i)
    print(valor1,'x',i,'=',valorTabuada)

#Fim