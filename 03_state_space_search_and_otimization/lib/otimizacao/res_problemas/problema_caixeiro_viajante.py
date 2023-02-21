from lib.otimizacao.problema.problema import Problema
import random as rd

class ProblemaCaixeiroViajante(Problema):

    def __init__(self, estado_inicial, tabela, cidades):

        self.__estado_inicial = estado_inicial
        self.__tabela = tabela
        self.__cidades = cidades
    
    def obter_custo_estado(self, estado):

        custo = sum(self.__tabela[id][self.__cidades[loc]] for id, loc in zip(estado, estado[1:]))
        return custo
    
    def obter_estado_aleatorio(self, estado):

        novo_estado = estado.copy()
        rd.shuffle(novo_estado)
        novo_estado.append(novo_estado[0])

        return novo_estado
    
    def obter_estados_vizinhos(self, estado):
        
        vizinhos = []
        estado_copia = estado.copy()
        estado_copia.pop()
        n = len(estado_copia)

        for i in range(n):
            for j in range(i+1,n):
                novo_estado = estado_copia.copy()
                novo_estado[i], novo_estado[j] = novo_estado[j], novo_estado[i]
                vizinhos.append(novo_estado)

        return vizinhos

    def obter_vizinho_aleatorio(self,vizinhos):

        estado = rd.choice(vizinhos)
        estado.append(estado[0])
        return estado
   
    @property
    def estado_inicial(self):
        return self.__estado_inicial