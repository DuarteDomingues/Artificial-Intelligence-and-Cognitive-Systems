class No:

    def __init__(self, estado, operador=None, antecessor=None):

        '''
        estado: Estado
        operador: Operador
        antecessor: No
        '''
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        if self.__antecessor is None:
            self.__profunidade = 0
            self.__custo = 0
        else:
            self.__profunidade = self.__antecessor.obter_profundidade() + 1
            self.__custo = self.__antecessor.obter_custo() + self.__operador.custo(self.__antecessor.obter_estado(), estado)

    def obter_estado(self):
        return self.__estado

    def obter_operador(self):
        return self.__operador

    def obter_antecessor(self):
        return self.__antecessor

    def obter_profundidade(self):
        return self.__profunidade

    def obter_custo(self):
        return self.__custo

    def __eq__(self, obj):
        return self.__estado == obj.obter_estado()

    def __lt__(self, no):
        return self.__custo < no.obter_custo()