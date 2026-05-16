import multiprocessing
import time
import random

pista_sem = None
equipe_sem = None


def init(p_sem, e_sem):
    global pista_sem
    global equipe_sem

    pista_sem = p_sem
    equipe_sem = e_sem


def carro(args):
    equipe_id, carro_id = args
    nome: str = ''
    tempo: float = 0.0
    global pista_sem
    global equipe_sem

    nome = (f'Equipe {equipe_id+1} - Carro {carro_id+1}')

    with equipe_sem[equipe_id]:
        with pista_sem:
            print(f'{nome} entrou na pista')

            for volta in range(1, 4):
                tempo = random.randint(1000, 2000)
                tempo = tempo/1000
                time.sleep(tempo)
                print(f'{nome} - volta {volta}: {tempo}s')

            print(f'{nome} saiu da pista')


def main():
    equipe: int = 0
    carro_id: int = 0
    params = []

    with multiprocessing.Manager() as manager:

        pista = manager.Semaphore(5)
        equipes = [manager.Semaphore(1) for _ in range(7)]

        for equipe in range(7):
            for carro_id in range(2):
                params.append((equipe, carro_id))

        with multiprocessing.Pool(processes=14,initializer=init,initargs=(pista, equipes)) as pool:
            pool.map(carro, params)


if __name__ == "__main__":
    main()