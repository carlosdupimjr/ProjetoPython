#Declaração de variáveis

valor1: int = 0
fibStart: int = 0
fibNext: int = 1
fibNext2: int = 0
fibIndx: int = 1
#Início

valor1 = int(input('Indique o valor para o cálculo da sequência de Fibonacci: '))

if (valor1 <= 0):
    print('Valor inválido, favor digitar um número inteiro positivo.')
else:
     while (fibIndx <= valor1):
        print('O',fibIndx,'º número da sequência de Fibonacci é: ',fibStart)
        fibNext2 = fibStart + fibNext
        fibStart = fibNext
        fibNext = fibNext2
        fibIndx +=1
#Fim