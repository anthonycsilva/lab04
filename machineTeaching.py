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
    meio = math.floor(round(tamanho / 2))
    string_inicio = s[:meio]
    string_final = s[meio:]
    return (string_inicio, string_final)

 print(recursiva('abcd'))