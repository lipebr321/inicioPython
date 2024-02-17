entrada = int(input('Digite um número para ver a tabuada de 0 a 100 dele --> '))

print('-' * 15)
for i in range(1, 101):  # O loop vai de 1 a 100
    print('{} X {:3} = {}'.format(entrada, i, entrada * i))
print('-' * 15)
