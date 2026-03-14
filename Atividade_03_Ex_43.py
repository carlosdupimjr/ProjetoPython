#Declaração de variáveis

alturaAna: int = 110
alturaMaria: int = 150
ritmoAna: int = 3
ritmoMaria: int = 2
ano: int = 0

#Início

while (alturaAna <= alturaMaria):
    ano +=1
    alturaAna = alturaAna + ritmoAna
    alturaMaria = alturaMaria + ritmoMaria

print('Serão necessários',ano,'anos para que Ana  tenha',alturaAna,'cm de altura e seja maior que Maria, que terá',alturaMaria,'cm.')



#Fim