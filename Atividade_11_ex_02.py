import multiprocessing
import time
import random


# Função executada pelos processos
def calcular_soma(parametros):

    id_linha:int = parametros[0]
    valores:int = parametros[1]

    soma:int = 0

    for valor in valores:
        soma += valor
        time.sleep(0.2)

    print(f"Linha {id_linha} -> Valores: {valores} -> Soma = {soma}")


def main():

    lista_parametros:int = []

    # Criando os parâmetros para 3 processos
    for i in range(5):

        id: int = i

        var1: int = random.randint(1, 100)
        var2: int = random.randint(1, 100)
        var3: int = random.randint(1, 100)
        var4: int = random.randint(1, 100)
        var5: int = random.randint(1, 100)

        # Vetor com os 5 valores
        valores: int = [var1, var2, var3, var4, var5]

        # Vetor de parâmetros
        parametros = [id, valores]

        lista_parametros.append(parametros)

    # Pool de processos
    with multiprocessing.Pool(processes=3) as pool:

        # Executa a função para cada conjunto de parâmetros
        pool.map(calcular_soma, lista_parametros)

    print("Todos os processos finalizaram.")


if (__name__ == '__main__'):
    main()