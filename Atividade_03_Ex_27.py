#Declaração de variáveis

numVoltas: int = 0
extCircuito: int = 0
tempo: int = 0
distancia: float = 0
velocidade: float = 0


#Início

numVoltas = int(input('Indique o número de voltas: '))
extCircuito = int(input('Indique a extensão do percurso, em metros: '))
tempo = int(input('Indique o tempo de duração, em minutos: '))

distancia = (extCircuito * numVoltas)
velocidade = ((distancia/1000)/(tempo/60))

print('A velocidade é de',velocidade,'km/h.')

#Fim