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

def formato_data(data):
#essa função recebe uma data, e reconhece como essa data está escrita e retorna o formato da mesma
    dataSeparada = data.split('/')
    diaStr = dataSeparada[0]
    mesStr = dataSeparada[1]
    anoStr  = dataSeparada[2]

    dia = int(diaStr)
    mes = int(mesStr)
    ano = int(anoStr)

    data0 = diaStr, mesStr, anoStr
    data1 = mesStr, diaStr, anoStr
    data2 = anoStr, mesStr, diaStr
    if (dia > 31 and mes > 12):

        return 0
    elif (ano == 0):
        primeiraData = '/'.join(data0)
        segundaData = '/'.join(data1)
        return primeiraData, segundaData

    elif (dia == 0):
        return '/'.join(data2)
    else:
        primeiraData = '/'.join(data0)
        segundaData = '/'.join(data1)
        terceiraData = '/'.join(data2)
        return primeiraData, segundaData, terceiraData