# Exercício 1: Crie um arquivo de texto aleatório contendo o texto do Lorem Ipsum, abra o arquivo em Python no modo
# leitura, leia o conteúdo e conte o número total de palavras, imprima o resultado na tela e escreva o valor do número
# de palavras em um outro arquivo.

texto_lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum."""

print(texto_lorem)
arq_texto_escrita = open("arquivo.txt", "w")
arq_texto_escrita.write(texto_lorem) # Salva o texto lorem ipsum em arquivo.txt
arq_texto_escrita.close()

arq_texto_leitura = open("arquivo.txt", "r")

contador_palavras = 0
for linha in arq_texto_leitura: # Percorre o arquivo linha por linha
    palavras = linha.split() # Obtém uma lista contendo cada palavra da linha atual
    contador_palavras += len(palavras)

print("Número de palavras: {}".format(contador_palavras))
arq_texto_leitura.close()

arq_texto_cont_palavras = open("cont_palavras.txt", "w")
arq_texto_cont_palavras.write(str(contador_palavras))
arq_texto_cont_palavras.close()
