def dobro(numero):
    return 2 * numero

def verifica_inteiro(numero):
    return numero.is_integer()

def verifica_primo(numero):
    e_primo = False
    if verifica_inteiro(numero) and numero > 1:
        numero = int(numero)
        for i in range(2, numero):
            if (numero % i) == 0:
                break
        else: # Somente será executado quando o loop terminar SEM o uso de um break.
            e_primo = True
    return e_primo
