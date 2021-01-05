def diff_datas(data1, data2):
    # calcula a diferença entre duas datas
    #Strings Dia1
    diaString1 = data1[0:2]
    mesString1 = data1[3:5]
    anoString1 = data1[6:10]

    #Strings Dia2
    diaString2 = data2[:2]
    mesString2 = data2[3:5]
    anoString2 = data2[6:]

    #Inteiros Dia1
    diaInt1 = int(diaString1)
    mesInt1 = int(mesString1)
    anoInt1 = int(anoString1)

    #Inteiros Dia2
    diaInt2 = int(diaString2)
    mesInt2 = int(mesString2)
    anoInt2 = int(anoString2)

    total_dias1 = anoInt1*365+(mesInt1*30)+diaInt1
    total_dias2 =  anoInt2*365+mesInt2*30+diaInt2

    total_dias = total_dias1 - total_dias2
    if(total_dias < 0):
        total_dias = total_dias *-1
        return total_dias
    return total_dias

print(diff_datas('10/03/1992','14/06/2013'))