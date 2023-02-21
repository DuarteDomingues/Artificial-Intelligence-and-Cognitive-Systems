from lib.pee.mecanismos_procura.mecanismo_procura import MecanismoProcura
from lib.pee.mecanismos_procura.memoria_prio import MemoriaPrioridade

class ProcuraMelhorPrim(MecanismoProcura):

    def _iniciarMemoria(self):
        return  MemoriaPrioridade(self)
    
    def prioridade(self, no):
       
        return self.f(no)


    def f(self, no):
        raise NotImplementedError()
