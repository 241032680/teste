import array

def initstat(n):
    return array.array('b', [0]*15 + [n])

def getstat(stat):
    return sum(stat) - stat[15]

rolls = initstat(0)

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




bonus_cargo = {
    'aae': [(mira[15], 2), (furtividade[15], 1), (desvio[15], 1)],
    'piloto': [(conserto[15], 3), (comunicaçao[15], 3), (navegaçao[15], 3),
               (pilotagem[15], 3), (tecnica[15], 3), (utilitarios[15], 3),
               (percepçao[15], 1), (carisma[15], 1)],
    'copiloto': [(conserto[15], 2), (comunicaçao[15], 2), (navegaçao[15], 2),
                 (pilotagem[15], 2), (tecnica[15], 2), (utilitarios[15], 2),
                 (saude[15], 1), (sorte[15], 1), (agilidade[15], 1)],
    'atirador': [(força, 2), (comunicaçao[15], 1), (intimidação[15], 1),
                 (resistencia[15], 1)],
    'engenheiro': {conserto[15]: 3, abrirtravas[15]: 2, comunicaçao[15]: 1,
                   navegaçao[15]: 1, pilotagem[15]: 1, tecnica[15]: 1,
                   utilitarios[15]: 1}
}
#print(bonus_cargo)
dts= [(10, 12, 14), (11, 14, 18), (12, 16, 21), (13, 18, 24), (18, 26, 36)]


def rolar(teste, cargo):
    print(teste)
    if teste[15] in bonus_cargo[cargo]:
        teste[7] = bonus_cargo[cargo][teste[15]]
    stat = getstat(teste)
    print(teste)
    bonus = stat % 5 + getstat(rolls)
    print(bonus)
    level = min((stat//5), 5)
    print(level)
    dice = (6, 8, 10, 12, 20)
    print(dice[level])
    result = [((rand()%dice[level])+1), ((rand()%dice[level])+1), ((rand()%dice[level])+1)]
    print(result)
    soma = sum(result)
    print(soma)
    if soma == dice[level]*3:
        return "CRIT"
    soma += bonus
    print(soma)
    facil = dts[level][0]
    medio = dts[level][1]
    dificil = dts[level][2]
    if soma < facil:
        return "FAIL"
    if soma >= facil and soma < medio:
        return "EASY"
    if soma >= medio and soma < dificil:
        return "MEDIUM"
    if soma >= dificil:
        return "HARD"
print(rolar(comunicaçao, 'engenheiro'))

