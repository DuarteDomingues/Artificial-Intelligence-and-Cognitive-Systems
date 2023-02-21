from lib.pee.modprob.estado import Estado

class EstadoTrajeto(Estado):

    def __init__(self,x,y):

        self.__x = x
        self.__y = y
    
    def obter_x(self):
        return self.__x
    
    def obter_y(self):
        return self.__y
    
    def __chave(self):
        return self.__x, self.__y
        
    def __hash__(self):
        return hash(self.__chave())


    
        
