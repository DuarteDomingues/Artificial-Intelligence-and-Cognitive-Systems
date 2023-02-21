from lib.mundo.modelo_mundo import ModeloMundo
from lib.plantraj.trajeto.operador_mover import OperadorMover

class ControloDelib:

    def __init__(self, planeador):
        '''
        param planeador: Planeador
        '''
        self.planeador = planeador
        self.__modelo_mundo = ModeloMundo()
        self.__objetivo = None
    

    def __reconsiderar(self):

        ''' 
        return: Boolean 
        '''
        #check if mundo alterado
        if self.__objetivo is None or not self.planeador.plano_pendente() :
            return True
        return False
    

    def __deliberar(self):
        
        self.__objetivo = self.__modelo_mundo.obter_alvo()  
    
    def __planear(self):

        '''
        para o agente a calcular o melhor percurso de acao
        '''

        if self.__objetivo is not None:
            self.planeador.planear(self.__modelo_mundo, self.__modelo_mundo.obter_estado(), self.__objetivo)
        
        else:
            self.planeador.terminar_plano()
    
    def __executar(self):

        operador = self.planeador.obter_operador()
        if operador is not None:
            return operador


    def processar(self, percecao):

        '''
        Processa o estado do ambiente e devolve a melhor accao a ser tomada
        
        param percepcao: Percepcao
                estado atual do ambiente 
        return: Operador
        '''
        self.__assimilar(percecao)
        if (self.__reconsiderar()):
            self.__deliberar()
            self.__planear()
        operador = self.__executar()
        return operador


    def __assimilar(self, percecao):

     
        self.__modelo_mundo.atualizar(percecao)

    def obter_plano(self):
        return self.planeador.obter_plano()
    

   # def processar(self, percepcao):




    

