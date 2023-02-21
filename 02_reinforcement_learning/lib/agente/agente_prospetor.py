from amb.ambiente.percepcao import Percecao
from amb.ambiente.mover import Mover
class AgenteProspector():

    def __init__(self, controlo,amb):
        '''
        param Controlo: controlo , algoritmo de busca do agente
        '''
        self.__controlo = controlo
        self.__amb = amb
        self.__primeira_accao =True
        #atuar acao

        
    def executar(self):

        if (self.__primeira_accao):
            self.__actuar(self.__amb.obter_dir_ini())
            self.__primeira_accao=False
        
        else:

            percepcao = self.__percepcionar()
            accao = self.__processar(percepcao)
            self.__actuar(accao)  #atuar acao no mundo
            if self.__controlo.acabou:
                self.reiniciar()


    def __percepcionar(self):
        '''
        Avalia o ambiente em que se encontra o agente, procura alvos e identifica obstaculos

        param : 
        return: Percepcao , um modelo do ambiente 
        '''
        percecao = Percecao(self.__amb)
        return percecao

    def __processar(self, percepcao):
        '''
        param Percepcao : percepcao  Modelo do ambiente
        return: Accao , accao que deve ser tomada, tendo em conta a percepcao do ambiente e o controlo definido
        '''
        return self.__controlo.processar(percepcao)

    def __actuar(self, accao):
        '''
        param Accao: accao a ser tomada
        '''
        if accao is not None:
            mover = Mover(self.__amb,accao)
            mover.mover()
    

    def reiniciar(self):
        #self.__primeira_accao=True
        self.__amb.reiniciar()
        self.__controlo.limpar()

        
        
        
        #reset mundo
            
        
        
