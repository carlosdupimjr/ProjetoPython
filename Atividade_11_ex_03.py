import multiprocessing
import time
import random


def puloSapo(num_sapo, distancia):

    salto = 0
    posicao = 0

    while posicao < distancia:

        salto = random.randint(1, 5)
        posicao += salto

        if posicao > distancia:
            posicao = distancia

        print(f'O sapo {num_sapo} deu um salto de {salto} cm, percorrendo {posicao} cm.')

        time.sleep(0.2)

    print(f'O sapo {num_sapo} completou a corrida!')


def main():

    args = []

    comprimento = int(input('Indique o tamanho do percurso, em centímetros: '))

    for count in range(5):
        args.append((count + 1, comprimento))

    with multiprocessing.Pool(processes=5) as pool:
        pool.starmap(puloSapo, args)


if __name__ == '__main__':
    main()