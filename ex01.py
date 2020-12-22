def calculaMedia(nome,nota1,nota2,nota3):

    mediaNota = (nota1+nota2+nota3)/3

    if(mediaNota>=7):
        return str(nome) + str(' ') + str(round(mediaNota, 1)) + str(' ') + str('aprovado')+ str(' ') + str('parabens')
    else:
        return str(nome) + str(' ') + str(round(mediaNota, 1)) + str(' ') + str('Reprovado')
print(calculaMedia('Anthony',7,8.7, 8.7))

#(<nome>, <media>,’aprovado’, ’Parabéns!’