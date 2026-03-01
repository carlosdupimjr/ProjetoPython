#Declaração de Variáveis

distancia: float = 0
quantidadeLitros: float = 0
distanciaLitro: int = 12
tempo: float = 0
velocidadeMedia: float = 0

#Início

distancia = float(input('Informe a distância total do percurso, em quilômetros: '))
quantidadeLitros = distancia/distanciaLitro

tempo = float(input('Informe o tempo de viagem, em horas: '))
velocidadeMedia = distancia/tempo

print('A quantidade de litros de gasolina gastos na viagem será de', quantidadeLitros, 'litros.')
print('A velociade média de viagem é de', velocidadeMedia, 'km/h,')

#Fim