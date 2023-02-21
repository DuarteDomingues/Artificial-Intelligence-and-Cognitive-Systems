from lib.plantraj.planeador import Planeador
from lib.pee.wavefront.wavefront.wavefront import Wavefront
from lib.pee.modprob.solucao import Solucao
import numpy as np
from lib.pee.mecanismos_procura.no import No

class PlanWavefront(Planeador):

    def __init__(self):

        self.__plano = []
    


    def planear(self, modelo_plan, estado_inicial, objetivo):

        wavefront = Wavefront(modelo_plan.obter_operadores())
        valores = wavefront.run(objetivo)
        self.__obter_solucao(estado_inicial,objetivo,valores,modelo_plan.obter_operadores() )
    


    def __obter_acao(self, estado, operadores,valores):

        acoes = []
        
        for operador in operadores:
            novo_estado = operador.aplicar(estado)
            if novo_estado != None and novo_estado in valores :
                valor = valores[novo_estado]
                acoes.append([operador,valor])
        
        a = np.asarray(acoes)
        print("a",a, "state",estado)
        index = a[:, 1].tolist().index(max(a[:, 1]))

        a = a.tolist()

        return a[index][0]
     

    def __obter_solucao(self, estado_inicial, objetivo,valores, operadores):

        #sol = Solucao()
        estado = estado_inicial

        caminho=[]
        while estado != objetivo:
            a = self.__obter_acao(estado, operadores, valores)
            novo_estado = a.aplicar(estado)
            caminho.append(No(estado,a))
            estado = novo_estado
        
        #sol.set_caminho(caminho)
        self.__plano = caminho

    
    def obter_operador(self):
        if len(self.__plano)!=0:
            return self.__plano.pop(0).obter_operador()
    
        return None


    def plano_pendente(self):
        return bool(self.__plano)
        
    def terminar_plano(self):
        self.__plano = None
    
    def obter_plano(self):
        return self.__plano

    