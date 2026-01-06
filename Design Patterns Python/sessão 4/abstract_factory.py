from abc import ABCMeta, abstractmethod


 #Abstract_Factory

class  PizzaFactory(metaclass=ABCMeta):

     @abstractmethod
     def criar_pizza_veg(self):
         pass

     @abstractmethod
     def criar_pizza(self):
         pass

#Concret Factory A
class PizzaBrazileira(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaMandioca()

    def criar_pizza(self):
        return PizzaCamarao()

#Concret Factory B
class PizzaItaliana(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaBrocoli()

    def criar_pizza(self):
        return PizzaBolonha()

#AbstractProdutoA
class PizzaVeg(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self):
        pass

#AbstractProdutoB
class Pizza(metaclass=ABCMeta):

    @abstractmethod
    def servir(self, pizza_veg_instance):
        pass


#ProdutoConcreto

class PizzaMandioca(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')

#ProdutoConcreto

class PizzaCamarao(Pizza):

    def servir(self, pizza_veg_instance):
        print(f'{type(self).__name__} é servida com camarão na {type(pizza_veg_instance).__name__}')

#ProdutoConcreto

class PizzaBrocoli(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')

#ProdutoConcreto

class PizzaBolonha(Pizza):

    def servir(self, pizza_veg_instance):
        print(f'{type(self).__name__} é servida com carne na {type(pizza_veg_instance).__name__}')


#CLiente

class Pizzaria:

        def fazer_pizzas(self):
            for factory in [PizzaBrazileira(), PizzaItaliana()]:
                self.factory = factory
                self.pizza = self.factory.criar_pizza()
                self.pizza_veg = self.factory.criar_pizza_veg()
                self.pizza_veg.preparar()
                self.pizza.servir(self.pizza_veg)

pizzaria = Pizzaria()
pizzaria.fazer_pizzas()