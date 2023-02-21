from lib.otimizacao.hill_climbing.hill_climbing_estocastico import HillClimbingEstocastico
from lib.otimizacao.simmulated_annealing.sim_anealing import SimulatedAnnealing
from lib.otimizacao.res_problemas.problema_caixeiro_viajante import ProblemaCaixeiroViajante
from lib.otimizacao.res_problemas.dados.tabelas import tabela_custo, cidades

T_INICIAL =25
estado_inicial = [
"Berlin", "Paris", "London", "Madrid", "Amsterdam",
"Vienna", "Budapest", "Brussels", "Lisbon", "Rome"
]


def run_hill_sim_annealing():

    problema = ProblemaCaixeiroViajante(estado_inicial, tabela_custo, cidades )
    sim__anealing = SimulatedAnnealing(problema, T_INICIAL)
    estado_otimo, custo_otimo, ult_itr = sim__anealing.run(max_itr=1000)
    print("------- Simulated Annealing ---------")
    print("custo: ",custo_otimo )
    print("ultima iteração: ", ult_itr)
    print("estado ótimo: ", estado_otimo)

def run_hill_climbing_estocastico():

    problema = ProblemaCaixeiroViajante(estado_inicial, tabela_custo, cidades )
    sim__anealing = HillClimbingEstocastico(problema)
    estado_otimo, custo_otimo, ult_itr = sim__anealing.run(max_itr=1000)
    print("------- Hill Climbing ---------")
    print("custo: ",custo_otimo )
    print("ultima iteração: ", ult_itr)
    print("estado ótimo: ", estado_otimo)



run_hill_climbing_estocastico()
run_hill_sim_annealing()





