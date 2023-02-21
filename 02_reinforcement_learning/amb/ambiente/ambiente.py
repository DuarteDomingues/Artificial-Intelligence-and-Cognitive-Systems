

class Ambiente:

    def __init__(self, larg, alt, origem, dir_ini, alvo, obstaculos):
        self.__larg = larg
        self.__alt = alt
        self.__pos_origem = origem
        self.__pos_agente = origem
        self.__alvo = alvo
        self.__dir_ini =  dir_ini
        self.__obstaculos = obstaculos
    
    def obter__larg(self):
        return self.__larg
    
    def reiniciar(self):
        self.__pos_agente = self.__pos_origem
    
    def obter__alt(self):
        return self.__alt

    def obter_alvo(self):
        return self.__alvo
    def obter_pos_agente(self):
        return self.__pos_agente
    
    def alterar_pos_agente(self, pos):
        self.__pos_agente = pos

    def obter_obstaculos(self):
        return self.__obstaculos
    
    def obter_dir_ini(self):
        return self.__dir_ini
