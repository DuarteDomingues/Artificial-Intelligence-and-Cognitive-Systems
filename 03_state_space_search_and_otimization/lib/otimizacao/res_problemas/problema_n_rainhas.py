from lib.otimizacao.problema.problema import Problema
import numpy as np
import random as rd

class ProblemaNRainhas(Problema):

    def __init__(self, estado_inicial ):
        
        self.__estado_inicial = estado_inicial
    
    def obter_custo_estado(self, estado):
        return self.__obter_custo_estado_ver_hor(estado) + self.__obter_custo_estado_diagonal(estado)
    
    def obter_estados_vizinhos(self, estado):

        vizinhos = []
        for i in range(len(estado)):
            for x in range(len(estado)):
                for y in range(len(estado)):
                    if (x != estado[i][0] or y != estado[i][1]) and (x,y) not in estado:
                        novo_estado = estado.copy()
                        novo_estado[i] = (x,y)
                        vizinhos.append(novo_estado)
        return vizinhos
    
    def obter_estado_aleatorio(self, estado):
        novo_estado = estado.copy()
        
        estados_repetidos=[]
        for i in range(len(novo_estado)):
            escolhido=False
            while(escolhido==False):
                x=np.random.randint(0, len(estado))
                y=np.random.randint(0, len(estado))
                if (x,y) not in estados_repetidos  :
                    novo_estado[i] = ( x, y)
                    escolhido=True
                    estados_repetidos.append(novo_estado[i])

        return novo_estado

          
    def __obter_custo_estado_ver_hor(self, estado):

        custo_ver_hor=0
        estados_vistos=[]
        for i in range(len(estado)-1):
            if estado[i] not in estados_vistos:
                for j in range(i+1,len(estado)):
                    
                    if estado[i][0] == estado[j][0] or estado[i][1] == estado[j][1] :
                        custo_ver_hor = custo_ver_hor+1
                estados_vistos.append(estado[i])
        
        return custo_ver_hor
    

    def __obter_custo_estado_diagonal(self, estado):

        custo=0
        estados_vistos=[]
        for i in range(len(estado)-1):
            if estado[i] not in estados_vistos:
                for j in range(i+1, len(estado)):
                    for n in range(1,len(estado)):
                        if (estado[i][0] == estado[j][0]+n and estado[i][1]== estado[j][1]+n):
                            custo = custo +1
                    
                        if(estado[i][0] == estado[j][0]-n and estado[i][1]== estado[j][1]-n):
                            custo = custo +1
                    
                        if(estado[i][0] == estado[j][0]-n and estado[i][1]== estado[j][1]+n):
                            custo = custo +1
                    
                        if(estado[i][0] == estado[j][0]+n and estado[i][1]== estado[j][1]-n):
                            custo = custo +1


                    estados_vistos.append(estado[i])
        return custo
    

    def obter_vizinho_aleatorio(self,vizinhos):
        return rd.choice(vizinhos)

    @property
    def estado_inicial(self):
        return self.__estado_inicial