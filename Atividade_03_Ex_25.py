#Declaração de variáveis

horaInicio: int = 0
minutoInicio: int = 0
horaFinal: int = 0
minutoFinal: int = 0
horaTotal: int = 0
minutoTotal: int = 0

#Início

horaInicio = int(input('Indique a hora no início do jogo: '))
minutoInicio = int(input('Indique os minutos no início do jogo: '))

horaFinal = int(input('Indique a hora ao final do jogo: '))
minutoFinal = int(input('Indique os minutos ao final do jogo: '))

if (horaFinal == horaInicio and minutoFinal == minutoInicio):
    minutoTotal = 0
    horaTotal = 0
elif (horaFinal == horaInicio and minutoFinal > minutoInicio):
    minutoTotal = minutoFinal - minutoInicio
    horaTotal = 0
elif (horaFinal > horaInicio and minutoFinal == minutoInicio):
    minutoTotal = 0
    horaTotal = horaFinal - horaInicio
elif (horaFinal > horaInicio and minutoFinal > minutoInicio):
    minutoTotal = minutoFinal - minutoInicio
    horaTotal = horaFinal - horaInicio
elif (horaFinal > horaInicio and minutoFinal < minutoInicio):
    minutoTotal = (minutoFinal + 60) - minutoInicio
    horaTotal = (horaFinal - horaInicio - 1)
elif (horaFinal < horaInicio and minutoFinal == minutoInicio):
    minutoTotal = 0
    horaTotal = (horaFinal + 24) - horaInicio
elif (horaFinal < horaInicio and minutoFinal > minutoInicio):
    minutoTotal = minutoFinal - minutoInicio
    horaTotal = (horaFinal + 24) - horaInicio
elif (horaFinal < horaInicio and minutoFinal < minutoInicio):
    minutoTotal = (minutoFinal + 60) - minutoInicio
    horaTotal = (horaFinal + 24) - horaInicio - 1

print('O tempo total de jogo é de:',horaTotal,'horas e',minutoTotal,'minutos.')

#Fim