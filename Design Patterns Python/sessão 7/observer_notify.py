from abc import ABCMeta, abstractmethod

# Assunto/ Tópico
class AgenteNoticias:

    def __init__(self):
        self.__inscritos = []
        self.__ultima_noticia = None

    def inscrever(self, inscrito):
        self.__inscritos.append(inscrito)

    def inscritos(self):
        return [type(valor).__name__ for valor in self.__inscritos]

    def desinscrever(self, inscrito=None):
        if not inscrito:
            return self.__inscritos.pop()
        else:
            return self.__inscritos.remove(inscrito)

    def notificar_todos(self):
        for insc in self.__inscritos:
            insc.notificar()

    def adicionar_noticia(self, noticia):
        self.__ultima_noticia = noticia

    def mostrar_noticia(self):
        return f'Urgente: {self.__ultima_noticia}'

#interface observer
class TipoInscricao(metaclass=ABCMeta):

    @abstractmethod
    def notificar(self):
        pass

#ObservadorA
class InscritosSMS(TipoInscricao):

    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}')


# ObservadorB
class InscritosEmail(TipoInscricao):

    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}')

# ObservadorN
class InscritosOutroMeio(TipoInscricao):

    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}')

#Cliente
if __name__ == '__main__':
    agencia_noticias = AgenteNoticias()

    InscritosSMS(agencia_noticias)
    InscritosEmail(agencia_noticias)
    InscritosOutroMeio(agencia_noticias)

    print(f'Inscritos: {agencia_noticias.inscritos()}')

    agencia_noticias.adicionar_noticia('Saiu novo vingadores')
    agencia_noticias.notificar_todos()

    print(f'Descadastrado: {type(agencia_noticias.desinscrever()).__name__}')
    print(f'Inscritos: {agencia_noticias.inscritos()}')

    agencia_noticias.adicionar_noticia('Saiu nova espansão de WOW')
    agencia_noticias.notificar_todos()