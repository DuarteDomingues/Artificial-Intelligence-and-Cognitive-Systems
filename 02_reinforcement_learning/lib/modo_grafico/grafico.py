import numpy as np
import pygame as pg
import sys


LARGURA_JANELA = 600
ALTURA_JANELA = 600
FPS = 30


class Mostrar():

    def __init__(self, amb, agente):

        self.__ambiente = amb
        self.__agente = agente
        self.__larg = self.__ambiente.obter__larg()
        self.__alt = self.__ambiente.obter__alt()
                
        self.__larg_bloco = int(LARGURA_JANELA/self.__larg)
        self.__alt_bloco = int(ALTURA_JANELA/self.__alt)

        self.__ecra = pg.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))        
        
        self.__y_coords = np.arange(0, LARGURA_JANELA, self.__larg_bloco)
        self.__x_coords = np.arange(0, ALTURA_JANELA, self.__alt_bloco)

        #imagens
        self.__setas_img = []
        self.__obstaculo_img = None
        self.__agente_img = None
        self.__alvo_img = None
        self.__carregar_imgs()
        
    

    def run(self):
        pg.init()
        clock = pg.time.Clock()
        running = True

        while (running):
            dt = clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.__mostrar_amb()
        
         
            self.__agente.executar()
            pg.display.update()
      


    
    def __carregar_imgs(self):

        #carregar imagens das setas

        seta_cima = pg.transform.scale(pg.image.load('lib/modo_grafico/recursos/setas/arrow_top.png'),
                                      ( self.__larg_bloco, self.__alt_bloco))
        seta_baixo = pg.transform.scale(pg.image.load('lib/modo_grafico/recursos/setas/arrow_bot.png'),
                                      ( self.__larg_bloco, self.__alt_bloco))
        seta_esquerda = pg.transform.scale(pg.image.load('lib/modo_grafico/recursos/setas/arrow_left.png'),
                                      ( self.__larg_bloco, self.__alt_bloco))
        seta_direita = pg.transform.scale(pg.image.load('lib/modo_grafico/recursos/setas/arrow_right.png'),
                                      ( self.__larg_bloco, self.__alt_bloco))
        seta_cima_direita = pg.transform.scale(pg.image.load('lib/modo_grafico/recursos/setas/arrow_top_right.png'),
                                      ( self.__larg_bloco, self.__alt_bloco))
        seta_cima_esquerda = pg.transform.scale(pg.image.load('lib/modo_grafico/recursos/setas/arrow_top_left.png'),
                                      ( self.__larg_bloco, self.__alt_bloco))
        seta_baixo_direita = pg.transform.scale(pg.image.load('lib/modo_grafico/recursos/setas/arrow_bot_right.png'),
                                      ( self.__larg_bloco, self.__alt_bloco))
        seta_baixo_esquerda = pg.transform.scale(pg.image.load('lib/modo_grafico/recursos/setas/arrow_bot_left.png'),
                                      ( self.__larg_bloco, self.__alt_bloco))

        #carregar imagem agente
        self.__agente_img = pg.transform.scale(pg.image.load('lib/modo_grafico/recursos/agente.png'),
                                      ( self.__larg_bloco, self.__alt_bloco))
        
        #carregar imagem obstaculo
        self.__obstaculo_img = pg.transform.scale(pg.image.load('lib/modo_grafico/recursos/obstaculo.png'),
                                      ( self.__larg_bloco, self.__alt_bloco))
        
        #carregar imagem alvo
        self.__alvo_img = pg.transform.scale(pg.image.load('lib/modo_grafico/recursos/tomato.png'),
                                      ( self.__larg_bloco, self.__alt_bloco))

        self.__setas_img = [seta_cima,seta_baixo,seta_esquerda,
        seta_direita,seta_cima_direita,seta_cima_esquerda,seta_baixo_direita,seta_baixo_esquerda]
    

    def __mostrar_amb(self):

        for x in self.__x_coords:
            for y in self.__y_coords:
                if ((self.__x_coords[self.__ambiente.obter_pos_agente()[0]]==x and  self.__y_coords[self.__ambiente.obter_pos_agente()[1]]==y)== False):
                    rect = pg.Rect(y, x, self.__larg_bloco, self.__alt_bloco)
                    #pintar o bloco
                    pg.draw.rect(self.__ecra, (20, 20, 20), rect)
                    #pintar o outline do bloco
                    pg.draw.rect(self.__ecra, (101,67,33), rect,1)
                
                    #mostrar imagem de agente
        agente_pos = self.__ambiente.obter_pos_agente()
        self.__ecra.blit(self.__agente_img, (self.__y_coords[agente_pos[1]],
                                                self.__x_coords[agente_pos[0]]))

        #mostrar imagem de obstaculo
        obstaculos = self.__ambiente.obter_obstaculos()
        for obs in obstaculos:
            self.__ecra.blit(self.__obstaculo_img, (self.__y_coords[obs[1]],
                                                self.__x_coords[obs[0]]))
        #mostrar imagem de alvo
        alvo = self.__ambiente.obter_alvo()
        self.__ecra.blit(self.__alvo_img, (self.__y_coords[alvo[1]],
                                                self.__x_coords[alvo[0]]))
        











        


    
    



   # def __mostrar_amb(self):


                





