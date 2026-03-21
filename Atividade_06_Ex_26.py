#Declaração de variáveis

valor1: int = 0
valor2: int = 0

#Início
def main():
    global valor1
    global valor2
    valor1 = int(input('Insira o primeiro valor: '))
    valor2 = int(input('Insira o segundo valor: '))
    multiplo()

def multiplo():
    if (valor1 > valor2):
        if (valor1%valor2 == 0):
            print('O valor',valor1,'é um múltiplo do valor',valor2,'.')
        else:
            print('O valor',valor1,'não é um múltiplo do valor',valor2,'.')
    elif (valor1 < valor2):
        if (valor2%valor1) == 0:
            print('O valor',valor2,'é um múltiplo do valor',valor1,'.')
        else:
            print('O valor',valor2,'não é um múltiplo do valor',valor1,'.')
    else:
        print('Os valores são iguais.')

if (__name__=='__main__'):
    main()

#Fim