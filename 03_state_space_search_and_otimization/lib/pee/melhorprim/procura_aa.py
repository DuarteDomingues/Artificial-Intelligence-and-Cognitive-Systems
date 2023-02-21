from lib.pee.melhorprim.procura_melhor_prim import ProcuraMelhorPrim


class ProcuraAA(ProcuraMelhorPrim):

    def f(self, no, peso=0):

        self.__peso = peso
        '''
        returns double
        '''

        return no.obter_custo() + ((1+self.__peso))*self.problema.heuristica(no.obter_estado())

 #   return node.cost + ((1 + self.__weight)*self.problem.heuristic(node.state))
