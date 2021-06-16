def minimo_operacoes(D: str, K: int) -> int:
    operacoes_total = 0
    numero_max_operacoes_permitidas = 1000
    moedas_atuais = D
    operacao_impossivel = False
    index_c = moedas_atuais.find("C")
    count = 0

    while (operacoes_total <= numero_max_operacoes_permitidas and index_c > -1 and not operacao_impossivel):
        if (index_c > -1 and ((index_c + K) > len(D))):
            operacao_impossivel = True
        if (index_c > -1 and ((index_c + K) <= len(D))):
            moedas_consecutivas = moedas_atuais[index_c:(index_c + K)]
            moedas_viradas = virar_moedas(moedas_consecutivas)
            moedas_atuais = moedas_atuais.replace(moedas_consecutivas, moedas_viradas)
            count += 1
        
        index_c = moedas_atuais.find("C")    
        operacoes_total += 1

    if (operacoes_total == numero_max_operacoes_permitidas and index_c > -1) or operacao_impossivel:
        return -1

    return count

def virar_moedas(moedas: str) -> str:
    moedas_viradas = ""
    for i in range(len(moedas)):
        if moedas[i] == "C":
            moedas_viradas += "V"
        else:
            moedas_viradas += "C"
    return moedas_viradas

if __name__ == "__main__":
    help(minimo_operacoes)