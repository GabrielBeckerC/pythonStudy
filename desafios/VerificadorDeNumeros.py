
try:
    numero = int(input('Digite um número: '))
    if numero > 10:
        print('O número é maior que 10')
    else:
        print('O número é menor ou igual a 10')
except ValueError:
    print('Use somente números')


