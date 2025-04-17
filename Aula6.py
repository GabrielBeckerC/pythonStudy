# Trabalhando com Arrays
'''Arrays são matrizes, ou seja, são listas com melhor performance'''

from array import array

# array deve ser importado da biblioteca array
'''u = unsigned char
i = integer
f = float
d = double
b = byte
B = unsigned byte
h = short
H = unsigned short
l = long
L = unsigned long
q = long long
Q = unsigned long long
'''

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)

letras1 = array('u', ['a', 'b', 'c', 'd'])
numeros_i1 = array('i', [10, 20, 30, 40])
numeros_f1 = array('f', [1.2, 2.2, 3.2])

print(letras1)
print(numeros_i1)
print(numeros_f1)

# Criando SETS
'''SETS são listas que não aceitam valores duplicados'''

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)
'''Existem 4 tipos de operações com SETS: união, simétrico, intersecção e diferença.
União: |
Intersecção: &
Diferença: -
Simetrico: ^
'''

print(num1 | num2)
print(num1 ^ num2)
print(num1 & num2)
print(num1 - num2)

# Funções com SETS

list3 = [10, 20, 30, 40, 50]

s1 = set(list3)

s1.add(60)
s1.update([70, 80, 90])
s1.discard(30)

print(s1)

# Sets com Strings

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2).union(set3)

print(set4)

# Introdoção a Dicionários
'''Dicionários são listas de dados que utilizam chave e valor'''

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 10.0, 'aprovação': True}

print(aluno['nome'])

aluno['nome'] = 'Jose'

print(aluno['nome'])

aluno.update({'nome': 'Erick', 'nota_final': 8.0})

print(aluno)

print(aluno.get('endereco', 'Não existe'))

del aluno['idade']

print(aluno)

# Iterando com Dicionários

for keys, values in aluno.items():
    print(f'{keys}: {values}')

# Visualizando Itens, Chaves e Valores

aluno.update({'Matérias': ['Matemática', 'Português', 'Inglês']})

print(aluno)

print(aluno.get('Matérias'))

print(len(aluno))

# Conhecendo a função LAMBDA
'''Função lambda é uma função como qualquer outra, mas é uma função anônima, ou seja, não possui nome'''


def multiplicar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4


print(multiplicar(2))

# Função MAP
'''Map é uma função que aplica uma função a um iterável'''

lista4 = [1, 2, 3, 4]


def multiplicar2(x):
    return x * 2


print(list(map(multiplicar2, lista4)))

# Função MAP com LAMBDA

print(list(map(lambda x: x * 2, lista4)))

# Função FILTER

'''Filter é uma função que filtra os elementos de um iterável'''

valors = [10, 12, 34, 44, 57]


def remover20(x):
    return x > 20


print(list(filter(remover20, valors)))

# Entendendo List Comprehension com Strings

'''List Comprehension é uma forma de criar listas de forma mais rápida e simples'''

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
# frutas2 = []


# for itens  in frutas1:
#   if 'b' in itens:
#     frutas2.append(itens)

frutas2 = [item for item in frutas1 if 'b' in item]

print(frutas2)

# List Comprehension com Números

# nums = []

# for x in range(6):
#   nums.append(x * 10)

nums = [x * 10 for x in range(6)]
print(nums)

# Generators expressions

'''Generators expressions são uma forma de criar generators de forma mais rápida e simples'''

numbers = [x * 10 for x in range(6)]

print(numbers)
