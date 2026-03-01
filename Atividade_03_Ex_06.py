#Declaração de Variáveis

valorX: int = 0
valorY: int = 0
valorZ: int = 0

#Início

valorX = int(input('Informe o valor X:'))
valorY = int(input('Informe o valor Y:'))

valorZ = valorX
valorX = valorY
valorY = valorZ

print('O valor de x é:', valorX)
print('O valor Y é de:', valorY)

#Fim