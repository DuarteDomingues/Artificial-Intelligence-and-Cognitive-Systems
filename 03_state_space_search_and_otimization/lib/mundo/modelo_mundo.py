from lib.plantraj.trajeto.estado_trajeto import EstadoTrajeto
from amb.ambiente.dir_amb import DirAmb
from lib.plantraj.trajeto.operador_mover import OperadorMover

class ModeloMundo:

    def __init__(self, larg=None, alt=None, origem=None, dir_ini=None, alvo=None, obstaculos=None):

        dirs = [d.value for d in DirAmb]
        self.__operadores = [OperadorMover(self,dir) for dir in dirs]

        self.__larg = larg
        self.__alt = alt
        self.__origem = origem
        self.__estado = origem
        self.__alvo = alvo
        self.__dir_ini =  dir_ini
        self.__obstaculos = obstaculos
        self.__alterado=False


    def reiniciar(self):
        self.__estado = self.__origem
    

    def atualizar(self, percecao):

        estado_percecao = percecao.obter_agente()
        self.__obstaculos = percecao.obter_obstaculos()
        self.__alvo = percecao.obter_alvo()

        if (self.__estado != estado_percecao):

            self.__alterado = True
        
        else:
            self.__alterado = False
        

        self.__estado = percecao.obter_agente()

    def alterar_estado_agente(self, estado):

        for obs in self.__obstaculos:
            if (estado.obter_x() == obs.obter_x()) and (estado.obter_y() == obs.obter_y()):
                return None
        
        return estado
            

    def obter_alterado(self):
        return self.__alterado


    def obter__larg(self):
        return self.__larg
    
    def obter__alt(self):
        return self.__alt

    def obter_alvo(self):
        return self.__alvo

    def obter_estado(self):
        return self.__estado

    def obter_obstaculos(self):
        return self.__obstaculos
    
    def obter_dir_ini(self):
        return self.__dir_ini
    
    def obter_operadores(self):
        return self.__operadores