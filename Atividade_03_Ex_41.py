#Declaração de variáveis

valor1: int = 0
valor2: int = 0
soma: int = 0

#Início

for valor1 in range(1,7,1):
    for valor2 in range (1,7,1):
        soma = (valor1 + valor2)
        if soma == 7:
            print (valor1,'+', valor2,'=',soma)


#Fim