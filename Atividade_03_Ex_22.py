#Declaração de variáveis

valor1: int = 0
valor2: int = 0

#Início

valor1 = int(input('Insira o primeiro valor: '))
valor2 = int(input('Insira o segundo valor: '))

if valor1 < valor2:
    print('Ordem crescente dos valores:', valor1, ',',valor2,'.' )
elif valor1 > valor2:
    print('Ordem crescente dos valores:', valor2, ',',valor1,'.' )
else:
    print('Os valores são iguais, não há ordem crescente entre eles.')

#Fim