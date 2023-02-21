import math
import sys

class Wavefront:

    def __init__(self, operadores):

        self.__valores = []
        self.__operadores = operadores

    
    def __obter_adjacentes(self, s):

        estados = []
        for operador in self.__operadores:
            novo_s = operador.aplicar(s)
            if novo_s != None:
                estados.append(novo_s)
        
        return estados

    
    def __obter_distancia(self,s,sn):

        #obter_x
        #obter_y
        x = (s.obter_x()-sn.obter_x())**2
        y = (s.obter_y()-sn.obter_y())**2
        return math.sqrt(x+y)



    def run(self, objetivo, valor_max=100,gama=0.5):

        '''
        planeia caminho até objetivo
        começa a pesquisar pelos nós mais antigos até chegar ao agente
        são explorados todos os nós mais antigos sempre
        por cada nó expandido é dado um valor ao memsmo, valores incrementados até chegar ao agente
        após pesquisa chegar ao agente, necessita de seguir gradiente dos valores criados pelo Wavefront até chegar ao nó objetivo
        '''

        valores = {}
        frente_onda = []
        valores[objetivo] = valor_max
        frente_onda.append(objetivo)

        while frente_onda:
            s = frente_onda.pop(0)
            for sn in self.__obter_adjacentes(s):
                v = valores[s] * math.pow(gama,self.__obter_distancia(s,sn))
                if sn in valores:
                    if v > (valores[sn]):
                        valores[sn] = v
                        frente_onda.append(sn)
                elif v > sys.float_info.min:
                    valores[sn] = v
                    frente_onda.append(sn)
        
        self.__valores = valores
        return self.__valores

