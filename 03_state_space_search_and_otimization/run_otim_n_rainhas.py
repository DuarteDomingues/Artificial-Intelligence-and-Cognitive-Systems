from lib.otimizacao.hill_climbing.hill_climbing_estocastico import HillClimbingEstocastico
from lib.otimizacao.simmulated_annealing.sim_anealing import SimulatedAnnealing
from lib.otimizacao.res_problemas.problema_n_rainhas import ProblemaNRainhas
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import image as mpimg

T_INICIAL =25


def visualizar(estado_otimo):

    n = len(estado_otimo)
    fig, ax = plt.subplots(nrows=n , ncols=n )
    img = mpimg.imread('imgs/rainha.png') 
    img2 = mpimg.imread('imgs/fundo.png') 
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
    for linha in range(n):
        for col in range(n):
            if (linha, col) in estado_otimo:
                ax[linha, col].imshow(img,aspect='auto')
            else:
                ax[linha, col].imshow(img2,aspect='auto')
            
            ax[linha, col].axis('off')
    
    plt.axis('off')
    plt.show()
    

estado_inicial = [(0,0),(2,0),(1,0),(3,0),(4,1),(1,2),(5,2),(5,3)]

def run_hill_climbing_estocastico():


    problema = ProblemaNRainhas( estado_inicial)
    hill_estocastico = HillClimbingEstocastico(problema)
    estado_otimo, custo_otimo, ult_itr = hill_estocastico.run(max_itr=10000)
    print("custo: ",custo_otimo )
    print("ultima iteração: ", ult_itr)
    print("estado ótimo: ", estado_otimo)
    visualizar(estado_otimo)

   
def run_hill_sim_annealing():


    problema = ProblemaNRainhas( estado_inicial)
    sim__anealing = SimulatedAnnealing(problema, T_INICIAL)
    estado_otimo, custo_otimo, ult_itr = sim__anealing.run(max_itr=1000)
    print("custo: ",custo_otimo )
    print("ultima iteração: ", ult_itr)
    print("estado ótimo: ", estado_otimo)
    visualizar(estado_otimo)



run_hill_sim_annealing()
run_hill_climbing_estocastico()





