import multiprocessing
import time
import random

#Declaração variáveis globais
distancia_corrida: int = 0
pos_chegada: int = 0
semaforo: None


def init(cheg, s, dist):
    global pos_chegada
    global semaforo
    global distancia_corrida

    pos_chegada = cheg
    semaforo = s
    distancia_corrida = dist


def sapo(id):
    global distancia_corrida
    global pos_chegada
    global semaforo
    
    sapo_pulando(id)

    with semaforo:
        sapo_chegando(id)


def sapo_pulando(id):
    global distancia_corrida

    dist_percorrida: int = 0
    pulo: int = 0

    while (dist_percorrida < distancia_corrida.value):
        pulo = random.randint(1, 5)
        print(f'O sapo #{id} deu um pulo de {pulo}cm.')

        dist_percorrida = dist_percorrida + pulo

        if (dist_percorrida > distancia_corrida.value):
            dist_percorrida = distancia_corrida.value

        time.sleep(0.5)
        print(f'O sapo #{id} percorreu {dist_percorrida}cm no total.')


def sapo_chegando(id):
    global pos_chegada
    global semaforo
    pos_chegada.value += 1
    colocacao = pos_chegada.value
    print(f'O sapo #{id} foi o {colocacao}º a chegar.')


def main():
    global distancia_corrida

    j: int = 0
    params: int = [0] * 5
    sem = None
    
    distancia_corrida = multiprocessing.Value('i', 0)
    distancia_corrida.value = int(input('Indique o tamanho total do percurso, em centímetros: '))
    chegada = multiprocessing.Value('i', 0)

    for j in range(5):
        params[j] = j

    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)

        with multiprocessing.Pool(processes=5,initializer=init,initargs=(chegada, sem, distancia_corrida)) as pool:
            pool.map(sapo, params)


if (__name__ == '__main__'):
    main()