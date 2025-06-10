quadrado = lambda num: num**2

lista = list((1, 2, 3, 4))
resutados = []

for numero in lista:
    resutados.append(quadrado(numero))

print(lista)
print(resutados)