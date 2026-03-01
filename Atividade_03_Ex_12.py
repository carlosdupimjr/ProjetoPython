#Declaração de Variáveis

anoNascimento: int=0
anoAtual: int = 0
idadeAtual: int = 0
idadeFuturo: int = 0
futuro: int = 17

#Início

anoNascimento = int(input('Informe o seu ano de nascimento: '))
anoAtual = int(input('Informe o ano atual: '))

idadeAtual = anoAtual-anoNascimento
idadeFuturo = idadeAtual + futuro

print('A sua idade atual é ', idadeAtual, 'anos, e sua idade em 17 anos será de ', idadeFuturo, 'anos.')


#Fim