from amb.ambiente.criar_ambiente.criar_ambiente import criar_ambiente
from lib.agente.agente_prospetor import AgenteProspector
from lib.controlo.controlo_delib.controlo_delib import ControloDelib
from lib.pee.melhorprim.procura_aa import ProcuraAA
from lib.plantraj.plan_pee.plan_pee import PlanPee
from lib.modo_grafico.grafico import Mostrar
from lib.pee.mecanismos_procura.no import No

amb = criar_ambiente("amb2.txt")

mec_pee = ProcuraAA()
planeador = PlanPee(mec_pee)
controlo = ControloDelib(planeador)
agente = AgenteProspector(controlo,amb)

m = Mostrar(amb, agente)
m.run()


