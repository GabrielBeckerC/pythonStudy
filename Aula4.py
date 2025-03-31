# FUNÇÕES

# Function
'''Funções são blocos de código que podem ser chamados em qualquer parte do programa'''

# Modeles
'''Módulos são arquivos que podem ser importados para o código principal'''

# Pacotes
'''Pacotes são conjuntos de módulos'''

# Bibliotecas
'''Bibliotecas são conjuntos de pacotes'''

# Como funciona uma função
'''DRY - Don't repeat yourself - basicamaente não se repita, que é o objetivo da função'''

# Parametros e Argumentos
'''Parametros são os dados que a função espera receber para executar a sua função. No exemplo abaixo são nome e quantidade'''
'''Argumentos são os dados que são passados para a função quando ela é chamada. No exmplo abaixo são 'Marcos' e '5'''


def boas_vindas(nome, quantidade):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')


boas_vindas('Gabriel', 5)

boas_vindas('Marcos', 4)

# Criando uma função de soma
'''usamos o return para retornaro valor da função'''


def soma(num1, num2):
    return num1 + num2


print(soma(10, 20))

# Defaut e Non-defaut
'''Defaut é quando você define o valor no parametro, e non-defaut é quando você não define o valor no parametro'''
'''O non-defaut precisa ser o ultimo parametro'''

# Funções são dividas em dos tipos:as que realizam uma tarefa e as que retornam um valor

'''Realizam uma tarefa'''


def cliente1(nome):
    print(f'Olá {nome}')


'''Retornam um valor'''


def cliente2(nome):
    return f'Olá {nome}'


cliente1('Maria')
print(cliente2('José'))


# Vários argumentos xargs com números

def soma_varios_numeros(*numeros):
    total = 0
    for num in numeros:
        total += num

    return total


x = soma_varios_numeros(2, 3, 4, 5)
print(x)


# Vários argumentos xargs nomeando parametros

def agencia(**carro):
    return carro


print(agencia(modelo='Gol', cor='Branca', motor=1.0))
print(agencia(modelo='Gol', cor='Branca', motor=1.0, placa='12k-123e'))
print(agencia(modelo='Gol', cor='Branca'))

# Importando um módulo

# Qual é o número fatorial de 4?
# 4*3*2*1 = 24
import math  # importa o módulo math normalmente ele deve ser no topo do código mas para leitura coloquei aqui  hehe

print(math.factorial(4))
print(math.floor(2.7))