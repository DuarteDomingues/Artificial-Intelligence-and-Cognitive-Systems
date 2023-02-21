from lib.pee.mecanismos_procura.memoria_procura import MemoriaProcura
import heapq

class MemoriaPrioridade(MemoriaProcura):

    def __init__(self, prioridade):
        super().__init__()
        self.__prioridade = prioridade


    #implementar aqui o metodo de adicionar e remover maybe

    def _inserir_fronteira(self, no):
        prio =  self.__prioridade.prioridade(no)
        heapq.heappush(self._fronteira, (prio, no))
    
    def _remover_fronteira(self):
        _, no = heapq.heappop(self._fronteira)
        return no

