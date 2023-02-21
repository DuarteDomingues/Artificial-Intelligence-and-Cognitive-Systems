from lib.plantraj.planeador import Planeador
from lib.plantraj.trajeto.plan_problema import ProblemaPlan

class PlanPee(Planeador):

    def __init__(self, mec_proc):
        '''
        param mec_proc: Procura
        '''
        self.__mec_proc = mec_proc
        self.__plano = []
    

    def planear(self, modelo_plan, estado_inicial, objetivo):

        operadores = modelo_plan.obter_operadores()
        problema_plan = ProblemaPlan(estado_inicial, objetivo,operadores )
        solucao = self.__mec_proc.resolver(problema_plan)
        self.__plano = self.__obter_solucao(solucao)
        solucao.set_caminho(self.__plano)

    
        return solucao
    

    def obter_operador(self):
        if self.__plano:
            
            op= self.__plano.pop(0).obter_operador()
         
            return op
        return None

    def plano_pendente(self):
        return bool(self.__plano)
        
    def terminar_plano(self):
        self.__plano = None
    

    def __obter_solucao(self, solucao):
        
        caminho=[]
        if solucao != None:
            for no in solucao.obter_caminho()[1:]:
               
                if no.obter_operador() is not None:
                    caminho.append(no)
        
        return caminho


    def obter_plano(self):
        return self.__plano