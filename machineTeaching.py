import math

def concatenacao(a,b):

    return a+b+b+a


def substitui(s,x,i):
    listaString = list(s)
    listaString[i] = 'K'
    listaString = ''.join(listaString)
    return listaString



def recursiva(s):
    # Essa função recebe uma string e escreve a mesma string dentro de si.
    # String -> String
    tamanho = len(s)
    meio = round(tamanho/2)

    stringInicio = s[:meio]
    stringFinal = s[meio:]
    inserirString = stringInicio + s + stringFinal
    return inserirString
