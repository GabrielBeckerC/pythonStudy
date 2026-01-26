from abc import ABCMeta, abstractmethod

#Command

class Ordem (metaclass=ABCMeta):

    @abstractmethod
    def executar(self):
        pass


#Comando Concreto

class OrdemCompra(Ordem):

    def __init__(self, acao):
        self.acao = acao

    def executar(self):
        self.acao.comprar()

class OrdemVenda(Ordem):

    def __init__(self, acao):
        self.acao = acao

    def executar(self):
        self.acao.vender()

class Acao:

    def comprar(self):
        print('Vc irá ciomprar ação...')

    def vender(self):
        print('Vc irá vender ações')

class Agente:

    def __init__(self):
        self.__fila_ordens =[]

    def add_ordem_na_fila(self, ordem):
        self.__fila_ordens.append(ordem)
        ordem.executar()

if __name__ =='__main__':
    #cliente
    acao = Acao()
    ordem_compra = OrdemCompra(acao)
    ordem_venda = OrdemVenda(acao)

    #Invoker
    agente = Agente()
    agente.add_ordem_na_fila(ordem_compra)
    agente.add_ordem_na_fila(ordem_venda)
