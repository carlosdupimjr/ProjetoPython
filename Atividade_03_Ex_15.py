#Declaração de Variáveis

cateto1: float = 0
cateto2: float = 0
hipotenusa: float = 0

#Início

cateto1 = float(input('Informe o primeiro cateto do triângulo, em centímetros: '))
cateto2 = float(input('Informe o segundo cateto do triângulo, em centímetros: '))

hipotenusa = (((cateto1**2) + (cateto2**2))**0.5)

print('O valor da hipotenusa é de', hipotenusa, "cm.")

#Fim