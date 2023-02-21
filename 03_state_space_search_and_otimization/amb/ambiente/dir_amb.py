from enum import Enum

class DirAmb(Enum):

    CIMA = (-1,0)
    BAIXO = (1,0)
    ESQUERDA = (0,-1)
    DIREITA = (0,1)
    CIMA_ESQUERDA = (-1,-1)
    CIMA_DIREITA = (-1,1)
    BAIXO_ESQUERDA = (1,-1)
    BAIXO_DIREITA = (1,1)
