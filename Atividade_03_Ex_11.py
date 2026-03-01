import math

#Declaração de Variáveis

raio: float = 0
comprimento: float = 0

#Início

raio = float(input('Inform o raio da circunferência em cm: '))

comprimento = math.pi*raio*2

print('O comprimento da circunferência é: ', comprimento,'cm')


#Fim