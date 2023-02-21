from amb.ambiente.percepcao import Percecao
from amb.ambiente.mover import Mover
from lib.plantraj.trajeto.operador_mover import OperadorMover
from lib.plantraj.trajeto.estado_trajeto import EstadoTrajeto

class AgenteProspector():

    def __init__(self, controlo,amb):
        '''
        param Controlo: controlo , algoritmo de busca do agente
        '''
        self.__controlo = controlo
        self.__amb = amb

        
    def executar(self):

      
        percepcao = self.__percepcionar()
        operador = self.__processar(percepcao)
       

        self.__actuar(operador)  #atuar acao no mundo

    def __percepcionar(self):
        '''
        Avalia o ambiente em que se encontra o agente, procura alvos e identifica obstaculos
        return: Percepcao , um modelo do ambiente 
        '''
        percecao = Percecao(self.__amb)
        return percecao

    def __processar(self, percepcao):
        '''
        param Percepcao : percepcao  Modelo do ambiente
        return: Accao , accao que deve ser tomada, tendo em conta a percepcao do ambiente e o controlo definido
        '''
        return self.__controlo.processar(percepcao)

    def __actuar(self, accao):
        '''
        param Accao: accao a ser tomada
        '''
        if accao is not None:
            mover = Mover(self.__amb,accao)
            mover.mover()
    
    def obter_plano(self):

        return self.__controlo.obter_plano()
    

