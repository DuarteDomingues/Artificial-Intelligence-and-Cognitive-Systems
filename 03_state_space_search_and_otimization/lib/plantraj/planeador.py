class Planeador:

    def planear(self, modelo_pan, estado_inicial, objectivo):
        '''
        param modelo_pan: ModeloPlan
        param estado_inicial: Estado
        param objetivo: Estado
        '''
        raise NotImplementedError
    
    def obter_operador(self):
        '''
        return: Operador
        '''
        raise NotImplementedError

    def plano_pendente(self):
        '''
        Indica se existe um plano pendente
        return: Boolean
        '''
        raise NotImplementedError

    def terminar_plano(self):
        raise NotImplementedError


