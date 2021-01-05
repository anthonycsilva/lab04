import math
def recursiva(s):
    # Essa função recebe uma string e escreve a mesma string dentro de si.
    # String -> String
    tamanho = len(s)
    meio = math.floor(tamanho/2)
    string_inicio = s[:meio]
    string_final = s[meio:]
    return (string_inicio+ s +string_final)

print(recursiva('linguístico'))