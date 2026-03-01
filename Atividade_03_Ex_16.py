#Declaração de Valores

horasTrabalhadas: float = 0
valorHora: float = 0
percDesconto: float = 0
numDescendentes: int = 0
salarioHoras: float = 0
salarioLiquido: float = 0
salarioReceber: float = 0

#Início

horasTrabalhadas = float(input('Informe a quantidade de horas trabalhadas: '))
valorHora = float(input('Informe o valor recebido por horas, em reais: '))
percDesconto = float(input('Informe o valor percentual de desconto do salário: '))
numDescendentes = int(input('Informe o número de descendentes: '))

salarioHoras = horasTrabalhadas*valorHora
salarioLiquido = (salarioHoras - (salarioHoras*(percDesconto/100)))
salarioReceber = (salarioLiquido + (numDescendentes*100))

print('O salário a receber é de R$', salarioReceber)


#Fim