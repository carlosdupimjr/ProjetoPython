#Declaração de variáveis

precoAtual: float = 0
mediaMensal: int = 0
precoNovo: float = 0

#Início

precoAtual = float(input('Indique o preço atual do produto: '))
mediaMensal = int(input('Indique a média mensal de vendas do produto: '))

if ((mediaMensal < 500) and (precoAtual < 30)):
    precoNovo = precoAtual * 1.1
elif ((mediaMensal >= 500 and mediaMensal < 1000) and (precoAtual >= 30 and precoAtual < 80)):
    precoNovo = precoAtual * 1.15
elif ((mediaMensal >= 1000) and (precoAtual >=80)):
    precoNovo = precoAtual * 0.95
else:
    precoNovo = precoAtual

print('O novo preço do produto será R$:',precoNovo,'.')
#Fim