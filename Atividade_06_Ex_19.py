#Declaração de variáveis

valor1: float = 0
valor2: float = 0

#Início

def maiorValor():
    if valor1 > valor2:
        print('O maior valor entre os valores fornecidos é o primeiro: ', valor1, '.')
    elif valor2 > valor1:
        print('O maior valor entre os valores fornecidos é o segundo: ', valor2, '.')
    else:
        print('Os valores são idênticos, não é possível trazer o maior deles.')

def main():
    global valor1
    global valor2
    valor1 = float(input('Insira o primeiro valor: '))
    valor2 = float(input('Insira o segundo valor: '))
    maiorValor()

if (__name__ == '__main__'):
    main()

#Fim