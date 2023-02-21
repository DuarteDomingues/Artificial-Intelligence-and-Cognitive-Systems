
class Solucao:
    def __init__(self):
        self.__caminho = []

    def inserir_solucao(self, no):
        self.__caminho.insert(0, no)

    def obter_caminho(self):
        return self.__caminho
    
    def set_caminho(self, caminho):

        self.__caminho = caminho