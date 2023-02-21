
class Mover():

    def __init__(self,amb, a):
        self.__amb = amb
        self.__a = a
        
    def mover(self):

        #vai pegar na posicao do agente
        # verificar se e obstaculo, se nao for obstaculo: aplicar mover
        # altera a posicao do agente no ambiente

        novas_coords = (self.__amb.obter_pos_agente()[0]+self.__a[0],self.__amb.obter_pos_agente()[1]+self.__a[1])

        if self.__verificar_obs(novas_coords)==False:
            self.__amb.alterar_pos_agente(novas_coords)
        

    def __verificar_obs(self, coords):

        #verificar se a acao resulta num obstaculo

        if coords in self.__amb.obter_obstaculos():
            return True
        else:
            return False


        
        

