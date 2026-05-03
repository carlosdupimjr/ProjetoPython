#Media
def funcMedia(valor, soma, count):
    count += 1
    soma = soma + valor
    return soma, count

#Soma Impar
def funcSomaImpar(valorImpar, somaImpar):
    somaImpar = somaImpar + valorImpar
    return somaImpar

#Principal
def main():
    vet_int: int =[0]*50
    soma: int = 0
    count: int = 0
    media: int = 0
    somaImpar: int = 0

    for i in range (50):
        vet_int[i] = int(input(f'Digite o {i+1}º valor: '))
        
        if (vet_int[i] >= 10 and vet_int[i] <=200):
            soma, count = funcMedia(vet_int[i], soma, count)
        
        if (vet_int[i] % 2 != 0):
            somaImpar = funcSomaImpar(vet_int[i], somaImpar)
    
    if count > 0:
        media = soma/count
    else:
        media = 0

    print ('Media dos números entre 10 e 20 é igual a ', media,'.')
    print ('Soma dos números ímpares é igual a ', somaImpar,'.')


if (__name__ == '__main__'):
    main()
#Fim