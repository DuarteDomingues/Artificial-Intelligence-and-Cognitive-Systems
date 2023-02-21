from lib.pee.mecanismos_procura.no import No
from lib.pee.modprob.solucao import Solucao
import sys

class MecanismoProcura:

    def __init__(self):
        self.__memoria = self._iniciarMemoria()
        self.problema = None
    
    def _iniciarMemoria(self):
        raise NotImplementedError()
    
    def resolver(self, problema, profMax=sys.maxsize):
        self.problema = problema
        self.__memoria.limpar()
        no = No(problema.obter_estado_inicial())
        self.__memoria.inserir(no)

        while self.__memoria.fronteira_vazia() is False:
            no = self.__memoria.remover()
            if self.problema.objetivo(no.obter_estado()):    

                return self.__gerar_solucao(no)
            
            elif no.obter_profundidade() < profMax:
                self.__expandir(no)
            
            #sus
            elif no.obter_profundidade() >= profMax:
                return self.__gerar_solucao(no)
        
        #VER
    

    '''
	 Aplica os operadores definidos para o problema no nó.
	 param no
    '''

    def __expandir(self, no):
        estado = no.obter_estado()
        for operador in self.problema.obter_operadores():
            estado_suc = operador.aplicar(estado)
            if (estado_suc is not None):
                noSuc = No(estado_suc,operador,no)
                self.__memoria.inserir(noSuc)
    

    '''
	Gera a solucao para um problema apos ter sido achada uma solucao num
	determinado nó.
	  
	Tendo como ponto de partida o nó final, irá navegar pela arvore até
	atingir a sua raiz, devolvendo o caminho percorrido como a solucao para o
	problema em causa.
	  
	param noFinal : no onde foi encontrada a solucao para o problema
	  
	return Solucao neste caso, percurso a percorrer
	 '''
    def __gerar_solucao(self, no_final):

        solucao_percurso = Solucao()
        no = no_final

        while no is not None:
            solucao_percurso.inserir_solucao(no)
            antecessor = no.obter_antecessor()
            no = antecessor
        
        #ver esta parte melhor
        
        return solucao_percurso


