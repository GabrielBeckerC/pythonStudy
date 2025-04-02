#Estrutura de dados

#Introdução  a LISTAS

'''Listas são estruturas de dados do tipo sequencial, ou seja, uma sequêcia de elementos que podem ser acessados por um índice.'''

cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Porto Alegre'
cidades = ['Rio de Janeiro', 'São Paulo', 'Porto Alegre']
#index           0               1            2

print(cidades)

#Manipulando listas

print(cidades[2])

#Funções dentro de listas

cidades.append('Santa Maria')
print(cidades)
cidades.remove('São Paulo')
print(cidades)

#Concatenando listas

numeros = [2 ,3 ,4 ,5]
letras = ['a', 'b', 'c', 'd']
final = numeros + letras
print(final)
numeros*=2
print(numeros)

itens = [['item1', 'item2'], ['item3', 'item4']]

print(itens)
print(itens[1][1])

#Extraindo variáveis de listas

produtos = ['arroz', 'feijão', 'laranja', 'banana']

item1 = produtos[0]

print(item1)
'''como fazer com menos linhas de código'''

item1, item2, item3, *outros = produtos
print(item2)
print(outros)

#Looping dentro de uma lista

valores = [50, 80, 110, 150, 170]

for x in valores:
    print(f'O valor final do produto é de R${x}.')

#Verificando itens em uma lista

cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:
    print('Em estoque')
else:
    print('Não temos esta cor em estoque')

#Agregando duas listas com o ZIP

cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]

duas_listas = zip(cores, valores)
print(list(duas_listas))

#Input em uma lista

frutas_usuario = input('Digite o nome das frutas separados por virgula:')

frutas_lista = frutas_usuario.split(', ')
print(frutas_lista)

#Entendendo sobre Tuples

'''Tuples são listas imutáveis, ou seja, não podem ser alteradas'''

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

print(type(cores_list))
print(type(cores_tuple))
