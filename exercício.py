def formato_data(data):

    #strings
    diaString = data[0:2]
    mesString = data[3:5]
    anoString = data[6:]

    #inteiros
    diaInt = int(diaString)
    mesInt = int(mesString)
    anoInt = int(anoString)

    if(diaInt>31 and mesInt>12):
        return 0
    elif(diaInt>31 or mesInt>12):
        return 0
    elif(anoInt == 0):
       return 'dd/mm/yy', 'mm/dd/yy'
    elif (diaInt == 0):

        return 'yy/mm/dd'
    else:
        return 'dd/mm/yy', 'mm/dd/aa', 'yy/mm/dd'


print(formato_data('01/01/01'))