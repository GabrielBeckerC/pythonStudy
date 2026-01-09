from abc import ABCMeta, abstractmethod

# interface

class Carteira(metaclass=ABCMeta):

    @abstractmethod
    def pagar(self):
        pass

#Objeto real

class Banco(Carteira):

    def __init__(self):
        self.cartao = None
        self.conta = None

    def __get_conta(self):
        self.conta = self.cartao
        return self.conta

    def __tem_saldo(self):
        print(f'Banco :: Checando se a conta {self.__get_conta()} tem saldo')
        return True

    def set_cartao(self, cartao):
        self.cartao = cartao

    def pagar(self):
        if self.__tem_saldo():
            print('Banco :: pagando o bar')
            return True
        else:
            print('Banco :: Sem saldo')
            return False

#Proxy

class CartaoDebito(Carteira):

    def __init__(self):
        self.banco = Banco()

    def pagar(self):
        cartao = input('Proxy :: Informe o nº do cartão')
        self.banco.set_cartao(cartao)
        return self.banco.pagar()

#cliente

class Cliente:

    def __init__(self):
        print('Quero comprar um  suco')
        self.cartao_debito = CartaoDebito()
        self.comprei = None

    def fazer_pagamento(self):
        self.comprei = self.cartao_debito.pagar()

    def __del__(self):
        if self.comprei:
            print('suquinho bom')
        else:
            print('Sem dinheiro :(')


if __name__ == '__main__':
    cliente = Cliente()
    cliente.fazer_pagamento()