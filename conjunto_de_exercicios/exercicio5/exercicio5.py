# Crie um pacote chamado 'utils' com módulos para diferentes tarefas, como manipulação de strings, operações matemáticas, etc
# No mínimo 2 módulos e 3 funções (métodos) em cada. Use este pacote em outro script.

from utils.modulo_matematica import *
from utils.modulo_listas import *

numero = float(input("Informe um número: "))
print("O dobro do número {} é {}.".format(numero, dobro(numero)))
e_inteiro = verifica_inteiro(numero)
if e_inteiro:
    print("O número é inteiro.")
else:
    print("O número não é inteiro.")
e_primo = verifica_primo(numero)
if e_primo:
    print("O número é primo.")
else:
    print("O número não é primo.")

lista = [14, 88, 1, 65, 47, 234, 123, 44, 1332, 12, 55]
print("A lista original é:", lista)
adiciona_ao_fim(lista, numero)
print("A lista com {} adicionado ao fim é: {}".format(numero, lista))
remove_do_fim(lista)
print("A lista com o último elemento removido é:", lista)
ordena(lista)
print("A lista ordenada é:", lista);
