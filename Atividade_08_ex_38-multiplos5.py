import os

# Função para verificar se uma linha é um número válido
def NumeroValido(linha):
    linha = linha
    if linha == "":
        return False
    if "Menor" in linha or "Maior" in linha:
        return False
    try:
        int(linha)
        return True
    except ValueError:
        return False

# Função para verificar se um número é múltiplo de 5
def MultiploDe5(numero):
    return numero % 5 == 0

# Função principal que lê um arquivo e grava múltiplos de 5
def filtrarMultiplosDe5(arquivo_entrada, arquivo_saida):
    if not os.path.exists(arquivo_entrada):
        print("Arquivo de entrada não encontrado!")
        return

    with open(arquivo_entrada, "r") as entrada, open(arquivo_saida, "w") as saida:
        for linha in entrada:
            if NumeroValido(linha):
                numero = int(linha)
                if MultiploDe5(numero):
                    saida.write(str(numero) + "\n")

    print("Números múltiplos de 5 gravados em '" + str(arquivo_saida) + "'")

# Função principal
def main():
    dir = '/tmp/exercicios/'
    arquivo_entrada = os.path.join(dir, 'ex38.txt')
    arquivo_saida = os.path.join(dir, 'ex38_multiplos5.txt')

    filtrarMultiplosDe5(arquivo_entrada, arquivo_saida)

if (__name__ == "__main__"):
    main()