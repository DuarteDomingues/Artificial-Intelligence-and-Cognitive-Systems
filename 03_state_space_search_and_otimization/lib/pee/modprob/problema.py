class Problema:

    def __init__(self, estado_inicial, operadores):

        '''
        param estado_inicial: Estado
        param estado_final: Estado
        param operadores: List<Operador>
        '''
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores

    def obter_estado_inicial(self):
        return self.__estado_inicial

    def obter_operadores(self):
        return self.__operadores

    def objetivo(self, s):
        raise NotImplementedError()

    def heuristica(self, s):
        raise NotImplementedError()
