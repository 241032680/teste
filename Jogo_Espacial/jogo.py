import time
import array

#categorias de stats
mob = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50] #mobilidade
ger = [51, 52, 53, 54, 55, 56] #geral
nav = [22, 23, 24, 25, 26, 27] #navegação
com = [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39] #comunicação

def getstat(stat):
    if stat[15] in mob:
        return int(sum(stat) - stat[15] + sum(mobilidade) - mobilidade[15] + sum(rolls))
    elif stat[15] in ger:
        return int(sum(stat) - stat[15] + sum(geral) - geral[15] + sum(rolls))
    elif stat[15] in com:
        return int(sum(stat) - stat[15] + sum(combate) - combate[15] + sum(rolls))
    elif stat[15] in nav:
        return int(sum(stat) - stat[15] + sum(nave) - nave[15] + sum(rolls))
    else:
        return int(sum(stat) - stat[15])

def initstat(n):
    return array.array('b', [0]*15 + [n]) #o ultimo valor do array é o identificador

def timer(frames):
    while frames:
        secs, totframes = divmod(frames, 50)
        timer = str(f'{secs, totframes}')
        time.sleep((1/50))
        frames -= 1

#arrendondar pra cima
#ceil (5, 2)
#print (ceil (5, 2))
#dividir por 1 se só quiser arrendondar sem operação
def ceil(a, b):
    return int(-(-a // b))

#randomização
#Xn+1 = (aXn + c) mod mod (segundo a wikipedia)
#foi de uma monstruosidade de 70 linhas pra uma beleza de 12 quando descobri o mundo magico do id()
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

#função seno
pi = 3.141592653589793
def sin(x): #formula roubada da wikipedia, adaptada
    x = (x + pi)%(2*pi) - pi
    if x > pi/2: x = pi - x
    elif x < -pi/2: x = -pi - x
    y = x**2
    return x*(1 - y/6*(1 - y/20*(1 - y/42*(1 - y/72))))

#média:
def avg(list):
  l = list.copy()
  average = ((sum(l) / float(len(l))))
  return (int(average * 100))/100 #2 casas decimais

#stats
#começando a separar por causa do display/GUI, talvez desnecessário com método...
f = {}
#só sobrou o f agora

def setfoo(foo, valor): #seta as flags do jogo
    f[foo] = valor

#stats nave
numtorpedos= initstat(1)
numaae= initstat(2)
numfrontal=  initstat(3)
hp = initstat(4)
escudo= initstat(5)
velmax= initstat(6)
escudot= initstat(7)
escudof=  initstat(8)
direct= initstat(9)
overclock= initstat(10)
modoativo = initstat(11)
grav = initstat(12)
sonar = initstat(13) 
radio = initstat(14)
crio = initstat(15)
danotorp = initstat(16)
danoaae = initstat(17)
danofront = initstat(18)
criodesmaio = initstat(19)
depressurização = initstat(20)
riscomotor = initstat(21)
numtorpedos[0],numaae[0],numfrontal[0],hp[0],velmax[0],direct[0],modoativo[0],grav[0],sonar[0],radio[0],crio[0],danotorp[0],danoaae[0],danofront[0],criodesmaio[0],depressurização[0],riscomotor[0] = 5,8,6,20,7,1,1,1,1,1,1,1,1,1,5,3,8

#stats
rolls = initstat(0)
pilotagem = initstat(22)
utilitarios = initstat(23)
comunicaçao = initstat(24)
conserto = initstat(25)
navegaçao = initstat(26)
tecnica = initstat(27)
pilotagem[0],utilitarios[0],comunicaçao[0],conserto[0],navegaçao[0],tecnica[0]= 1,1,1,1,1,1
cover = initstat(28)
curtoalc= initstat(29)
medioalc= initstat(30)
longoalc= initstat(31)
armasenergia= initstat(32)
armasprojetil= initstat(33)
bastoes= initstat(34)
corpoacorpo= initstat(35)
laminas= initstat(36)
mira= initstat(37)
percepçao= initstat(38)
resistencia = initstat(39)
curtoalc[0],medioalc[0],longoalc[0],armasenergia[0],armasprojetil[0],bastoes[0],corpoacorpo[0],laminas[0],mira[0],percepçao[0],resistencia[0] = 1,1,1,1,1,1,1,1,1,1,1
rolls[0],cover[0],mira[0],percepçao[0] = 0,1,1,1
agilidade = initstat(40)
corridacurta = initstat(41)
corridalonga = initstat(42)
desvio = initstat(43)
escalar = initstat(44)
equilibrio = initstat(45)
furtividade = initstat(46)
nataçao = initstat(47)
nocaute = initstat(48)
salto = initstat(49)
temperaturasextremas = initstat(50)
agilidade[0],corridacurta[0],corridalonga[0],desvio[0],escalar[0],equilibrio[0],furtividade[0],nataçao[0],nocaute[0],salto[0],temperaturasextremas[0] = 1,1,1,1,1,1,1,1,1,1,1
carisma = initstat(51)
sorte = initstat(52)
saude = initstat(53)
força = initstat(54)
intimidação = initstat(55)
abrirtravas = initstat(56)
mobilidade = initstat(57)
combate = initstat(58)
nave = initstat(59)
geral = initstat(60)

#buffs/debuffs modo: stat[1]
#buffs/debuffs crio: stat[2]
#buffs/debuffs sonar: stat[3]
#buffs/debuffs radio: stat[4]
#buffs/debuffs grav: stat[5]
#buffs/debuffs danonave: stat[6]
#stats/debuffs players: stat [7]
#buffs cargo: stat[8]

#randomizador
setrand('d', 1)
setrand('a', 42)
setrand('b', 67)
setrand('z', 1)

#controles de jogo/placeholders/modificadores
setfoo('turnos', 1)
setfoo('rods', 1)
setfoo('gameon', True)
setfoo('gamewin', 0)
setfoo('foo', 1)
setfoo('modoanterior', 0)
setfoo('pesadoprop', 0)
setfoo('numasas', 0) #numero de asas DANIFICADAS, numero de asas na nave é 4
setfoo('numprops', 0) #mesma coisa das asas mas pra propulsores
setfoo('pesadoasa', 0)
setfoo('medioasa', 0)
setfoo('quarto1dano', False)
setfoo('quarto2dano', False)
setfoo('quarto3dano', False)
setfoo('quarto4dano', False)
setfoo('quarto5dano', False)
setfoo('podeusartorpedo', True)
setfoo('podeusarcomms', True)
setfoo('motorfrito', False)
setfoo('motorquente', False)
setfoo('hangarselado', False)

#tipos de dano
setfoo('tipoaae', 1)
setfoo('tipotorp', 1)

f.update({
    'danocrio': False, 'danograv': False, 'danohangar': False,
    'danoasa': False, 'danoquartos': False, 'danopropulsores': False,
    'danoarmazém': False, 'danomedbay': False, 'danocozinha': False, 'danosalacomum': False,
    'danocomms': False, 'genescudo': True, 'hitcrio': 0,
    'rodssemgrav': 0, 'rodsfalhamotor': 0, 'falhamotor': False,
    'numquartos': 0, 'riscoverclock': 0, 'hangarselado': False,
    'podeusartorpedo': True, 'podeusarcomms': True,
    'tipoaae': 1, 'tipotorp': 1, 'direçãoinimigo': None,
    'escudoefetivof': 0, 'escudoefetivot': 0, 'criodesmaio': 5,
})


MODOS = {
    1: (10, 0, 0, 0, 0, 0, 0),
    2: (15, -2, -8, -5, -6, -1, -1),
    3: (9, 3, -5, -5, -4, 2, -1),
    4: (7, -1, 6, 1, 4, 0, -1),
    5: (8, -1, -3, 5, -2, 1, 2),
}

def atualizar_stats():
    def distribuir_escudos(total, direcao):
        if direcao == 2:
            return int(total * 1.5), ceil(total, 2)
        if direcao == 3:
            return ceil(total, 2), int(total * 1.5)
        return total, total

    #modo de energia
    (escudo[1], velmax[1], danoaae[1], danotorp[1],
     danofront[1], pilotagem[1], utilitarios[1]) = MODOS[modoativo[0]]

    #equipamentos
    crioativo = crio[0] and not f['hitcrio']
    sonarativo = sonar[0]
    radioativo = radio[0] and not f['danocomms']
    gravativa = grav[0] and not f['danograv']

    rolls[2],velmax[2],danoaae[2],danofront[2] = (0,0,0,0) if crioativo else (-1,3,4,4)
    mira[3],percepçao[3],danoaae[3],danofront[3],velmax[3] = (0,0,0,0,0) if sonarativo else (-2,-1,3,1,1)
    velmax[4] = 0 if radioativo else 1
    (mobilidade[5],cover[5],mira[5],escudo[5],danoaae[5],danofront[5]) = (0,0,0,0,0,0) if gravativa else (-2,-1,-1,2,1,1)

    #danos
    f['danocrio'] = f['hitcrio'] > 0
    f['danopropulsores'] = f['numprops'] > 0
    f['danoasa'] = f['numasas'] > 0
    f['danoquartos'] = any(f[estado] for estado in (
        'danosalacomum','quarto1dano','quarto2dano','quarto3dano',
        'quarto4dano','quarto5dano'))

    f['numquartos'] = sum(int(f[estado]) for estado in (
        'danosalacomum','quarto1dano','quarto2dano','quarto3dano',
        'quarto4dano','quarto5dano'))
    rolls[6] = -f['hitcrio']
    mobilidade[6] = -2 * f['rodssemgrav']
    cover[6] = -f['rodssemgrav']
    pilotagem[6] = -(f['numasas'] + f['medioasa'] + f['pesadoasa'])
    prop = f['numprops'] + f['pesadoprop']
    motor = f['rodsfalhamotor'] if f['falhamotor'] else 0
    velmax[6] = -min(prop + motor, max(0, sum(velmax[:6])))

    #capacidades e permissões
    total = sum(escudo[:15]) + 5 * overclock[0]
    escudof[0],escudot[0] = distribuir_escudos(total, direct[0])
    f['escudoefetivof'] = min(max(0, f['escudoefetivof']), escudof[0])
    f['escudoefetivot'] = min(max(0, f['escudoefetivot']), escudot[0])
    f['podeusartorpedo'] = bool(sonarativo)
    f['podeusarcomms'] = bool(radioativo)
    f['hangarselado'] = f['danohangar'] and depressurização[0] == 0

def setmodo(modo):
    modoativo[0] = modo if modo in MODOS else 1
    atualizar_stats()

def setdirect(direcao):
    if direcao not in (1, 2, 3):
        return False
    direct[0] = direcao
    atualizar_stats()
    return True

def flip():
    if not f['genescudo']:
        return False
    overclock[0] = int(not overclock[0])
    if not overclock[0]:
        f['riscoverclock'] = 0
    atualizar_stats()
    return True

atualizar_stats()
f['escudoefetivof'],f['escudoefetivot'] = escudof[0],escudot[0]

#inventários

#armazém (18 slots)
#gera 18 itens de valor aleatório, que definem o valor da recomepensa no final do jogo
#quanto mais itens chegarem no checkpoint final, melhor o score
#varias mecanicas fazem os itens perderem valor

armazém = {}
cozinha = {}
medbay = {}
salacomum = {}
quarto1 = {}
quarto2 = {}
quarto3 = {}
quarto4 = {}
quarto5 = {}

#centraliza as capacidades dos inventários
capacidade_inventarios = (
    (armazém, 18), (cozinha, 12),
    (medbay, 12), (salacomum, 6),
    (quarto1, 4), (quarto2, 4), (quarto3, 4), (quarto4, 4), (quarto5, 4),
) 

#centraliza os estados dos quartos
quartos = {
    'salacomum': (0, 'salacomum', salacomum),
    'quarto1': (1, 'quarto1dano', quarto1),
    'quarto2': (2, 'quarto2dano', quarto2),
    'quarto3': (3, 'quarto3dano', quarto3),
    'quarto4': (4, 'quarto4dano', quarto4),
    'quarto5': (5, 'quarto5dano', quarto5),
}
def additem(local, nome, valor):
    local[nome.upper()] = valor

#rodada: cada jogador e inimmigo tem seu turno
#turno de cada jogador: 3 ações
#turno de cada inimigo: instantâneo
#ordem de turnos: piloto, copiloto, engenheiro, atirador, atirador aaebase, ajuste de distância, inimigos

def hitnave(intensidade, direcao=None): #acertos de inimigos
    intensidade = intensidade.lower()
    if intensidade == 'r':
        intensidade = ('l','m','p')[rand() % 3]
    danos_base = {'l': 5, 'm': 8, 'p': 12}
    if intensidade not in danos_base:
        raise ValueError('Intensidade inválida')
    dano = danos_base[intensidade]
    direcao = direcao if direcao is not None else f['direçãoinimigo']
    chave_escudo = {'Frente': 'escudoefetivof', 'Atras': 'escudoefetivot', 'Atrás': 'escudoefetivot'}.get(direcao)
    if chave_escudo and f[chave_escudo] > 0:
        f[chave_escudo] = max(0, f[chave_escudo] - dano)
        return f'Escudo {direcao.lower()} absorveu {dano} de dano'

    hp[0] -= dano
    local = 'Casco'

    #avarias leves
    if intensidade == 'l':
        match rand() % 12:
            case 0:
                f['hitcrio'] += 1
                local = 'Criogênicos'
            case 1:
                f['danograv'] = True
                local = 'Gerador de Gravidade'
            case 2:
                f['genescudo'] = False
                overclock[0] = 0
                f['riscoverclock'] = 0
                local = 'Gerador de Escudos'
            case 3:
                f['danomedbay'] = True
                local = 'Medbay'
            case 4:
                f['danocozinha'] = True
                local = 'Cozinha'
            case 6:
                quarto = ('salacomum','quarto1','quarto2','quarto3','quarto4','quarto5')[rand() % 6]
                f['salacomum' if quarto == 'salacomum' else quarto + 'dano'] = True
                local = quarto
            case 7:
                f['danocomms'] = True
                local = 'Comunicações'
            case 8:
                f['danoarmazém'] = True
                local = 'Armazém'
            case 9:
                f['danohangar'] = True
                depressurização[0] = min(depressurização[0], 3)
                local = 'Microhangar'
            case 10:
                f['numprops'] = min(f['numprops'] + 1, 9)
                local = 'Propulsores'
            case 11:
                f['numasas'] = min(f['numasas'] + 1, 4)
                local = 'Asa'

    #avarias médias e pesadas já descritas no código
    elif intensidade == 'm':
        if rand() % 10 == 9 and f['numasas'] < 4:
            f['numasas'] += 1
            f['medioasa'] += 1
            local = 'Asa'
    elif intensidade == 'p':
        if rand() % 10 == 6 and f['numprops'] < 9:
            f['numprops'] += 1
            f['pesadoprop'] += 1
            local = 'Propulsores'

    atualizar_stats()
    return f'{local} levou um tiro de {dano} de dano'

#ações players
def consertar(lugar):
    if lugar == 'prop' and f['numprops']:
        f['numprops'] -= 1
        if f['pesadoprop']:
            f['pesadoprop'] -= 1
    elif lugar == 'asa' and f['numasas']:
        f['numasas'] -= 1
        if f['pesadoasa']:
            f['pesadoasa'] -= 1
        elif f['medioasa']:
            f['medioasa'] -= 1
    elif lugar == 'grav' and f['danograv']:
        f['danograv'] = False
        f['rodssemgrav'] = 0
    elif lugar == 'crio' and f['hitcrio']:
        f['hitcrio'] -= 1
    elif lugar == 'geradorescudo':
        f['genescudo'] = True
        f['riscoverclock'] = 0
        f['escudoefetivof'] = escudof[0]
        f['escudoefetivot'] = escudot[0]
    elif lugar == 'comms' and f['danocomms']:
        f['danocomms'] = False
    elif lugar == 'motor' and f['falhamotor']:
        f['falhamotor'] = False
        f['rodsfalhamotor'] = 0
    elif lugar == 'hangar' and f['danohangar']:
        f['danohangar'] = False
        depressurização[0] = 3
    elif lugar in ('armazém','medbay','cozinha'):
        f['dano' + lugar] = False
    elif lugar in quartos:
        _, estado, _ = quartos[lugar]
        f[estado] = False
    else:
        return False

    atualizar_stats()
    return True

#end of round

def inventorycheck(): #corrigido: remove itens aleatórios ao exceder a capacidade
    for inventario, capacidade in capacidade_inventarios:
        while len(inventario) > capacidade:
            inventario.pop(tuple(inventario)[rand() % len(inventario)]) #corrigido: remove por uma chave existente

def danos():
    mensagens = []

    if f['danograv']:
        f['rodssemgrav'] += 1

    if f['hitcrio'] or not crio[0]:
        f['criodesmaio'] = max(0, f['criodesmaio'] - 1)
        if f['criodesmaio'] == 0:
            mensagens.append('Tripulação desmaiou por falha na criogenia')
    else:
        f['criodesmaio'] = min(5, f['criodesmaio'] + 1)

    if f['falhamotor']:
        f['rodsfalhamotor'] += 1

    if f['danopropulsores']:
        if f['novoprop'] == 1 and f['numprops'] < 9:
            setfoo('numprops', min(f['numprops'] + 1, 9)) #corrigido: respeita a capacidade máxima
            print('Um novo propulsor foi danificado!')
            setfoo('novoprop', 0)
        print("Propulsores danificados!")

    depressurizacao_restante = depressurização[0]
    if f['danohangar']:
        depressurização[0] = max(0, depressurização[0] - 1)
        if depressurização[0] == 0:
            mensagens.append('Microhangar despressurizado')

    for estado, inventario in (
        ('danoarmazém', armazém), ('danomedbay', medbay), ('danocozinha', cozinha),
    ):
        if f[estado] and inventario:
            inventario.pop(tuple(inventario)[rand() % len(inventario)])

    for indice, estado, inventario in quartos.values():
        if f[estado] and inventario:
            inventario.pop(tuple(inventario)[rand() % len(inventario)])
    return mensagens

def genescudo():
    if f['genescudo']:
        if f['escudoefetivof'] > 0:
            f['escudoefetivof'] = escudof[0]
        if f['escudoefetivot'] > 0:
            f['escudoefetivot'] = escudot[0]

def atualizaroverclock():
    if not overclock[0] or not f['genescudo']:
        return False
    f['riscoverclock'] += 1
    if rand() % 4 < min(f['riscoverclock'], 4):
        f['genescudo'] = False
        overclock[0] = 0
        f['riscoverclock'] = 0
        return True
    return False

def eor():
    mensagens = danos()
    if atualizaroverclock():
        mensagens.append('Overclock fritou o gerador de escudos')
    inventorycheck()
    atualizar_stats()
    genescudo()
    return mensagens

#inimigo

def criarinimigo(tipo):
    if tipo == "medio":
        qtmissel = 3
        qthp = 40
        qtesc = 5
        v = 4.56
        s = 5
    elif tipo == "pesado":
        qtmissel = 4
        qtesc = 10
        qthp = 80
        v = 6.66
        s = 4
    else:
        qtmissel = 2
        v = 1.5
        qthp = 0
        qtmissel = 3
        qtesc = 0
        s = 6
    if len(inimigos) > 10:
        return 0
    n = len(inimigos)
    inimigos[f'i{(n+1)}'] = {
    "tipo" : tipo,
    "hp" : int(30 + qthp + float(((sin(rand())) * 6.66))),
    "velocidade": int(s),
    "mísseis" : int(rand()%qtmissel + sin(rand())),
    "escudo": int((10 + qtesc + (sin(rand()) * v)) * ((sin(rand()) + 1.5)//2.2))
    }

i1 = {
    "tipo de inimigo": "leve",
    "hp" : int((30 + (sin(rand())) * 6.66)),
    "velocidade": 6,
    "mísseis" : int(rand()%3 + sin(rand())),
    "escudo": int((10 + (sin(rand()) * 1.5)) * ((sin(rand()) + 1.5)//2.2)),
    #"tipo de missel": tipomissel(),
    #"tipo de escudo": tipoescudo(),
    #"tipo de dano": tipodano(),
  }

i2 = {"tipo" : "medio", 
"hp" : int(30 + 40 + float(((sin(rand())) * 6.66))),
"escudo": int((10 + 5 + (sin(rand()) * 4.56)) * ((sin(rand()) + 1.5)//2.2))}

i3 = {"tipo" : "pesado",
"hp" : int(30 + 80 + float(((sin(rand())) * 6.66))),
"escudo": int((10 + 10 + (sin(rand()) * 6.66)) * ((sin(rand()) + 1.5)//2.2))}

inimigos = {"i1" : i1,
"i2" : i2,
"i3" : i3} 

for x in range(1, 19):
    additem(armazém, str(x), rand()%90)
#print(armazém)
#print(len(armazém)) 

setfoo('turnosatuais', 0)

#print(inimigos["i1"])

#testes de DT
bonus_cargo = {
    'aae': {mira[15]: 2, furtividade[15]: 1, desvio[15]: 1},
    'piloto': {conserto[15]: 3, comunicaçao[15]: 3, navegaçao[15]: 3,
               pilotagem[15]: 3, tecnica[15]: 3, utilitarios[15]: 3,
               percepçao[15]: 1, carisma[15]: 1},
    'copiloto': {conserto[15]: 2, comunicaçao[15]: 2, navegaçao[15]: 2,
                 pilotagem[15]: 2, tecnica[15]: 2, utilitarios[15]: 2,
                 saude[15]: 1, sorte[15]: 1, agilidade[15]: 1},
    'atirador': {força[15]: 2, comunicaçao[15]: 1, intimidação[15]: 1,
                 resistencia[15]: 1},
    'engenheiro': {conserto[15]: 3, abrirtravas[15]: 2, comunicaçao[15]: 1,
                   navegaçao[15]: 1, pilotagem[15]: 1, tecnica[15]: 1,
                   utilitarios[15]: 1}
}
dts = [(10,12,14), (11,14,18), (12,16,21), (13,18,24), (18,26,36)]

def rolar(teste, cargo):
    base = teste[0]
    if teste[15] in mob:
        base += mobilidade[0]
    elif teste[15] in ger:
        base += geral[0]
    elif teste[15] in com:
        base += combate[0]
    elif teste[15] in nav:
        base += nave[0]

    level = min(max(base // 5, 0), 4)
    dice = (6,8,10,12,20)[level]
    dados = [rand() % dice + 1 for _ in range(3)]
    if sum(dados) == dice * 3:
        return 'CRIT'
    bonus_cargo_atual = bonus_cargo.get(cargo, {}).get(teste[15], 0)
    bonus_extra = bonus_cargo_atual - teste[8]
    total = sum(dados) + base % 5 + getstat(teste) - base + bonus_extra
    facil, medio, dificil = dts[level]
    if total < facil:
        return 'FAIL'
    if total < medio:
        return 'EASY'
    if total < dificil:
        return 'MEDIUM'
    return 'HARD'
#print(rolar(comunicaçao, 'engenheiro'))

map = ["X"] + ["0"]*20

def avançar_nave():
    x = map.index("X")
    map[x] = 0
    map[x+1] = " X "


import curses
from dataclasses import dataclass, field
from typing import Callable, List, Optional

#sentinels
EXIT = object()   # propagates up → quit
BACK = object()   # close this level, return to parent

#data model
@dataclass
class opt:
    label:   str
    submenu: List["opt"]   = field(default_factory=list)
    action:  Optional[Callable] = None   # (stdscr) → EXIT | BACK | None

#micro action
def exit_action(_): return EXIT
def back_action(_): 
    if f['turnosatuais'] == 3: 
        return BACK 

def status_nave():
    return ["STATUS DA NAVE",
        f"Casco: {hp[0]}",
        f"Escudo frontal: {f['escudoefetivof']}/{escudof[0]}",
        f"Escudo traseiro: {f['escudoefetivot']}/{escudot[0]}",
        f"Velocidade máxima: {max(0, sum(velmax[:15]))}",
        f"Modo de energia: {modoativo[0]}",
        f"Overclock: {'Ligado' if overclock[0] else 'Desligado'}",
        f"Criogenia: {'Ligada' if crio[0] and not f['danocrio'] else 'Desligada'}",
        f"Sonar: {'Ligado' if sonar[0] else 'Desligado'}",
        f"Rádio: {'Ligado' if radio[0] and not f['danocomms'] else 'Desligado'}",
        f"Gravidade: {'Ligada' if grav[0] and not f['danograv'] else 'Desligada'}"]

def mostrar_status(stdscr, items):
    largura = max(len(text) for text in items) + 2
    y, x = stdscr.getmaxyx()
    x = 1
    stdscr.addstr(1, x, "┌" + "─" * largura + "┐")

    for i, text in enumerate(items):
        stdscr.addstr(2 + i, x, "│ " + text.ljust(largura - 2) + " │")
    stdscr.addstr(2 + len(items), x, "└" + "─" * largura + "┘")
    stdscr.refresh()

criarinimigo("leve")
criarinimigo("pesado")
criarinimigo("medio")
criarinimigo("pesado")


def mostrar_inimigos(stdscr, items):
    duas_colunas = bool(len(items)>6)
    largura = max(len(key) for inimigo in items.values() for key in inimigo) + 2
    y, x = stdscr.getmaxyx()
    w = x +4 - largura*2
    j,k = 1,1
    colunaum, colunadois = inimigos.copy(), inimigos.copy()
    while len(colunaum) > 6:
        colunaum.popitem()
    for I in range(1, 7):
        try:
            colunadois.pop(f"i{I}")
        except:
            pass
    stdscr.addstr(j, w - (largura*duas_colunas*2), "┌" + "─" * (largura+((largura)//2)+2) + "┐")
    stdscr.addstr(j+1, w - (largura*duas_colunas*2), "│ ".ljust((largura-2)//2) + "INIMIGOS".center(largura-2) + " │".rjust((largura-2)//2))
    if duas_colunas:
        stdscr.addstr(j, w-2, "┌" + "─" * (largura+((largura)//2)+2) + "┐")
        stdscr.addstr(j+1, w-2, "│ ".ljust((largura-2)//2) + "INIMIGOS".center((largura-2)) + " │".rjust((largura-2)//2))

    for nome, inimigo in colunaum.items():
        stdscr.addstr(2 + j, w - (largura*duas_colunas*2), f"| --- {nome} {"-" * ((largura + 2))}|")
        j += 1
        for key, value in inimigo.items():
            if j < 33:
                stdscr.addstr(2 + j, w - (largura*duas_colunas*2), f"| {key.ljust(largura-2)} : {str(value).rjust((largura-2)//2)} |")
                j += 1
    for nome, Inimigo in colunadois.items():
        stdscr.addstr(2 + k, w-2, f"| --- {nome} {"-" * ((largura + 2))}|")
        k += 1
        for key, value in Inimigo.items():
            stdscr.addstr(2 + k, w-2, f"| {key.ljust(largura-2)} : {str(value).rjust((largura-2)//2)} |")
            k +=1

    stdscr.addstr(j+2, w - (largura*duas_colunas*2), "└" + "─" * (largura+((largura)//2)+2) + "┘")
    if duas_colunas: 
        stdscr.addstr(k+2, w-2, "└" + "─" * (largura+((largura)//2)+2) + "┘")

menu_inputs = ["Q: Ver Tripulação", "SETAS: Mover", "ESC: Voltar"]

def mostrar_inputs(stdscr, items):
    y, x = stdscr.getmaxyx()
    largura = max(len(text) for text in items) + 2
    for i, text in enumerate(menu_inputs):
        stdscr.addstr((y//3)+i+2, 1, text)
    stdscr.addstr(y//2, 1, f'y: {y} x: {x}')
    stdscr.refresh()

def mostrar_mapa(stdscr, items):
    y, x = stdscr.getmaxyx()
    largura = len(items)
    for i, text in enumerate(items):
        stdscr.addstr(1, x//2-(2*largura)+(2*i), "-" + str(text) + "-")

def draw_extras(stdscr):
    mostrar_status(stdscr, status_nave())
    mostrar_inimigos(stdscr, inimigos)
    mostrar_inputs(stdscr, menu_inputs)
    mostrar_mapa(stdscr, map)

def draw_menu_horizontal(stdscr, items, selected, draw_extras=None):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    draw_extras(stdscr)
    if draw_extras:
        draw_extras(stdscr)
    gap = 2
    espaçamento = 1
    button_widths = [len(item.label) + (espaçamento * 2) for item in items]
    x = 1
    y = h - 4
    for idx, item in enumerate(items):
        bw   = button_widths[idx]
        text = item.label.center(bw - 2)
        stdscr.addstr(y + 1, x, "┌" + "─" * (bw - 2) + "┐")
        if idx == selected:
            stdscr.attron(curses.color_pair(1))
        stdscr.addstr(y + 2, x, "│" + text + "│")
        if idx == selected:
            stdscr.attroff(curses.color_pair(1))
        stdscr.addstr(y + 3, x, "└" + "─" * (bw - 2) + "┘")
        x += bw + gap
    stdscr.refresh()

def draw_menu_vertical(stdscr, items, selected, draw_extras=None):
    stdscr.erase()
    h, w = stdscr.getmaxyx()
    if draw_extras:
        draw_extras(stdscr)
    for idx, item in enumerate(items):
        label = ("▶ " if item.submenu else "  ") + item.label
        x = w // 2 - len(label) // 2
        y = h // 2 - len(items) // 2 + idx
        if idx == selected:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, label)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, label)

    stdscr.refresh()

def run_menu(stdscr, items, layout="vertical", draw_extras=draw_extras):
    """
    layout="horizontal" → LEFT/RIGHT keys, box-buttons at the bottom.
    layout="vertical"   → UP/DOWN keys, centered list (default for submenus).
    Submenus always open as vertical regardless of their parent's layout.
    draw_extras(stdscr) is painted before menu items on every redraw,
    so you can overlay text boxes, live game values, banners, etc.
    """
    current  = 0
    draw     = draw_menu_horizontal if layout == "horizontal" else draw_menu_vertical
    key_prev = curses.KEY_LEFT  if layout == "horizontal" else curses.KEY_UP
    key_next = curses.KEY_RIGHT if layout == "horizontal" else curses.KEY_DOWN
    draw(stdscr, items, current, draw_extras)
    while True:
        key = stdscr.getch()
        if key == key_prev and current > 0:
            current -= 1
        elif key == key_next and current < len(items) - 1:
            current += 1
        elif key in (curses.KEY_ENTER, 10, 13):
            item = items[current]
            if item.submenu:
                stdscr.clear()
                result = run_menu(stdscr, item.submenu, draw_extras=draw_extras)
                if result is EXIT:
                    return EXIT
                # BACK from child → fall through, redraw this level
            elif item.action:
                result = item.action(stdscr)
                if result == EXIT:
                    stdscr.clear()
                    return EXIT
                if result == BACK:
                    stdscr.clear()
                    return BACK
                # None → stay, redraw this level
        elif key == 27:   # Escape → go up one level
            return BACK
        draw(stdscr, items, current, draw_extras)

#game actions
def confirmar_acoes(stdscr):
    if f['turnosatuais'] < 3:
        turnos = f'Você ainda tem {f['turnosatuais']} ações!'
        stdscr.addstr((h // 2) - 2, w // 2 - len(turnos) // 2, turnos)
    h, w = stdscr.getmaxyx()
    #stdscr.clear()
    msg = "Ações Confirmadas"
    stdscr.addstr(h // 2, w // 2 - len(msg) // 2, msg)
    stdscr.refresh()
    timer(25)

def escape_seq():
    setfoo('gameon', 0)
    setfoo('gamewin', 1)

def force_confirm():
    setfoo('turnosatuais', 3)

def ajustar_util(alvo):
    equipamentos = {'crio': crio, 'sonar': sonar, 'radio': radio, 'grav': grav}
    if alvo not in equipamentos:
        return False
    equipamento = equipamentos[alvo]
    equipamento[0] = int(not equipamento[0])
    atualizar_stats()
    return True

# ── Menu tree (only edit this to add new menus/submenus) ──────────────────────
MENU = [opt("Piloto", submenu=[
        opt("Acelerar"),
        opt("Trocar de Marcha"),
        opt("Manobrar"),
        opt("Navegar"),
        opt("Usar Utilitários"),
        opt("Ajudar Engenheiro"),
        opt("Atirar em Inimigos"),
        opt("Confirmar Ações",        action=confirmar_acoes, submenu=[
            opt("Sim", action = force_confirm),
            opt("Não", action = lambda s: BACK),]),
        opt("Voltar", action = lambda s: BACK),
        ]),

    opt("Copiloto", submenu=[
        opt("Acelerar"),
        opt("Trocar de Marcha"),
        opt("Manobrar"),
        opt("Navegar"),
        opt("Usar Utilitários"),
        opt("Ajudar Engenheiro"),
        opt("Atirar em Inimigos"),
        opt("Confirmar Ações",        action=confirmar_acoes, submenu=[
            opt("Sim", action = force_confirm),
            opt("Não", action = lambda s: BACK),]),
        opt("Voltar", action = lambda s: BACK)]),

    opt("Engenheiro", submenu=[
        opt("Consertar",   action=lambda s: None),
        opt("Abrir Painel de Utilitários", submenu=[
            opt("Ajustar Gravidade", action=lambda s: ajustar_util("grav")),
            opt("Ajustar Sonar", action=lambda s: ajustar_util("sonar")),
            opt("Ajustar Rádio", action=lambda s: ajustar_util("radio")),
            opt("Ajustar Criogenia", action=lambda s: ajustar_util("crio")),
            opt("Voltar", action = back_action)
        ]),
        opt("Deslocar", action=lambda s: None),
        opt("Interagir", action=lambda s: None),
        opt("Confirmar Ações",        action=confirmar_acoes, submenu=[
        opt("Sim", action = force_confirm),
        opt("Não", action = lambda s: BACK),
        ]),
        opt("Voltar",        action=lambda s: BACK),
    ]),   

    opt("Atirador",submenu=[
        opt("Atirar em um Inimigo",   action=lambda s: None),
        opt("Abrir Painel de Utilitários", submenu=[
            opt("Ajustar Gravidade", action = lambda s: ajustar_util("grav")),
            opt("Ajustar Sonar", action=lambda s: ajustar_util("sonar")),
            opt("Ajustar Rádio", action=lambda s: ajustar_util("radio")),
            opt("Ajustar Criogenia", action=lambda s: ajustar_util("crio")),
            opt("Voltar", action = lambda s: BACK),
        ]),
        opt("Abrir Painel de Comunicações", submenu=[
            opt("Interceptar Comms Inimigas", action=lambda s: None),
            opt("Enviar Mensagem", action=lambda s: None),
            opt("Sabotar Comms Inimigas", action=lambda s: None),
            opt("Voltar", action = lambda s: BACK),
        ]),
        opt("Confirmar Ações",        action=confirmar_acoes, submenu=[
        opt("Sim", action = force_confirm),
        opt("Não", action = lambda s: BACK),
        ]),
        opt("Voltar", action = lambda s: BACK),
    ]),

    opt("Atirador AAE", submenu=[
        opt("Atirar em um Inimigo",   action=lambda s: None),
        opt("Trocar Tipo de Munição", action=lambda s: None),
        opt("Procurar Ponto Fraco",   action=lambda s: None),
        opt("Levantar",               action=lambda s: None),
        opt("Confirmar Ações",        action=confirmar_acoes, submenu=[
        opt("Sim", action = force_confirm),
        opt("Não", action = lambda s: BACK),
        ]),
        opt("Voltar", action = lambda s: BACK),
    ]),

    opt("Confirmar Ações", action=confirmar_acoes),
    opt("Desligar Jogo",   action=escape_seq),
]

#entry point
def main(stdscr):
    curses.curs_set(0)
    curses.noecho()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    run_menu(stdscr, MENU, layout="horizontal", draw_extras=draw_extras)
    # To add game-state overlays to the top layer:
    # run_menu(stdscr, MENU, layout="horizontal", draw_extras=my_hud_fn)

if __name__ == '__main__':
    while f['gameon'] == 1:
        if f['foo'] > 1 or f['foo'] <= 0:
            setfoo('foo', 1)
        if f['gamewin'] == 1:
            setfoo('gameon', 0)
        if f['turnosatuais'] <3:
            setfoo('turnos', f['turnos']+1)
            #[coisas dentro do turno]
            setfoo('turnosatuais', f['turnosatuais'] + 1)
        setfoo('rods', f['rods']+1)
        curses.wrapper(main)
        if f['turnosatuais'] >= 3: #fecha a rodada após três ações
            eor() #processa danos contínuos e atualizações de fim de rodada
            setfoo('rods', f['rods'] + 1) #conta rodadas completas
            setfoo('turnosatuais', 0) #prepara a próxima rodada



