import array

def initstat():
    return array.array('b', [0]*8)

def getstat(stat):
    return sum(stat)

rolls = initstat()

r = {}
def setrand(num, val):
    r[num] = val

def lcg(Xn, a, c, m, n): 
    resultados = []
    for _ in range(n):
        Xn = (a * Xn + c) % m
        resultados.append(Xn)
    return resultados
def rand():
    rand = r['z']
    index = r['a']
    b = r['b']
    d = r['d']
    f = lcg((id(rand)), (1103515244+d%9999999999), (12344+b)%9999999, 2**31, 1024)
    index = id(b)%(769) + 255
    setrand('z', (rand+b) | (d+index))
    setrand('a', (rand+b) & (d+index))
    setrand('b', (rand+b) ^ (d+index))
    setrand('d', (id(f)+id(b)) ^ (id(d)+id(index)))
    return f[index]

setrand('d', 1)
setrand('a', 42)
setrand('b', 67)
setrand('z', 1)

mira=furtividade=desvio=comunicaçao=navegaçao=abrirtravas=conserto=pilotagem=tecnica=utilitarios=saude=sorte=agilidade=percepçao=carisma=resistencia=força=intimidação=initstat()



def rolar(teste, cargo):
    match cargo:
        case 'aae':
            mira[7], furtividade[7], desvio[7] = 2, 1, 1
        case 'piloto':
            conserto[7], comunicaçao[7], navegaçao[7], pilotagem[7], tecnica[7], utilitarios[7], percepçao[7], carisma[7] = 3,3,3,3,3,3,1,1
        case 'copiloto':
            conserto[7], comunicaçao[7], navegaçao[7], pilotagem[7], tecnica[7], utilitarios[7], saude[7], sorte[7], agilidade[7] = 2, 2, 2, 2, 2, 2, 1, 1, 1
        case 'atirador':
            força[7], comunicaçao[7], intimidação[7], resistencia[7] = 2, 1, 1, 1
        case 'engenheiro':
            conserto[7], abrirtravas[7], comunicaçao[7], navegaçao[7], pilotagem[7], tecnica[7], utilitarios[7] = 3, 2, 1, 1, 1, 1, 1
    stat = getstat(teste)
    bonus = stat%5 + getstat(rolls)
    match cargo:
        case 'aae':
            mira[7], furtividade[7], desvio[7] = 0, 0, 0
        case 'piloto':
            conserto[7], comunicaçao[7], navegaçao[7], pilotagem[7], tecnica[7], utilitarios[7], percepçao[7], carisma[7] = 0,0,0,0,0,0,0,0
        case 'copiloto':
            conserto[7], comunicaçao[7], navegaçao[7], pilotagem[7], tecnica[7], utilitarios[7], saude[7], sorte[7], agilidade[7] = 0, 0, 0, 0, 0, 0, 0, 0, 0
        case 'atirador':
            força[7], comunicaçao[7], intimidação[7], resistencia[7] = 0, 0, 0, 0
        case 'engenheiro':
            conserto[7], abrirtravas[7], comunicaçao[7], navegaçao[7], pilotagem[7], tecnica[7], utilitarios[7] = 0, 0, 0, 0, 0, 0, 0
    level = min((stat//5), 5)
    dice = (6, 8, 10, 12, 20)
    result = [((rand()%dice[level])+1), ((rand()%dice[level])+1), ((rand()%dice[level])+1)]
    for idx in result:
        result[idx] += bonus

    cargos = (Conserto, Comunicações, Força, Intimidação, Medicina, Mira, Percepção, Saúde, Técnica) = [
        (+2, +2, +3), (-2, +2, +4), (+2, +1, +3),
        (+3, +3, +3), (+3, +2, +3), (+2, +0, +2), 
        (+3, +0, +2), (+2, -1, +1), (+2, -1, +1)]

    #for combos in cargos:
    #    combo1 = cargo[1][1]
    #if result>=dt and 


