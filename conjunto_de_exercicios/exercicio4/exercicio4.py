# Crie um módulo que contenha uma função para ler um arquivo CSV e retornar os dados como uma lista de listas.
# Cada linha é uma lista da lista maior. Use este módulo para ler um arquivo CSV e imprimir os dados.

from modulo_csv import ler_arquivo_csv

dados = ler_arquivo_csv("customers-100.csv")
for linha in dados:
    print(linha)
