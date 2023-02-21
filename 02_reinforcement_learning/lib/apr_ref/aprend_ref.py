class AprendRef:

    def __init__(self, mem_aprend, sel_accao, alfa, gama):
        '''
        param mem_aprend: MemoriaAprend
        param sel_accao: SelAccao
        param alfa: double
        param gama: double
        '''
        self._mem_aprend = mem_aprend
        self._sel_accao = sel_accao
        self._alfa = alfa
        self._gama = gama

    def aprender(self, s, a, r, sn, an=None):
        '''
        Tendo em conta o estado, a acao, a recompensa, o agente aprende se a acao é ou não vantajosa
        param s: Estado
        param a: Accao
        param r: double
                    recompensa ou custo
        param sn: Estado
                    estado seguinte
        param an: Accao=None
        '''
        raise NotImplementedError
    
