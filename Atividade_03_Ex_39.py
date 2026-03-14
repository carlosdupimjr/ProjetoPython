#Declaração de variáveis

casa: int = 0
casaAtual: int = 0
quantidade: int = 1
total: int =0

#Início


casaAtual = int(input('Indique a casa que deseja saber a quantidade de grãoes que possui: '))

if (casaAtual <= 0 or casaAtual > 64):
    print('Valor de casa inválido, favor digitar número entre 1 e 64.')
else:
    for casa in range (1,65,1):
        total = total + quantidade
        quantidade = quantidade * 2
        if casa == casaAtual:
            print('A quantidade de grãoes na casa',casaAtual,'é de',total,'grãos.')

    print('A quantidade total de grãoes no tabuleiro é de',total,'grãos.')


#Fim