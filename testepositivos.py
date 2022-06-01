cont=0
media=0
positivos = []
for i in range(6):
    entrada = float(input())
    if entrada>0:
        positivos.insert(i, entrada)
        cont = cont+1
    
soma = sum(positivos)

media = soma/len(positivos)
print('{} valores positivos'.format(cont))
print('{:.1f}'.format(media))