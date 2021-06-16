from typing import List, Tuple

#Professor o senhor vai me endoidecer com essas questões
def encontra_rota(M: int, N: int, L: int, C: int, B: List[Tuple[int, int, int, int]]) -> str:
    rotas_cidade = cria_rotas_cidade(M, N)
    coordenada_aninha = (L, C)
    rota_utilizada = []
    backtracking(rotas_cidade, coordenada_aninha, rota_utilizada, B)
    
    if len(rota_utilizada) == 0:
        return "IMPOSSIVEL"
    return rota_utilizada[0]

def backtracking(rotas_cidade: List[Tuple[int, int]], 
coordenada_aninha: Tuple[int, int],
rota_utilizada: str, B: List[Tuple[int, int, int, int]],
rotas_escolhidas = [(0,0)]) -> str:
    if validar_utlimo_movimento(rotas_escolhidas, B):
        if rotas_escolhidas[-1] == coordenada_aninha:
            rota_utilizada.append(decodifica_coordenada(rotas_escolhidas))
        else:
            possibilidades_validas = calcula_possibilidades(rotas_escolhidas, rotas_cidade)
            for pos in possibilidades_validas:
                backtracking(rotas_cidade, coordenada_aninha, rota_utilizada, B, rotas_escolhidas + [pos])

def calcula_possibilidades(rotas_escolhidas, rotas_cidade):
    lin, col = rotas_escolhidas[-1][0], rotas_escolhidas[-1][1]
    possibilidades_validas = []
    cima = (lin - 1, col)
    direita = (lin, col + 1)
    baixo = (lin + 1, col)
    esquerda = (lin, col - 1)
    pos = [cima, direita, baixo, esquerda]
    for coordenada in pos:
        if (coordenada in rotas_cidade) and (coordenada not in rotas_escolhidas):
            possibilidades_validas.append(coordenada)
    # print(rotas_escolhidas[-1], possibilidades_validas) - deu certo
    return possibilidades_validas

def decodifica_coordenada(rotas_escolhidas):
    rota_resultante = ""
    for i in range(len(rotas_escolhidas) - 1):
        rota_atual_lin, rota_atual_col = rotas_escolhidas[i][0], rotas_escolhidas[i][1]
        rota_seguinte_lin, rota_seguinte_col = rotas_escolhidas[i + 1][0], rotas_escolhidas[i + 1][1]

        ## pra baixo
        if rota_seguinte_lin > rota_atual_lin and rota_seguinte_col == rota_atual_col:
            rota_resultante += "S"
        ## pra cima
        elif rota_seguinte_lin < rota_atual_lin and rota_seguinte_col == rota_atual_col:
            rota_resultante += "N"
        ## pra direita
        elif rota_seguinte_col > rota_atual_col and rota_seguinte_lin == rota_atual_lin:
            rota_resultante += "L"
        ## pra esquerda
        else:
            rota_resultante += "O"
    return rota_resultante
    
def validar_utlimo_movimento(rotas_escolhidas, B):
    if len(rotas_escolhidas) == 1:
        return True
    return rota_esta_disponivel(rotas_escolhidas[-2], rotas_escolhidas[-1], B)

def cria_rotas_cidade(M: int, N: int) -> List[Tuple[int, int]]:
    rotas_cidade = []
    for coluna in range(N):
        for linha in range(M):
            rota = (linha, coluna)
            rotas_cidade.append(rota)
    return rotas_cidade

def rota_esta_disponivel(rota_atual: Tuple[int, int], rota_destino: Tuple[int, int], 
B: List[Tuple[int, int, int, int]]) -> bool:
    rota_esta_disponivel = True
    for index in range(len(B)):
        rota = (rota_atual[0], rota_atual[1], rota_destino[0], rota_destino[1])
        if rota == B[index]:
            rota_esta_disponivel = False
    return rota_esta_disponivel

#test = [(0, 0, 0, 1), (1, 0, 1, 1), (1, 1, 1, 2), (2, 1, 2, 2)]
#encontra_rota(3, 3, 2, 2, test)