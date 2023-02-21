import random as rd
import numpy as np
import sys


class HillClimbingEstocastico():

    def __init__(self, problema):

        self.__problema = problema
        self.__estado_curr = problema.estado_inicial
        self.__custo_curr = problema.obter_custo_estado(self.__estado_curr)

   
    def run(self, max_itr=sys.maxsize):
        
        self.__estado_curr = self.__problema.obter_estado_aleatorio(self.__estado_curr)
        self.__custo_curr = self.__problema.obter_custo_estado(self.__estado_curr)
        

        ult_itr = 0

        for i in range(max_itr):

            #obter vizinhos do estado currente
            vizinhos = self.__problema.obter_estados_vizinhos(self.__estado_curr)

            #obter melhor estado e custo do conjunto de vizinhos
            melhor_estado_vizinho, melhor_custo = self.__decidir_escolhe_estado_vizinho(vizinhos)

            ult_itr = i

            if melhor_custo  < self.__custo_curr:
                
                self.__estado_curr = melhor_estado_vizinho
                self.__custo_curr = melhor_custo
            
            else:

                return self.__estado_curr, self.__custo_curr, ult_itr
        
        return self.__estado_curr, self.__custo_curr, ult_itr
    

    def __decidir_escolhe_estado_vizinho(self, vizinhos, max_itr=10000):

        for i in range (max_itr):

            #estado_aleatorio = rd.choice(vizinhos)
            estado_aleatorio = self.__problema.obter_vizinho_aleatorio(vizinhos)
            custo_estado_aleatorio = self.__problema.obter_custo_estado(estado_aleatorio)
            if custo_estado_aleatorio < self.__custo_curr:
                return estado_aleatorio, custo_estado_aleatorio
        
        return self.__estado_curr, self.__custo_curr