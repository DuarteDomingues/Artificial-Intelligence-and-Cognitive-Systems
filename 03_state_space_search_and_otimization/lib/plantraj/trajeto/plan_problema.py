from lib.pee.modprob.problema import Problema
import math

class ProblemaPlan(Problema):
    
        def __init__(self, estado_inicial, estado_final, operadores):

            '''
            param estado_inicial: Estado
            param estado_final: Estado
            param operadores: List<Operador>
            '''
            super().__init__(estado_inicial, operadores)
            self.__estado_final = estado_final
        
        def objetivo(self, estado):
            '''
            param estado: Estado
            return: boolean
            '''
            return estado == self.__estado_final

        def heuristica(self, estado):
            '''
            param estado: Estado
            return: double
            '''
            return math.sqrt(((self.__estado_final.obter_x()-estado.obter_x())**2)+((self.__estado_final.obter_y()-estado.obter_y())**2))
        
        
