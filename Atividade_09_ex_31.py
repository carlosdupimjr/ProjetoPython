import os
#Início

# Procedimento para gravar os valores
def gravar_valores(caminho):
    contador = 11

    pasta = os.path.dirname(caminho)
    os.makedirs(pasta, exist_ok=True)

    with open(caminho, "w") as arquivo:
        while contador > 10 and contador < 150:
            valorQuadrado = contador ** 2
            
            print(valorQuadrado)                  
            arquivo.write(f"{valorQuadrado}\n")   
            
            contador += 1

# Função principal
def main():
    dir = 'C:\\temp\\'
    arq = 'ex31.txt'
    caminho = dir + arq

    gravar_valores(caminho)
    
    print("Documento criado em ", caminho)

if __name__ == "__main__":
    main()