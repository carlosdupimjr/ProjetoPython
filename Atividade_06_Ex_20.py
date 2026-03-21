import math

#Declaração de variáveis

coefA: int = 0
coefB: int = 0
coefC: int = 0
delta: float = 0
raiz1: float = 0
raiz2: float = 0

#Início

def raizes():
    global delta
    global raiz1
    global raiz2
    delta = (coefB*coefB)-(4*coefA*coefC)

    if delta < 0:
        print('A equação não possui raízes reais.')
    elif delta == 0:
        raiz1 = ((coefB*-1) + math.sqrt(delta))/ (2*coefA)
        print('A equação possui 1 raíz real, sendo:', raiz1,'.')
    else:
        raiz1 = ((coefB*-1) + math.sqrt(delta))/ (2*coefA)
        raiz2 = ((coefB*-1) - math.sqrt(delta))/ (2*coefA)
        print('A equação possui 2 raízes reais, sendo:', raiz1,'e', raiz2,'.')

def main():
    global coefA
    global coefB
    global coefC
    coefA = int(input('Insira o coeficiente A: '))
    coefB = int(input('Insira o coeficiente B: '))
    coefC = int(input('Insira o coeficiente C: '))
    raizes()

if (__name__ == '__main__'):
    main()

#Fim