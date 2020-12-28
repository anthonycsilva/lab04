def formato_data(data):

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


   #'-'.join(frase2)

print(formato_data('01/01/01'))