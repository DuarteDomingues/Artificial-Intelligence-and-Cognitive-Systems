#no
#estado

#queue<no> fronteira
#map<estado, no> nosExplorados


class MemoriaProcura:

    def __init__(self):

        self.limpar()
        
    def limpar(self):
        self._fronteira = []
        self._explorados = {}
        self.__fechados = {}

    def inserir(self, no):

        estado = no.obter_estado()
        no_mem = self._explorados.get(estado)

        if (no_mem is None or no.obter_custo() < no_mem.obter_custo()):
            #fazer metodo inserir_fronteira
            #posso ter um metodo de adicionar na fronteira que pode ser overwrited
            self._inserir_fronteira(no)
            self._explorados[estado] = no
    
    def remover(self):
        #fazer metodo remover fronteira
        no = self._remover_fronteira()
        self.__fechados[no.obter_estado()] = no
        return no
    
    def fronteira_vazia(self):

        if self._fronteira is None or len(self._fronteira)==0:
            return True
        else:
            return False
     
    

    def _inserir_fronteira(self, no):
        #self._fronteira.append(no)
        return self._fronteira.append(no)


    def _remover_fronteira(self):
        return self._fronteira.pop(0)
    


    