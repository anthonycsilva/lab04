def calculaMedia(nome,nota1,nota2,nota3):
#Essa função recebe o nome do aluno e suas 3 notas e tira sua media, retornando o nome do mesmo e dizendo se foi aprovado ou não com aquela nota
    mediaNota = (nota1+nota2+nota3)/3
    roundedMediaNota = round(mediaNota,1)

    if(mediaNota>=7):
        return nome,roundedMediaNota,'Aprovado', 'Parabens'
    elif(mediaNota<7 and mediaNota>5):
        return nome,roundedMediaNota,'Aprovado'
    else:
        return str(nome),roundedMediaNota, 'Reprovado'

#(<nome>, <media>,’aprovado’, ’Parabéns!’