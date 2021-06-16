from typing import List, Tuple
from queue import PriorityQueue

class Prato:
    def __init__(self, nome, valor, experiencia):
        self.nome = nome
        self.valor = valor
        self.experiencia = experiencia

    def __str__(self):
        return f"{self.nome}"

class Restaurante:
    def __init__(self, valor_limite, pratos_escolhidos, pratos_disponiveis):
        self.pratos_escolhidos = pratos_escolhidos
        self.pratos_disponiveis = pratos_disponiveis
        self.valor = sum([objeto.valor for objeto in pratos_escolhidos])
        self.experiencia = sum([objeto.experiencia for objeto in pratos_escolhidos])
        proporcoes = [objeto.valor/objeto.experiencia for objeto in pratos_disponiveis] + [0]
        melhor_proporcao = max(proporcoes)
        self.melhor_possivel = self.experiencia + (valor_limite - self.valor) * melhor_proporcao


    def __ge__(self, other):
        return self.melhor_possivel <= other.melhor_possivel

    def __gt__(self, other):
        return self.melhor_possivel < other.melhor_possivel

    def __repr__(self):
        
        itens = ([str(objeto.nome) for objeto in self.pratos_escolhidos])
        return itens

class BranchAndBound:
    def __init__(self, valor_limite, pratos_disponiveis):
        self.valor_limite = valor_limite
        self.pratos_disponiveis = pratos_disponiveis
        

    def escolher(self, verbose=False):
        raiz = Restaurante(self.valor_limite, [], self.pratos_disponiveis)
        melhor_solucao = raiz
        fila = PriorityQueue()
        fila.put(raiz)

        while not fila.empty():
            proximo = fila.get()
            if proximo.melhor_possivel <= melhor_solucao.experiencia or proximo.valor > self.valor_limite:
                continue
            if proximo.valor > melhor_solucao.valor:
                melhor_solucao = proximo
            n_opcoes = len(proximo.pratos_disponiveis)
            for i in range(n_opcoes):
                objeto_escolhido = proximo.pratos_disponiveis.pop(i)
                fila.put(Restaurante(self.valor_limite, proximo.pratos_escolhidos + [objeto_escolhido], list(proximo.pratos_disponiveis)))
                proximo.pratos_disponiveis.insert(i, objeto_escolhido)

        return melhor_solucao


def melhor_experiencia(L: int, C: List[Tuple[str, int, int]]) -> List[str]:
    pratos_objetos = []
    for prato in C:
         pratos_objetos.append(Prato(prato[0], prato[1], prato[2]))

    mb = BranchAndBound(L, pratos_objetos)
    escolhidos = mb.escolher()
    
    aa = [a.nome for a in escolhidos.pratos_escolhidos]
    
    return aa
    


if __name__ == "__main__":
    help(melhor_experiencia)