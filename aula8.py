# OOP - Object Oriented Programming

# Conhecendo Classes

'''
Classes são modelos para criar objetos. Um objeto é uma instância de uma classe. São utilizadas para agrupar dados e funções, podendo reutilizar.
'''

'''
Class: Fruta
Objetos: Abacate, Banana...
'''

# Criando uma classe

'''class Funcionarios:
  nome = 'Clark'
  sobrenome = 'Kent'

usuario1 = Funcionarios()

print(usuario1.nome)'''

# Criando um Objeto dentro de uma Classe

# criar a classe
'''class Funcionarios:
  pass #pass é uma palavra reservada que não faz nada, mas é usada para evitar erros de sintaxe quando uma classe ou função está vazia.

#criar o objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()


#Criar os parâmetros do usuário1
usuario1.nome = 'Clark'
usuario1.sobrenome = 'Kent'
usuario1.data_nascimento = '19/06/1938'

#Criar os parâmetros do usuário2
usuario2.nome = 'Bruce'
usuario2.sobrenome = 'Wayne'
usuario2.data_nascimento = '30/04/1962'

#print
print(usuario1.nome)
print(usuario2.nome)'''

# Criando Construtores
from datetime import datetime


class Funcionarios:

    # Metodo construtor
    # def __init__(self): #self é uma referência ao próprio objeto, permitindo acessar atributos e métodos da classe.
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    # Criando mais  funções na classe
    def nome_completo(self):
        return print(f'{self.nome} {self.sobrenome}')

    # Calcular idade
    def idade_funcionario(self, ):
        ano_atual = datetime.now().year
        return print(ano_atual - self.ano_nascimento)


# criar o objeto
usuario1 = Funcionarios('Clark', 'Kent', 1938)
usuario2 = Funcionarios('Bruce', 'Wayne', 1962)

# print
print(usuario1.nome)
print(usuario2.nome)
usuario1.nome_completo()
usuario2.nome_completo()
Funcionarios.nome_completo(usuario1)
Funcionarios.idade_funcionario(usuario1)
Funcionarios.idade_funcionario(usuario2)