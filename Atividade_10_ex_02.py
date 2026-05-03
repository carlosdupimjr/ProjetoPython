#Função Maior valor
def funcMaiorValor(valor1, maiorAtual, count):
    if (count == 0):        
        return valor1
    else:
        if (maiorAtual >= valor1):
            return maiorAtual
        else:            
            return valor1

#Função Menor valor
def funcMenorValor(valor2, menorAtual, count):
    if (count == 0):
        return valor2
    else:
        if (menorAtual <= valor2):
            return menorAtual
        else:
            return valor2

#Principal
def main():
    vet_int: int = [0]*100
    maiorValor: int = 0
    menorValor: int = 0
    soma: int = 0
    media: float = 0

    for i in range (100):
        vet_int[i] = int(input(f'Digite o {i+1}º número: '))
        maiorValor = funcMaiorValor(vet_int[i], maiorValor, i)
        menorValor = funcMenorValor(vet_int[i], menorValor, i)
        soma = soma + vet_int[i]
    
    media = soma/100
    
    
    print('O maior valor é igual a ', maiorValor,'.')
    print('O menor valor é igual a ',menorValor,'.')
    print('A media dos valores é igual a ',media,'.')

if (__name__ == '__main__'):
    main()