from lib.pee.modprob.operador import Operador
from lib.plantraj.trajeto.estado_trajeto import EstadoTrajeto
from math import sqrt

class OperadorMover(Operador):

    def __init__(self, modelo_mundo, dir):

        self.__modelo_mundo = modelo_mundo
        self.__dir = dir
        
    
    @property
    def dir(self):
        return self.__dir


    def aplicar(self, s):
        '''
            Se este operador for selecionado, altera a posicao do agente.
            param estado: Estado
                                estado atual do agente
            return: Estado
                        estado futuro do agente, depois de lhe ser aplicado o movimento
        '''

        #posicoes de s
        pos_x_atual = s.obter_x()
        pos_y_atual = s.obter_y()

        pos_x_dir = self.__dir[0]
        pos_y_dir = self.__dir[1]

        sn = EstadoTrajeto(pos_x_atual+pos_x_dir,pos_y_atual+pos_y_dir)
        estado_operador = self.__modelo_mundo.alterar_estado_agente(sn)

        return estado_operador
    
    #rever
    def custo(self,s, sn):

        aux_x = (s.obter_x() - sn.obter_x())**2
        aux_y = (s.obter_y() - sn.obter_y())**2
        return sqrt(aux_x + aux_y)
        