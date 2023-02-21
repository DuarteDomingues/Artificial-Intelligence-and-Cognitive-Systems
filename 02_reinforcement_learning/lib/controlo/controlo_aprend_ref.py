from amb.ambiente.acoes_amb import AcoesAmb
from lib.controlo.mec_aprend import MecAprend
from lib.controlo.controlo import Controlo


class ControloAprendRef(Controlo):
   

    def __init__(self, metodo):
       
        self.__rmax = 100
        accoes = [acao.value for acao in AcoesAmb]
        self.__mec_aprend = MecAprend(accoes, metodo)
        self.acabou = False
        self.__s = None
        self.__a = None


        
    def processar(self, percepcao):
        '''
        Processa o ambiente como o agente o percebe, selecionando e aplicando a melhor accao
        param percepcao: Percepcao
        return: Accao
        '''
        sn = percepcao.obter_pos_agente()
        an = self.__mec_aprend.selecionar_acao(sn)
        
        if(self.__s != None):

            r = self.__gerar_reforco(percepcao, sn, an)
            self.__mec_aprend.aprender(self.__s, self.__a, r, sn)
        
   
        self.__a = an
        self.__s = sn
        
        return an
    
    def __gerar_reforco(self, percepcao,s,an):
        '''
        gera o reforco associado ao movimento
        param percepcao: Percepcao
        return: double
        '''
        # # deve gerar um reforco, tendo em conta o custo do movimento (negativo), recompensa maxima (ao atingir o alvo), recompensa maxima (colisao, negativo)
        
        #atingiu alvo
        if percepcao.atingiu_alvo():
            self.acabou = True
            return self.__rmax
        
        custo = percepcao.verificar_custo_mov(s) * -1.0
        if(percepcao.atingiu_obstaculo(s,an)==True):
            custo -= self.__rmax
       
        return custo
    
    def limpar(self):
        self.__s = None
        self.__a = None
        self.acabou = False