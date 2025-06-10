
parOuImpar = lambda num: 'Par' if num % 2 == 0 else 'Impar'

numero = int(input('Digite um número: '))

print(f'{numero} é {parOuImpar(numero)}')