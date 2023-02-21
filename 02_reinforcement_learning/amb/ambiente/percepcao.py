
class Percecao():

    def __init__(self, ambiente):
        self.__ambiente = ambiente
        self.__obstaculos = self.__ambiente.obter_obstaculos()
        self.__pos_agente = self.__ambiente.obter_pos_agente()
        self.__alvo = self.__ambiente.obter_alvo()
    
    def obter_pos_agente(self):
        return self.__pos_agente
    
    def obter_obstaculos(self):
        return self.__obstaculos

    def atingiu_obstaculo(self,s,an):

        #verifica se agente atingiu um obstaculo

        if  (s[0]== self.__pos_agente[0]) and  (s[1]== self.__pos_agente[1]):

            return True
        else:
            return False

    def atingiu_alvo(self):

        #verifica se agente atingiu um alvo

        if self.__pos_agente == self.__alvo:
            return True
        else:
            return False
 
    
    def verificar_custo_mov(self,s):
        
        #verificar a dimensão da ação é dois passos
        #retorna custo do movimento
        
        if (s[0]== self.__pos_agente[0]-1 or s[0] == self.__pos_agente[0]+1) and (s[1]== self.__pos_agente[1]-1 or s[1] == self.__pos_agente[1]+1):
            return 0.2
    
        else:
            return 0.1
    
    
    

 
    
  
        




    


        

    



    




