import multiprocessing
import time
import random

pos_chegada = None
espera_chegada = None
semaforo = None


def init(cheg, espera, sem):
    global pos_chegada
    global espera_chegada
    global semaforo

    pos_chegada = cheg
    espera_chegada = espera
    semaforo = sem


def pessoa(id):
    pessoa_andando(id)
    
    with espera_chegada:
        pos_chegada.value += 1
        ordem = pos_chegada.value

    print(f'Pessoa #{id} foi a {ordem}ª a chegar na porta.')
    
    with semaforo:
        pessoa_cruzando(id)

    pessoa_saindo(id)


def pessoa_andando(id):
    dist = 0
    dist_total = 200

    velocidade = random.randint(4, 6)

    while dist < dist_total:
        dist += velocidade

        if dist > dist_total:
            dist = dist_total

        print(f'Pessoa #{id} percorreu {dist} m.')
        time.sleep(1)

    print(f'Pessoa #{id} chegou à porta.')


def pessoa_cruzando(id):
    tempo_porta = random.uniform(1, 2)

    print(f'Pessoa #{id} está atravessando a porta.')
    time.sleep(tempo_porta)


def pessoa_saindo(id):
    print(f'Pessoa #{id} cruzou a porta.\n')


def main():
    i: int = 0
    chegada = multiprocessing.Value('i', 0)

    espera = multiprocessing.Lock()

    pessoas = [0]*4

    for i in range(4):
        pessoas[i]=i

    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)

        with multiprocessing.Pool(processes=4,initializer=init,initargs=(chegada, espera, sem)) as pool:

            pool.map(pessoa, pessoas)


if __name__ == '__main__':
    main()