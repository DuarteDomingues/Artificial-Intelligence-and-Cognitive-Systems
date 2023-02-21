from random import choice


class ModeloTR:

    def __init__(self):
        self.__T = {}
        self.__R = {}

    def atualizar(self, s, a, r, sn):
        self.__T[(s, a)] = sn #Modelo determinista
        self.__R[(s, a)] = r

    def amostrar(self):
        s, a = choice(list(self.__T))
        sn = self.__T[(s, a)]
        r = self.__R[(s, a)]
        return s, a, r, sn
