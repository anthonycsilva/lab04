def calculaMedia(aluno):
#essa função rebece uma tupla com o nome e tres notas e retorna se o aluno em questão foi reprovado ou não e sua média
    nome = aluno[0]
    n1 = int(aluno[1])
    n2 = int(aluno[2])
    n3 = int(aluno[3])

    mediaNota = (n1 + n2 + n3) / 3
    roundedMediaNota = round(mediaNota, 1)

    if (mediaNota >= 7):
        return nome, roundedMediaNota, 'Aprovado', 'Parabens'
    elif (mediaNota < 7 and mediaNota > 5):
        return nome, roundedMediaNota, 'Aprovado'
    else:
        return str(nome), roundedMediaNota, 'Reprovado'

    if(mediaNota>=7):
        return nome,roundedMediaNota,'Aprovado', 'Parabens'
    elif(mediaNota<7 and mediaNota>5):
        return nome,roundedMediaNota,'Aprovado'
    else:
        return str(nome),roundedMediaNota, 'Reprovado'

