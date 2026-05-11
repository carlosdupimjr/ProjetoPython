import platform
import subprocess
import multiprocessing

def nameOS():
    system: str = ''
    system = platform.system()
    return system

def procPing(nomeServidor, url, nomeSO):
    comando: str = ''
    if (nomeSO == 'Windows'):
        comando = f'ping -4 -n 10 {url}'
    elif (nomeSO == 'Linux'):
        comando = f'ping -4 -c 10 {url}'
    else:        
        abort()
        return
        
    lerProcesso(comando, nomeSO, nomeServidor)

def lerProcesso(comando, nomeSO, nomeServidor):
    vet_proc = comando.split(' ')
    linha = ' '
    
    saida = subprocess.Popen(vet_proc, stdout=subprocess.PIPE)
    linha = saida.stdout.readline().decode('utf-8', errors='ignore')
    
    media = 'Não identificado'

    while (linha != ''):
        linha_limpa = linha.strip()
        
        if (nomeSO == 'Windows'):
            
            if ('tempo=' in linha_limpa or 'tempo<' in linha_limpa):
                partes = linha_limpa.split()
                item_tempo = [p for p in partes if 'tempo' in p][0]
                
                tempo = item_tempo.replace('tempo=', '').replace('tempo<', '').replace('ms', '')
                print(f'[{nomeServidor}] Iteração: {tempo}ms')


            if ('M' in linha and 'dia' in linha and '=' in linha):
               
                if 'Mdia =' in linha_limpa:
                    media = linha_limpa.split('Mdia = ')[-1].strip()
                elif 'Média =' in linha_limpa:
                    media = linha_limpa.split('Média = ')[-1].strip()
                elif 'Average =' in linha_limpa:
                    media = linha_limpa.split('Average = ')[-1].strip()
                
            linha = saida.stdout.readline().decode('utf-8', errors='ignore')
        else:
            
            if ('time=' in linha_limpa):
                tempo = linha_limpa.split('time=')[-1].split()[0]
                print(f'[{nomeServidor}] Iteração: {tempo} ms')

            
            if ('rtt' in linha_limpa and '/' in linha_limpa and '=' in linha_limpa):
                valores = linha_limpa.split('=')[-1].strip()
                parte = valores.split('/')
                media = parte[1] + ' ms'
                
            linha = saida.stdout.readline().decode('utf-8', errors='ignore')

    print(f'>>> FIM - Servidor: {nomeServidor} | Tempo Médio: {media}')

def abort():
    print('Sistema operacional não compatível.')

def main():
    nomeSistema: str = ''
    nomeSistema = nameOS()

    if (nomeSistema != 'Windows' and nomeSistema != 'Linux'):
        abort()
        return

    args = [
        ("UOL", "uol.com.br", nomeSistema),
        ("Terra", "terra.com.br", nomeSistema),
        ("Google", "google.com.br", nomeSistema)
    ]

    with multiprocessing.Pool(processes=3) as pool:
        pool.starmap(procPing, args)

if (__name__=='__main__'):
    main()
