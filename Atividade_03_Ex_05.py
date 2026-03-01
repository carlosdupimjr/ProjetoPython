import math
#Declaração de variáveis

coefA: float = 0
coefB: float = 0
coefC: float = 0
delta: float = 0
raiz1: float = 0
raiz2: float = 0

#Início

coefA = float(input('Informe o valor do coeficiente A:'))
coefB = float(input('Informe o valor do coeficiente B:'))
coefC = float(input('Informe o valor do coeficiente C:'))
delta = ((coefB**2)-(4*(coefA*coefC)))

raiz1 = (((coefB*(-1))+(math.sqrt(delta)))/(2*coefA))
raiz2 = (((coefB*(-1))-(math.sqrt(delta)))/(2*coefA))

print('A equação de segundo grau é ', coefA, '* X^2 +', coefB, '* X', '+', coefC,'= 0')
print('As raízes da equação de segundo grau são:', raiz1, 'e', raiz2,'.')

#Fim