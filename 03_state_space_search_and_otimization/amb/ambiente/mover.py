
class Mover():

    def __init__(self,amb, operador):
        self.__amb = amb
        self.__operador = operador
        
    def mover(self):

        #vai pegar na posicao do agente
        # verificar se e obstaculo, se nao for obstaculo: aplicar mover
        # altera a posicao do agente no ambiente

        novo_estado = self.__operador.aplicar(self.__amb.obter_estado_agente())

        if novo_estado is not None:
            self.__amb.alterar_pos_agente(novo_estado)
        

