
class Problema():

    def __init__(self, estado_inicial):
        
        self.__estado_inicial = estado_inicial
    
    @property
    def estado_inicial(self):
        return self.__estado_inicial
    
    def obter_estado_sucessor(self, estado):
        return NotImplementedError()
    
    def obter_custo_estado(self, estado):
        return NotImplementedError()
    
    def obter_estados_vizinhos(self, estado):
        return NotImplementedError()
    
    def obter_estado_aleatorio(self,estado):
        return NotImplementedError()
    
    def obter_vizinho_aleatorio(self, vizinhos):
        return NotImplementedError()
    

    



    