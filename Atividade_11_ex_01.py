# 1) Fazer uma aplicação que rode 5 Threads que cada uma delas receba um inteiro chamado id como parâmetro e imprima no console o texto “Thread #” + id. Antes de imprimir o valor, deve-se fazer um sleep de 0.5 segundos.

import multiprocessing
import time

def executar_processo(id):
    time.sleep(0.5)
    print(f"Thread #{id+1}")


def main():
    args: int = [0]*5

    for i in range (5):
        args[i] = i
    with multiprocessing.Pool(processes = 5) as pool:
        pool.map (executar_processo, args)


if (__name__=='__main__'):
    main()