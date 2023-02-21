from lib.apr_ref.aprend_ref import AprendRef
from lib.apr_ref.sel_acao import SelAcao
from lib.apr_ref.memoria_aprend import MemoriaAprend

class MecanismoAprendRef():

    def __init__(self, accoes):
        self.__accoes = accoes
        self.__aprend_ref = AprendRef()
        self.__sel_accao = SelAcao()
        self.__mem_aprend = MemoriaAprend()
    
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
