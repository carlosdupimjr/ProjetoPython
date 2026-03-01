#Declaração de Variáveis

comp: float=0
larg: float=0
altura: float=0
volume: float=0

#Início

comp = float(input('Informe o valor do comprimento em cm:'))
larg = float(input('Informe o valor da largura em cm:'))
altura = float(input('Informe o valor da altura em cm:'))

volume = comp*larg*altura

print('O volume do paralelepípedo é de ', volume, 'cm³.')

#Fim