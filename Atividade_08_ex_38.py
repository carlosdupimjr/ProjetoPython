import os

# Função para ler um número inteiro do usuário
def lerNumero():
    return int(input('Indique um valor inteiro: '))

# Função para atualizar maior e menor valor
def atualizarValores(valor1, menor, maior, primeiraVez):
    if primeiraVez == 1:
        return valor1, valor1
    else:
        if valor1 > maior:
            maior = valor1
        elif valor1 < menor:
            menor = valor1
        return menor, maior

# Procedimento para gravar no arquivo
def gravarArquivo():
    dir = '/tmp/exercicios/'
    arq = 'ex38.txt'
    caminho = dir + arq

    if not os.path.exists(dir):
        os.mkdir(dir)
        os.chmod(dir, 0o744)

    with open(caminho, "w") as arquivo:
        quantNumeros = 1
        menorValor = 0
        maiorValor = 0

        arquivo.write("Valores digitados:\n")

        while quantNumeros <= 100:
            valor = lerNumero()

            arquivo.write(str(valor) + "\n")

            menorValor, maiorValor = atualizarValores(
                valor, menorValor, maiorValor, quantNumeros
            )

            quantNumeros += 1

        arquivo.write("\n")
        arquivo.write("Menor valor: " + str(menorValor) + "\n")
        arquivo.write("Maior valor: " + str(maiorValor) + "\n")

        print('O menor valor é:', menorValor)
        print('O maior valor é:', maiorValor)

# Função principal
def main():
    gravarArquivo()

if __name__ == "__main__":
    main()