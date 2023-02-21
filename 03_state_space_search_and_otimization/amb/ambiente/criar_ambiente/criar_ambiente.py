from amb.ambiente.estados import Estados
from amb.ambiente.ambiente import Ambiente
from amb.ambiente.dir_amb import DirAmb
from lib.plantraj.trajeto.estado_trajeto import EstadoTrajeto

def criar_ambiente(amb):

    f = open("amb/ambiente/criar_ambiente/ambientes/"+ str(amb) , "r")
    linhas = f.read().splitlines()

    alt_mapa = len(linhas)
    larg_mapa = len(linhas[0])

    origem = None
    alvo = None
    obstaculos = []
    dir_ini = None


    y = 0
    for linha in linhas:
        x = 0
        for estado in linha:
            if estado == Estados.ORIGEM_DIREITA.value:
                
                origem = EstadoTrajeto(y, x)
             
                dir_ini = DirAmb.DIREITA.value
            
            elif estado == Estados.ORIGEM_ESQUERDA.value:

                origem = EstadoTrajeto(y, x)
                dir_ini = DirAmb.ESQUERDA.value
                
            elif estado == Estados.OBSTACULO.value:
                obstaculos.append(EstadoTrajeto(y, x))
                
            elif estado == Estados.ALVO.value:
                alvo = EstadoTrajeto(y, x)
           
            x += 1
        y += 1
    
    return Ambiente(larg_mapa,alt_mapa,origem,dir_ini,alvo,obstaculos)


