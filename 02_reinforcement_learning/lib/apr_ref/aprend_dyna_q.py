from lib.apr_ref.aprend_q import QLearning
from lib.apr_ref.modelo_tr import ModeloTR

class DynaQ(QLearning):
 
    def __init__(self, mem_aprend, sel_accao, alfa, gama, num_sim):
        
        super().__init__(mem_aprend, sel_accao,alfa, gama)
        self.__num_sim = num_sim
        self.__modelo = ModeloTR()               
    
    def aprender(self, s, a, r, sn):
        '''
        Guarda em memoria um par de (estado acao) com uma recompensa.
        
        param s : Estado
        param a : Accao
        param r : double
        param sn: Estado
        '''
        super().aprender(s, a, r, sn)
        self.__modelo.atualizar(s, a, r, sn)
        self.simular()
    
    
    def simular(self):

        for i in range(self.__num_sim):
            s,a,r,sn = self.__modelo.amostrar()
            super().aprender(s,a,r,sn)




