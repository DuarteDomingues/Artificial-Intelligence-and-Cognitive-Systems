

class Percecao():

    def __init__(self, amb):
        self.__amb = amb
        self.__obstaculos = self.__amb.obter_obstaculos()
        self.__agente = self.__amb.obter_estado_agente()
        self.__alvo = self.__amb.obter_alvo()
    

    def obter_obstaculos(self):
        return self.__obstaculos
    
    def obter_agente(self):
        return self.__agente

    def obter_alvo(self):
        return self.__alvo
    

  
        

    



    




