#Declaração de Variáveis

anguloA: float = 0
anguloB: float = 0
anguloC: float = 0

#Início

anguloA = float(input('Informe o primeiro ângulo do triângulo: '))
anguloB = float(input('Informe o segundo ângulo do triângulo: '))

anguloC = (180-(anguloA+anguloB))

print('O terceiro ângulo do triângulo é de', anguloC, 'graus.')

#Fim