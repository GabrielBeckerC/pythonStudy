#façade

class GerenciamentoEventos:

    def __init__(self):
        print('GerenciamentoEventos :: Vou organizar com todo mundo \n\n')

    def organizar(self):
        self.salao = SalaoFestas()
        self.salao.agendar()

        self.florista = Florista()
        self.florista.arranjar_flores()

        self.comida = Restaurante()
        self.comida.preparar()

        self.musica = Banda()
        self.musica.montar_palco()

#Subsistema 1

class SalaoFestas:

    def __init__(self):
        print('SalãoFestas :: Agendando o salão de festas...')

    def _esta_disponível(self):
        print('SalaoFestas :: Este salaão de festas es disponível? ')

    def agendar(self):
        if self._esta_disponível():
            print('SalaoFestas :: Agentadamento do salão realizado. \n')

#Subsistema 2

class Florista:
    def __init__(self):
        print('Florista ::  Flores para um Evento?')

    def arranjar_flores(self):
        print('Florista :: Rosas, Margaridase Lírios')

#Subsistema 3

class Restaurante:

    def __init__(self):
        print('Restaurante :: Comida para eventos...')

    def preparar(self):
        print('Restaurante :: Comida chinesa e brasileira serão servidas...\n')

#subsitema 4

class Banda:

    def __init__(self):
        print('Banda :: Arranjo musicais para eventos')

    def montar_palco(self):
        print('Banda ::  monta palco para eo evento ...\n')


#Cliente

class Cliente:

    def __init__(self):
        print('Cliente :: UAU! Preparação para o evento')

    def contrata_gerente_eventos(self):
        print('Cliente :: Vou contratar uma empresa pra gerenciar o evento\n')

        ge = GerenciamentoEventos()
        ge.organizar()

    def __del__(self):
        print('Cliente:: Foi muito simples organizar oo evento com o FAÇADE')



if __name__ == '__main__':
    cliente = Cliente()
    cliente.contrata_gerente_eventos()