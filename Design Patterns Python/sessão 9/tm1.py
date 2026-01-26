from abc import abstractmethod, ABCMeta

class Compilador(metaclass=ABCMeta):

    @abstractmethod
    def coletar_fonte(self):
        pass

    @abstractmethod
    def compilar_objeto(self):
        pass

    @abstractmethod
    def executar(self):
        pass

    def compilar_e_executar(self):
        self.coletar_fonte()
        self.compilar_objeto()
        self.executar()


class CompiladorIOS(Compilador):

    def coletar_fonte(self):
        print('coletando código fonte swift')

    def compilar_objeto(self):
        print(' compilando cód seift para bytecode LLVM')

    def executar(self):
        print('programa executando no ambiente de execução')


class CompiladorAndroid(Compilador):

    def coletar_fonte(self):
        print('coletando código fonte Kotlin')

    def compilar_objeto(self):
        print(' compilando cód Kotlin para bytecode JVM')

    def executar(self):
        print('programa executando no ambiente de execução')

ios = CompiladorIOS()
ios.compilar_e_executar()

android = CompiladorAndroid()
android.compilar_e_executar()