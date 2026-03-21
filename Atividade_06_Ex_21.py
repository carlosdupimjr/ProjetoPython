#Declaração de variáveis

nota1: float = 0
nota2: float = 0
nota3: float = 0
nota4: float = 0
media: float = 0

#Início

def resultado():
    global media
    media = (nota1 + nota2 + nota3 + nota4)/4
    if media >=6:
        print('APROVADO')
    elif media >=3 and media <6:
        print('EXAME')
    else:
        print('RETIDO')

def main():
    global nota1
    global nota2
    global nota3
    global nota4
    nota1 = float(input('Insira a nota do 1º bimestre: '))
    nota2 = float(input('Insira a nota do 2º bimestre: '))
    nota3 = float(input('Insira a nota do 3º bimestre: '))
    nota4 = float(input('Insira a nota do 4º bimestre: '))
    resultado()

if (__name__ == '__main__'):
    main()


#Fim