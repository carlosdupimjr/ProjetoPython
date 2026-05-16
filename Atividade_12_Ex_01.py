import multiprocessing
import time
import random

# Declaração de variáveis globais
direcoes = ["Norte -> Sul", "Sul -> Norte", "Leste -> Oeste", "Oeste -> Leste"]
semaforo = None
sentido = None


def init(s, sen):
    global semaforo
    global sentido

    semaforo = s
    sentido = sen


def carro(id):
    global semaforo
    global sentido

    with semaforo:
        carro_passando(id)


def carro_passando(id):
    global sentido

    sentido.value = direcoes[id]

    print(f'O carro #{id} está passando no sentido: {sentido.value}')
    time.sleep(random.uniform(0.1,0.8))
    print(f'O carro #{id} saiu do cruzamento.')


def main():
    j = 0
    params = [0] * 4
    sem = None

    for j in range(4):
        params[j] = j

    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)
        sentido = manager.Value(str, "")

        with multiprocessing.Pool(processes=4,initializer=init,initargs=(sem, sentido)) as pool:

            pool.map(carro, params)


if __name__ == "__main__":
    main()