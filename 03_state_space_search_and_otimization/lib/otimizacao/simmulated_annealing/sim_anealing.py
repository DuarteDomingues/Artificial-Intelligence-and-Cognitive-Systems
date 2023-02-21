import random as rd
import numpy as np
import sys


class SimulatedAnnealing():

   def __init__(self, problema, T):

      self.__problema = problema
      self.__T  = T
      self.__estado_curr = problema.estado_inicial
      self.__custo_curr = problema.obter_custo_estado(self.__estado_curr)
   
   def run(self, max_itr=sys.maxsize):

      self.__estado_curr = self.__problema.obter_estado_aleatorio(self.__estado_curr)
      self.__custo_curr = self.__problema.obter_custo_estado(self.__estado_curr)

      #temp minima em que as iteracoes acabam
      t_min = 1
      # variacao iterativa da temp
      variacao = 0.99
      ult_itr=0

      while(self.__T > t_min):
         for i in range(max_itr):

            self.__T *= variacao

            #obter vizinhos do estado currente
            vizinhos = self.__problema.obter_estados_vizinhos(self.__estado_curr)
            #obter novo estado, escolhendo estado randomly do conjunto de vizinhos
            novo_estado = self.__problema.obter_vizinho_aleatorio(vizinhos)
            custo_novo_estado = self.__problema.obter_custo_estado(novo_estado)

            delta_e = custo_novo_estado - self.__custo_curr
            
            if delta_e >0:
               prob = np.exp((self.__custo_curr-custo_novo_estado)/self.__T)
               if prob > rd.uniform(0,1):
                  self.__estado_curr = novo_estado
                  self.__custo_curr = custo_novo_estado

            else:
               self.__estado_curr = novo_estado
               self.__custo_curr = custo_novo_estado

            ult_itr = i

      return (self.__estado_curr, self.__custo_curr, ult_itr)
