from lib.apr_ref.aprend_q import QLearning
from lib.apr_ref.memoria_experiencia import MemoriaExperiencia

class QME(QLearning):
 
    def __init__(self, mem_aprend, sel_accao, alfa, gama, num_sim, dim_max):
       
        super().__init__(mem_aprend, sel_accao,alfa, gama)
        self.__num_sim = num_sim
        self.__memoria_experiencia = MemoriaExperiencia(dim_max)               
    
    def aprender(self, s, a, r, sn):
        '''
        Guarda em memoria um par de (estado acao) com uma recompensa.
        
        param s : Estado
        param a : Accao
        param r : double
        param sn: Estado
        '''
        super().aprender(s, a, r, sn)
        
        e = (s,a,r,sn)
        self.__memoria_experiencia.atualizar(e)
        self.simular()
    
    def simular(self):

        amostras = self.__memoria_experiencia.amostrar(self.__num_sim)
        for (s,a,r,sn) in amostras:
            super().aprender(s,a,r,sn)


