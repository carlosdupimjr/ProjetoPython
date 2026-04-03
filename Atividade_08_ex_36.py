#Início

import os

def fatorial(fatorN):
    resultado = 1
   
    for i in range(1, fatorN + 1):
        resultado = resultado * i
   
    return resultado


def divisao(denomN):
    denominador:int = fatorial(denomN)
    divisaoFat:float = 1/denominador
    
    return divisaoFat


def lerNumero():
    
    return int(input('Indique o valor para o cálculo: '))


def calcValor(n1, arquivo):
    valorCalc = 1.0

    arquivo.write("Soma das frações fatoriais:\n")
    arquivo.write("1/0! = 1.0\n")

    for i in range(1, n1 + 1, 1):
        termo = divisao(i)
        valorCalc = valorCalc + termo

        arquivo.write("1/" + str(i) + "! = " + str(termo) + "\n")

    return valorCalc


def gravarArquivo():
    dir = '/tmp/exercicios/'
    arq = 'ex36.txt'
    caminho = dir + arq

    if not os.path.exists(dir):
        os.mkdir(dir)
        os.chmod(dir, 0o744)

    with open(caminho, "w") as arquivo:
        valorN:int = lerNumero()

        resultado:float = calcValor(valorN, arquivo)

        arquivo.write("\n")
        arquivo.write("Resultado final: " + str(resultado) + "\n")

        print('Resultado final:', resultado)


def main():
    gravarArquivo()


if __name__ == "__main__":
    main()

#Fim