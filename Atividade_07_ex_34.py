import os

#Declaração de variáveis globais

valor: int = 0
dir: str = ''
arq: str = ''

#Início
    
def mult(vlr,tab):
        res: int = 0
        res = (vlr*tab)
        return res
         
def grava(c,rslt):
     global valor
     global dir
     global arq
     file: str = ''
     tipo: str = ''
     enc: str = ''
     linha: str = ''

     dir = '/tmp/exercicios/'
     arq = 'ex34.txt'
    
     if not os.path.exists(dir):
         os.mkdir(dir)
         os.chmod(dir, 0o744)

     linha = (str(valor))+(' x ')+(str(c))+(' = ')+(str(rslt))+('\n')

     if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        caminho = dir + arq
        enc = 'utf-8'
        if (os.path.exists(caminho) and os.path.isfile(caminho) and c>0):
            tipo = 'a'
        with open (caminho, tipo, encoding=enc) as file:
            file.write(linha)

     else:
        print('Diretório inválido!')   

def main():
    global valor
    contador: int = 0
    result: str = ''
        
    valor = int(input('Indique um valor entre 1 e 10 para cálculo da tabuada: '))
    if (valor < 1 or valor > 10):
        print('Valor inválido! Favor inserir número entre 1 e 10.')
    else:
        for contador in range (1,11,1):
            result = (mult(valor,contador))            
            print (result)
            grava(contador,result)

if (__name__ == '__main__'):
    main()

#Fim