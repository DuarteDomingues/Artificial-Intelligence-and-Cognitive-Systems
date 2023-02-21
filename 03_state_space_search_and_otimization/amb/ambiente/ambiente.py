

class Ambiente:

    def __init__(self, larg, alt, estado_origem, dir_ini, alvo, obstaculos):
        self.__larg = larg
        self.__alt = alt
        self.__estado_origem = estado_origem
        self.__estado_agente = self.__estado_origem
        self.__alvo = alvo
        self.__dir_ini =  dir_ini
        self.__obstaculos = obstaculos
    

    def obter_origem(self):
        return self.__estado_origem
    
    def obter__larg(self):
        return self.__larg
    
    def obter__alt(self):
        return self.__alt

    def obter_alvo(self):
        return self.__alvo
    
    def obter_estado_agente(self):
        return self.__estado_agente

    
    def obter_obstaculos(self):
        return self.__obstaculos
    
    def obter_dir_ini(self):
        return self.__dir_ini
    

    def alterar_pos_agente(self, estado):
        self.__estado_agente = estado


    def obter_pos_agente(self):

        return (self.__estado_agente.obter_x(), self.__estado_agente.obter_y())
    
