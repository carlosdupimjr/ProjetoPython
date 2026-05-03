import platform
import subprocess

def chamada():
    system: str = platform.system()
    return system

def processosWindows():
    print('Seu sistema operacional é o Windows.\n')
    processoSelecionado: int = 0
    
    while (processoSelecionado <1 or (processoSelecionado >3 and processoSelecionado !=9)):
        processoSelecionado = int(input('Selecione uma das seguintes opções: \n1 - Listar processos \n2 - Matar por PID (ID processo)\n3 - Matar por nome do processo\n9 - Encerrar aplicação\nOpção: '))
        if (processoSelecionado <1 or (processoSelecionado >3 and processoSelecionado !=9)):
            print('Opção inávlida. Favor selecionar novamente.\n')
    funcAcaoWin(processoSelecionado)

def funcAcaoWin(opcao): #notepad 2816
    acao: str = ''
    pidWin: str = ''
    nameWin: str = ''
    killWin: str = ''

    if opcao == 1:
        acao = 'TASKLIST /FO TABLE'
        subprocess.run(acao)
    
    elif opcao == 2:
        acao = 'TASKKILL /PID '
        pidWin = input('Favor indicar o PID do processo a ser morto: ')
        killWin = acao + pidWin
        subprocess.run(killWin)
    
    elif opcao == 3:
        acao = 'TASKKILL /IM '
        nameWin = input('Favor indicar o nome do processo a ser morto: ')
        killWin = acao + nameWin
        subprocess.run(killWin)

    else:
        encerrar()

def processosLinux():
    print('Seu sistema operacional é o Linux.\n')
    processoSelecionado: int = 0
    
    while (processoSelecionado <1 or (processoSelecionado >3 and processoSelecionado !=9)):
        processoSelecionado = int(input('Selecione uma das seguintes opções: \n1 - Listar processos \n2 - Matar por PID (ID processo)\n3 - Matar por nome do processo\n9 - Encerrar aplicação\nOpção: '))
        if (processoSelecionado <1 or (processoSelecionado >3 and processoSelecionado !=9)):
            print('Opção inávlida. Favor selecionar novamente.\n')
    funcAcaoLinux(processoSelecionado)

def funcAcaoLinux(opcao):
    pidLinux: str = ''
    nameLinux: str = ''

    if opcao == 1:
        subprocess.run(['ps','-ef'])
    
    elif opcao == 2:
        pidLinux = input('Favor indicar o PID do processo a ser morto: ')
        subprocess.run(['kill','-9',pidLinux])
    
    elif opcao == 3:
        nameLinux = input('Favor indicar o nome do processo a ser morto: ')
        subprocess.run(['pkill','-f', nameLinux])

    else:
        encerrar()

def encerrar():
    print('Encerrando o programa.')

def main():
    nomeSO: str = ''
    nomeSO = chamada()

    if (nomeSO == 'Windows'):
        processosWindows()
    
    elif(nomeSO == 'Linux'):
        processosLinux()
    
    else:
        print('Sistema Operacional não aplicável.')



if (__name__=='__main__'):
    main()