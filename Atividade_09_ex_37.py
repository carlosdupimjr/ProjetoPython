import os

#Início

# Procedimento para gravar a sequência
def gravar_fibonacci(valor1, caminho):
    fibStart = 0
    fibNext = 1
    fibIndx = 1
   
    pasta = os.path.dirname(caminho)
    os.makedirs(pasta, exist_ok=True)

    while fibIndx <= valor1:
        print(fibStart)
        
        if fibIndx == 1:
            with open(caminho, "w") as arquivo:
                arquivo.write(f"{fibStart}\n")
        else:            
            with open(caminho, "a") as arquivo:
                arquivo.write(f"{fibStart}\n")

        fibNext2 = fibStart + fibNext
        fibStart = fibNext
        fibNext = fibNext2
        fibIndx += 1

# Função principal
def main():
    dir = 'C:\\temp\\'
    arq = 'ex37.txt'
    caminho = dir + arq

    valor1 = int(input('Indique o valor para o cálculo da sequência de Fibonacci: '))

    if valor1 <= 0:
        print('Valor inválido, favor digitar um número inteiro positivo.')
    else:
        gravar_fibonacci(valor1, caminho)
        print("Documento gravado em ", caminho)


if __name__ == "__main__":
    main()