#Declaração de Variáveis

alimentoKG: float = 0
dias: int = 0

#Início

alimentoKG = float(input('Informe o peso do alimento em quilogramas: '))

dias = alimentoKG/0.05

print('Com uma taxa de consumo de 50g ao dia, o alimento durará', dias, 'dias.')

#Fim