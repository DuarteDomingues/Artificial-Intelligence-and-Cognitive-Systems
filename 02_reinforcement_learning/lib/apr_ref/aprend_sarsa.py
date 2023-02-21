from lib.apr_ref.aprend_ref import AprendRef


class SARSA(AprendRef):

    def __init__(self, mem_aprend, sel_accao, alfa, gama):
       
        super().__init__(mem_aprend, sel_accao, alfa, gama)
               
    
    def aprender(self, s, a, r, sn, an):
        '''
        Guarda em memoria um par de (estado acao) com uma recompensa.
        
        param s : Estado
        param a : Accao
        param r : double
        param sn: Estado
        param an: Accao
        '''
                
        qsa = self._mem_aprend.Q(s, a)
        qsnan = self._mem_aprend.Q(sn, an)
        q = qsa + self._alfa* (r + self._gama * qsnan - qsa)
        self.__mem_aprend.atualizar(s,a,q)

        #Qant = mem.obter(s, a)
        
        #q = Qant + self._alfa * (r + self._gama * maxA - Qant)
        #mem.atualizar(s, a, q)

