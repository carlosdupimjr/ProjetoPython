#Declaração de Variáveis

valorInicial: float = 0
tempo: int=1
rendimento = 0.013
valorFinal: float=0

#Início

valorInicial = float(input('Informe o valor inicial do depósito em poupança: R$'))

valorFinal = (valorInicial+(valorInicial*(rendimento*tempo)))

print('O valor ajustado do investimento é de R$', valorFinal)

#Fim