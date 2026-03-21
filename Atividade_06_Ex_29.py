#Declaração de variáveis

tipoInvest: int = 0
valorInvest: float = 0
dias: int = 30
meses: int = dias/30

#Início

def calcValor(valor,tipo):
    valorFinal: float = 0
    global dias
    global meses
    if (tipo == 1):
        valorFinal = (valor * 1.03 * meses)
        print('O valor final do investimento em poupança após um mês será R$',valorFinal,'.')
    elif (tipo == 2):
        valorFinal = (valor * 1.05 * meses)
        print('O valor final do investimento em renda fixa após um mês será R$',valorFinal,'.')
    else:
        print('O tipo de investimento indicado é inválido.')

def main():
    global valorInvest
    global tipoInvest
    valorInvest = float(input('Indique o valor do investimento, em reais: '))
    tipoInvest = int(input('Indique o tipo de investimento, sendo 1 - poupança, ou 2 - renda fixa: '))
    calcValor(valorInvest,tipoInvest)


if(__name__=='__main__'):
    main()

#Fim