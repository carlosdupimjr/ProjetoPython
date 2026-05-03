def main():
    vet_int: float = [0.0]*30
    soma: float = 0.0
    media: float = 0.0
    acimaMedia: int = 0
    posicaoAbaixo: int = []*30
    count: int = 0

    for i in range (30):
        vet_int[i] = float(input(f'Insira a {i+1}ª nota: '))
        soma += vet_int[i]

    media = soma/30
    
    for i in range (30):
        if (vet_int[i] >= media):
            acimaMedia +=1
        else:
            posicaoAbaixo.append(i)

    

    print('Média geral de notas é igual a ',media,'.')
    print('A quantidade de notas acima da média é igual a ',acimaMedia,'.')
    print('As posições das notas abaixo da média, lembrando que posição 0 corresponde à 1ª nota: ',posicaoAbaixo)

if(__name__=='__main__'):
    main()