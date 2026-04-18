import os

#Início

# Procedimento de leitura
def ler_arquivo(caminho):
    with open(caminho, "r") as arquivo:
        for linha in arquivo:
            numero = int(linha.strip())

            resultado = validar_impar(numero)

            if resultado != -1:
                print(resultado)

# Função para validar se é ímpar
def validar_impar(numero):
    if numero % 2 != 0:
        return numero
    else:
        return -1

# Função principal
def main():
    dir = 'C:\\temp\\'
    arq = 'ex37.txt'
    caminho = dir + arq

    if not os.path.exists(caminho):
        print("Arquivo não encontrado!")
    else:
        ler_arquivo(caminho)

if __name__ == "__main__":
    main()