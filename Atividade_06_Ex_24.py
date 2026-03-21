#Declaração de variáveis

valor1: int = 0

#Início

def main():
    global valor1
    valor1 = int(input('Digite o valor: '))
    divisivel()

def divisivel():
    if valor1%2 == 0 and valor1%3 == 0:
        print('O valor',valor1,'é divisível por 2 e por 3.')
    elif valor1%2 == 0 and valor1%3 != 0:
        print('O valor',valor1,'é divisível por 2, mas não é divisível por 3.')
    elif valor1%2 != 0 and valor1%3 == 0:
        print('O valor',valor1,'não é divisível por 2, mas é divisível por 3.')
    else:
        print('O valor',valor1,'não é divisível por 2 nem por 3.')
if (__name__=='__main__'):
    main()
#Fim