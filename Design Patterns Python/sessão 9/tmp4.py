from abc import ABCMeta, abstractmethod



class Viagem(metaclass=ABCMeta):

    @abstractmethod
    def ida(self):
        pass

    @abstractmethod
    def dia1(self):
        pass

    @abstractmethod
    def dia2(self):
        pass

    @abstractmethod
    def dia3(self):
        pass

    @abstractmethod
    def retorno(self):
        pass

    def itinerario(self):
        self.ida()
        self.dia1()
        self.dia2()
        self.dia3()
        self.retorno()

class ViagemVeneza(Viagem):

    def ida(self):
        print('Viagem de avião')

    def dia1(self):
        print('Visista a basílica de São Marcos')

    def dia2(self):
        print('Visita palácio Doge')

    def dia3(self):
        print('Aproveitar a comida local')

    def retorno(self):
        print('Retorno de avião')

class ViagemMalvinas(Viagem):
    def retorno(self):
        print('Retorno de Avião')

    def dia3(self):
        print('Relaxar na praia')

    def dia2(self):
        print('Esportes aquáticos')

    def dia1(self):
        print('Apreciar a vida marinha')

    def ida(self):
        print('Ida de ônibus')

class GeekTravel:

    def preparar_viagem(self):
        opcao = input('Qual local de viagem? [Veneza, Malvinas]')

        if opcao == 'Veneza':
            self.viagem = ViagemVeneza()
            self.viagem.itinerario()
        elif opcao == 'Malvinas':
            self.viagem = ViagemMalvinas()
            self.viagem.itinerario()
        else:
            print('Opção não disponível')

agenciaViagem = GeekTravel()
agenciaViagem.preparar_viagem()