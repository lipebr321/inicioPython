#Criando uma lista []

times = ['Sao Paulo', 'Paleiras', 'Santos', 'Bragantino']

#print (times[0])
times.append('curintia')
#Adciona a lista um novo item

#reproduz a lista
for time in times :
 print(time)

times.remove(input('Digite um time para remover'))


for time in times :
 print(time)
 