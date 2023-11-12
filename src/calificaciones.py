def nota_teoria(a,b):
    if a == None:
        a = 0
    if b == None:
        b = 0
    nota = (float(a)+float(b))/2
    return nota

def nota_cuatrimestre(tupla,a):
    b = tupla[0]
    c = tupla[1]
    if nota_teoria(b,c) < 4:
        nota = 0
    else:
        if a == None:
            a = 0
        nota = nota_teoria(b,c) * 0.2 + 0.8 * float(a)
    return nota

def nota_continua(tupla1 , tupla2):
    et1_1 = tupla1[0]
    et1_2 = tupla1[1]
    ep1 = tupla2[0]
    et2_1 = tupla1[2]
    et2_2 = tupla1[3]
    ep2 = tupla2[1]
    notac1 =nota_cuatrimestre((et1_1, et1_2), ep1)
    notac2 = nota_cuatrimestre((et2_1,et2_2),ep2)
    if notac1 < 4:
        nota = notac2 / 2
    elif notac2 < 4:
        nota = notac1 / 2
    else:
        nota = (notac1 + notac2) / 2
    return nota