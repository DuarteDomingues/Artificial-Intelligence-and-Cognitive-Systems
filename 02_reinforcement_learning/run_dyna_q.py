from amb.ambiente.acoes_amb import AcoesAmb
from amb.ambiente.criar_ambiente.criar_ambiente import criar_ambiente
from lib.controlo.controlo_aprend_ref import ControloAprendRef
from lib.agente.agente_prospetor import AgenteProspector
from lib.modo_grafico.grafico import Mostrar
from lib.controlo.metodos import Metodos

amb = criar_ambiente("amb1.txt")


controlo = ControloAprendRef(Metodos.dyna_q.value)
agente = AgenteProspector(controlo,amb)


m = Mostrar(amb, agente)
m.run()