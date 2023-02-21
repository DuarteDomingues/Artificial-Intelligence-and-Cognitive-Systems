from random import sample


class MemoriaExperiencia:

    def __init__(self,dim_max):
        self.__dim_max = dim_max
        self.__memoria = []
    
    def atualizar(self, e):

        if len(self.__memoria) == self.__dim_max:
            self.__memoria.pop()
        self.__memoria.append(e)
    
    def amostrar(self,n):
        n_amostras = min(n, len(self.__memoria))
        return sample(self.__memoria, n_amostras)
