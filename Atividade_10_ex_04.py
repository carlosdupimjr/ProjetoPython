import platform
import subprocess

def nameOS():
    system: str = ''
    system = platform.system()
    return system

def procPing(nomeSO):
    comando: str = ''
    vet_proc: str = []
    linha: str = ''
    saida: str = ''
    valor: str = ''
    parte: str = ''
    media: str = ''

    if (nomeSO == 'Windows'):
        comando = 'ping -4 -n 10 www.google.com.br'
    elif (nomeSO == 'Linux'):
        comando = 'ping -4 -c 10 www.google.com.br'
    else:        
        abort()
    lerProcesso(comando,nomeSO)

def lerProcesso(comando, nomeSO):
    vet_proc = comando.split(' ')
    print(vet_proc)
    #subprocess.run(vet_proc)
    linha = ' '
    saida = subprocess.Popen(vet_proc, stdout=subprocess.PIPE)
    linha = saida.stdout.readline().decode('utf-8', errors='ignore')
    while (linha != ''):
        if (nomeSO == 'Windows'):
            if ('M' in linha and 'dia' in linha):
                valor = linha.split('Mdia = ')[1].strip()
                print(f'Média Windows = {valor}.')
            linha = saida.stdout.readline().decode('utf-8', errors='ignore')
        else:
            if ('avg' in linha and '=' in linha):
                valor = linha.split('=')[1].strip()
                parte = valor.split('/')
                media = parte[1] + 'ms'
                print(f'Média Linux = {media}.')
            linha = saida.stdout.readline().decode('utf-8', errors='ignore')

    

def main():
    nomeSistema: str =''
    nomeSistema = nameOS()
    procPing(nomeSistema)

def abort():
    print('Sistema operacional não compatível.')

if (__name__=='__main__'):
    main()