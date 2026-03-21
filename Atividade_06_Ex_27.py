#Declaração de variáveis

numVoltas: int = 0
extCircuito: int = 0
tempo: int = 0

#Início

def calcVelocidade(voltas,circuito,duracao):
    distancia: float = 0
    velocidade: float = 0
    distancia = (circuito * voltas)
    velocidade = ((distancia/1000)/(duracao/60))
    print('A velocidade é de',velocidade,'km/h.')

def main():
    global numVoltas
    global extCircuito
    global tempo
    numVoltas = int(input('Indique o número de voltas: '))
    extCircuito = int(input('Indique a extensão do percurso, em metros: '))
    tempo = int(input('Indique o tempo de duração, em minutos: '))
    calcVelocidade(numVoltas,extCircuito,tempo)

if(__name__=='__main__'):
    main()

#Fim