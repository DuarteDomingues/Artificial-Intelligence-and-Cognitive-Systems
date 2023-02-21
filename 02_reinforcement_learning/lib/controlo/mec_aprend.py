from lib.apr_ref.memoria_esparca import MemoriaEsparca
from lib.apr_ref.memoria_experiencia import MemoriaExperiencia
from lib.apr_ref.sel_acao_EGreedy import SelAccaoEGreedy
from lib.apr_ref.aprend_q import QLearning
from lib.controlo.metodos import Metodos
from lib.apr_ref.aprend_qme import QME
from lib.apr_ref.aprend_dyna_q import DynaQ

class MecAprend:

    def __init__(self, accoes, metodo):
       
        alfa = 0.5
        gama = 0.9
        epsilon = 0.01
        dim_max = 10
        num_sim = 100
        self.__accoes = accoes

        self.__mem_aprend = None
        self.__sel_acao = None
        self.__aprend_ref = None

        if metodo==Metodos.q_learning.value:

            self.__mem_aprend = MemoriaEsparca(epsilon)
        
            self.__sel_acao = SelAccaoEGreedy(self.__mem_aprend, self.__accoes, epsilon)
            self.__aprend_ref = QLearning(self.__mem_aprend, self.__sel_acao, alfa, gama)
        
        elif metodo == Metodos.q_learning_qme.value:
            
            self.__mem_aprend = MemoriaEsparca(epsilon)
        
            self.__sel_acao = SelAccaoEGreedy(self.__mem_aprend, self.__accoes, epsilon)
            self.__aprend_ref = QME(self.__mem_aprend, self.__sel_acao, alfa, gama, num_sim ,dim_max)

        elif metodo == Metodos.dyna_q.value:

            self.__mem_aprend = MemoriaEsparca(epsilon)
            self.__sel_acao = SelAccaoEGreedy(self.__mem_aprend, self.__accoes, epsilon)
            self.__aprend_ref = DynaQ(self.__mem_aprend, self.__sel_acao, alfa, gama, num_sim)

    
    def aprender(self, s, a, r, sn):
        '''
        Associa a um par estado-accao um custo ou recompensa á transicao para o estado seguinte 
        '''
        
        self.__aprend_ref.aprender(s, a, r, sn)

    
    def selecionar_acao(self, s):
        return self.__sel_acao.selecionar_acao(s)
    
