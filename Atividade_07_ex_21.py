import os

#Declaração de variáveis globais
nome: str = ''
nota1: float = 0
nota2: float = 0
nota3: float = 0
nota4: float = 0
valor_media: float = 0
dir: str = ''
arq: str = ''
situacao: str = ''

#Início


def entrada():
    global nome
    global nota1
    global nota2
    global nota3
    global nota4
    global valor_media

    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Insira a nota do 1º bimestre: '))
    nota2 = float(input('Insira a nota do 2º bimestre: '))
    nota3 = float(input('Insira a nota do 3º bimestre: '))
    nota4 = float(input('Insira a nota do 4º bimestre: '))

    valor_media = med(nota1,nota2,nota3,nota4)
    print ('Média final é igual a: ' + str(valor_media))
    
    if (valor_media >= 6):
        situacao = 'APROVADO'
    elif (valor_media < 6 and valor_media >=3):
        situacao = 'EXAME'
    else:
        situacao = 'RETIDO'
        
    cadastro(nome,nota1,nota2,nota3,nota4,valor_media,situacao)

def med(n1,n2,n3,n4):
    media: float = 0
    media = (n1 + n2 + n3 + n4)/4
    return media

def cadastro(nm,nt1,nt2,nt3,nt4,vlr_med,status):
    linha: str = ''
    global arq
    global dir

    dir = '/tmp/exercicios/'
    arq = 'ex21.txt'

    if not os.path.exists(dir):
         os.mkdir(dir)
         os.chmod(dir, 0o744)

    linha = 'Aluno: ' + nm + '; Notas: ' + (str(nt1)) + '; ' + (str(nt2)) + '; ' + (str(nt3)) + '; ' + (str(nt4)) + '; Média final: ' +(str(vlr_med)) + '; Situação: ' + status + ('\n')
    escreveArq(dir,arq,linha)

def escreveArq(caminho,arquivo,linha_arq):
    file: str = ''
    tipo: str = ''
    enc: str = ''

    if os.path.exists(caminho) and os.path.isdir(caminho):
        tipo = 'w'
        caminho_completo = caminho + arquivo
        enc = 'utf-8'
        if os.path.exists(caminho_completo) and os.path.isfile(caminho_completo):
            tipo = 'a'
        with open (caminho_completo, tipo, encoding=enc) as file:
            file.write(linha_arq)

    else:
        print('Diretório inválido!')

def main():
    contador: int = 0
    local: str = ''
    entrada()

if (__name__=='__main__'):
    main()
#Fim