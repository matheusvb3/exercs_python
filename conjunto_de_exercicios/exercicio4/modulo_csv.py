def ler_arquivo_csv(caminho_arquivo):
    dados = [] # Cria um array vazio para adicionar as linhas com as informações usando append()
    arquivo_csv = open(caminho_arquivo)
    for linha in arquivo_csv:
        linha_sem_espacos = linha.strip() # Retira os espaços em branco no início e no final
        if linha_sem_espacos:
            dados.append(linha_sem_espacos.split(',')) # Separa cada dado pela vírgula
    return dados
