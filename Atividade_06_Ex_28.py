#Declaração de variáveis

precoAtual: float = 0
mediaMensal: int = 0

#Início

def calcPreco(preco,media):
    precoNovo: float = 0.0
    if ((media < 500) and (preco < 30)):
        precoNovo = preco * 1.1
    elif ((media >= 500 and media < 1000) and (preco >= 30 and preco < 80)):
        precoNovo = preco * 1.15
    elif ((media >= 1000) and (preco >=80)):
        precoNovo = preco * 0.95
    else:
        precoNovo = preco
    print('O novo preço do produto será R$:',precoNovo,'.')

def main():
    global precoAtual
    global mediaMensal
    precoAtual = float(input('Indique o preço atual do produto: '))
    mediaMensal = int(input('Indique a média mensal de vendas do produto: '))
    calcPreco(precoAtual,mediaMensal)



if(__name__=='__main__'):
    main()

#Fim