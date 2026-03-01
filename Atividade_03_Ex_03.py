#Declaração de variáveis

base: float = 0
altura: float = 0
area: float =0

#Início

base = float(input('Informe o valor da base do triângulo, em centímetros:'))
altura = float(input('Informe o valor da altura do triângulo, em centímetros:'))
area = (base*altura)/2

print('O valor da área de um triângulo com', base, 'cm de base, e', altura, 'cm de altura é', area,'cm.')

#Fim