import math
def hastag(s):
    # Essa funçao recebe uma string, a separada e a returna entre hastags
    # String -> String
    tamanho = len(s)
    meio = math.floor(tamanho/2)
    string_inicio = s[:meio]
    string_final = s[meio:]

    return '#'+string_inicio+'#'+string_final+'#'

print(hastag('abcde'))