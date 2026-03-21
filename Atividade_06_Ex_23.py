#Declaração de valores

valor1: float = 0
valor2: float = 0
valor3: float = 0
valor4: float = 0

#Início
def main():
    global valor1
    valor1 = float(input('Insira o primeiro valor:'))
    ordemCresc()
    
def ordemCresc():
    global valor2
    global valor3
    global valor4
    
    valor2 = float(input('Insira o segundo valor:'))
    if valor2 < valor1:
        print('Valor não pode ser menor que o anterior, favor inserir valor válido.')
    else:
        valor3 = float(input('Insira o terceiro valor:'))    
        if valor3 < valor2:
            print('Valor não pode ser menor que o anterior, favor inserir valor válido.')
        else:
            valor4 = float(input('Insira o quarto valor:'))    
            if valor4 <= valor1:
                    print('Ordem crescente dos valores:',valor4,',',valor1,',',valor2,',',valor3,'.')
            elif valor4 > valor1 and valor4 <= valor2:
                    print('Ordem crescente dos valores:',valor1,',',valor4,',',valor2,',',valor3,'.')
            elif valor4 > valor2 and valor4 <= valor3:
                    print('Ordem crescente dos valores:',valor1,',',valor2,',',valor4,',',valor3,'.')
            else:
                    print('Ordem crescente dos valores:',valor1,',',valor2,',',valor3,',',valor4,'.')

if(__name__ == '__main__'):
      main()

#Fim