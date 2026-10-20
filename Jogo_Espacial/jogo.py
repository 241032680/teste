import time
import array


def getstat(stat):
    return sum(stat)

def initstat():
    return array.array('b', [0]*8)

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


def setfoo(foo, valor):
    f[foo] = valor

#stats nave
numtorpedos,numaae,numfrontal,hp,escudo,velmax,escudot,escudof,direct,overclock,modoativo = initstat()
grav = sonar,radio,crio,danotorp,danoaae,danofront,criodesmaio,depressurização,riscomotor = initstat()
numtorpedos[0] = 5
numaae[0] = 8
numfrontal[0] = 6
hp[0] = 20
velmax[0] = 7
direct[0] = 1
modoativo[0] = 1
grav[0] = 1
sonar[0] = 1
radio[0] = 1
crio[0] = 1
danotorp[0] = 1
danoaae[0] = 1
danofront[0] = 1
criodesmaio[0] = 5
depressurização[0] = 3
riscomotor[0] = 8

#stats
nave = pilotagem = utilitarios =comunicaçao = conserto = navegaçao = tecnica = initstat()
nave[0],pilotagem[0],utilitarios[0],comunicaçao[0],conserto[0],navegaçao[0],tecnica[0]= 0,1,1,1,1,1,1
combate = curtoalc = medioalc = longoalc = armasenergia = armasprojetil = bastoes = corpoacorpo = laminas = mira = percepçao = resistencia = initstat()
combate[0],curtoalc[0],medioalc[0],longoalc[0],armasenergia[0],armasprojetil[0],bastoes[0],corpoacorpo[0],laminas[0],mira[0],percepçao[0],resistencia[0] = 0,1,1,1,1,1,1,1,1,1,1,1
mobilidade[0],rolls[0],cover[0],mira[0],percepçao[0] = 1,1,1,1,1


#buffs/debuffs modo: stat[1]
#buffs/debuffs crio: stat[2]
#buffs/debuffs sonar: stat[3]
#buffs/debuffs radio: stat[4]
#buffs/debuffs grav: stat[5]
#buffs/debuffs danonave: stat[6]
#stats/debuffs players: stat [7]

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
    'danoarmazém': False, 'danomedbay': False, 'danocozinha': False,
    'genescudo': True, 'criodesmaio': 5, 'hitcrio': 0,
    'rodssemgrav': 0, 'numquartos': 0, 'quarto': -1, 'salacomum': False,
    'novoprop': 0, 'novaasa': 0, 'riscoverclock': 0,
    'danomotor': False, 'falhamotor': False, 'direçãoinimigo': None,
}) #define estados iniciais usados antes do primeiro dano

def flip(): #ativar/desativar overclock
    overclock[0] = int(not getstat(overclock))
    setfoo('motorquente', bool(overclock[0]))
    setmodo(getstat(modoativo)) #setmodo também atualiza a distribuição dos escudos
    return ()

def setdirect(direcao): #direcionar foco dos escudos (equilibrado, frente, atrás)
    escudo_base = getstat(escudo)
    escudo_total = escudo_base + 5 * getstat(overclock) #reutiliza o total do escudo
    if direcao == 1:
        escudof[0], escudot[0] = ceil(escudo_total, 1), int(escudo_total)
    elif direcao == 2:
        escudof[0], escudot[0] = int(escudo_total * 1.5), ceil(escudo_total * 0.5, 1)
    elif direcao == 3:
        escudof[0], escudot[0] = ceil(escudo_total * 0.5, 1), int(escudo_total * 1.5)
    else:
        escudof[0], escudot[0] = ceil(escudo_base, 1), int(escudo_base)
    direct[0] = direcao
    return direct
MODOS = {
    1: (10, 0, 0, 0, 0, 0, 0),
    2: (15, -2, -8, -5, -6, -1, -1),
    3: (9, 3, -5, -5, -4, 2, -1),
    4: (7, -1, 6, 1, 4, 0, -1),
    5: (8, -1, -3, 5, -2, 1, 2),
} #centraliza os modificadores de cada modo

def setmodo(modo): #modos de distribuição de energia
    if modo not in MODOS:
        modo = 1 #corrigido: evita recursão para o modo padrão
    modoativo[0] = modo
    (escudo[1], velmax[1], danoaae[1], danotorp[1],
     danofront[1], pilotagem[1], utilitarios[1]) = MODOS[modo]
    setdirect(getstat(direct))
    return modoativo

setmodo(1)
setfoo('escudoefetivof', escudof[0]) #inicializa o escudo frontal
setfoo('escudoefetivot', escudot[0]) #inicializa o escudo traseiro

def utilbase(crioat, sonarat, radioat, gravat): #utilitários
    crio[0], sonar[0], radio[0], grav[0] = (
        int(bool(crioat)), int(bool(sonarat)), int(bool(radioat)), int(bool(gravat))
    ) #normaliza estados para 0/1

    if crio[0]:
        print("Crio On")
        rolls[2] = velmax[2] = danoaae[2] = danofront[2] = 0
    else:
        print("Crio Off")
        rolls[2], velmax[2], danoaae[2], danofront[2] = -1, 3, 4, 4

    if sonar[0]:
        print("Sonar On")
        mira[3] = percepçao[3] = danoaae[3] = danofront[3] = velmax[3] = 0
    else:
        print("Sonar Off")
        mira[3], percepçao[3], danoaae[3], danofront[3], velmax[3] = -2, -1, 3, 1, 1
        setfoo('podeusartorpedo', True)

    if radio[0]:
        print("Radio On")
        velmax[4] = 0
        radio[0] = radioat
    else:
        print("Radio Off")
        velmax[4] = 1
        setfoo('podeusarcomms', False)

    if grav[0]:
        print("Gravity On")
        mobilidade[5] = cover[5] = mira[5] = escudo[5] = danoaae[5] = danofront[5] = 0
    else:
        print("Gravity Off")
        mobilidade[5], cover[5], mira[5], escudo[5], danoaae[5], danofront[5] = -2, -2, -1, 2, 1, 1

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

def hitnave(intensidade): #acertos de inimigos
    intensidade = intensidade.lower()
    if intensidade == 'r':
        hitnave(('l', 'm', 'p')[rand() % 3]) #corrigido: r sorteia apenas a intensidade
        setfoo('foo', 1)
        return

    c = f['foo']
    y = "O casco"
    danos_base = {'l': 5, 'm': 8, 'p': 12}
    if intensidade not in danos_base:
        hp[0] -= 8
        z = ""
        c += 1
    else:
        z = {'l': 'leve', 'm': 'médio', 'p': 'pesado'}[intensidade]
        c = 0 if intensidade in ('m', 'p') else c
        dano = danos_base[intensidade]
        direcao = f.get('direçãoinimigo')
        if direcao == 'Frente' and f['escudoefetivof'] > 0:
            setfoo('escudoefetivof', f['escudoefetivof'] - dano) #escudo absorve o ataque inteiro
        elif direcao == 'Atras' and f['escudoefetivot'] > 0:
            setfoo('escudoefetivot', f['escudoefetivot'] - dano) #escudo absorve o ataque inteiro
        else:
            hp[0] -= dano

        if intensidade == 'l':
            match rand() % 12:
                case 0:
                    utilbase(0, getstat(sonar), getstat(radio), getstat(grav))
                    setfoo('danocrio', True)
                    rolls[6] -= 1
                    setfoo('hitcrio', f['hitcrio'] + 1)
                    y = "Criogênicos"
                case 1:
                    setfoo('danograv', True)
                    utilbase(getstat(crio), getstat(sonar), getstat(radio), 0)
                    y = "Gerador de Gravidade"
                case 2:
                    setfoo('genescudo', False)
                    y = "Gerador de Escudo"
                case 3:
                    setfoo('danomedbay', True)
                    y = "Medbay"
                case 4:
                    setfoo('danocozinha', True)
                    y = "Cozinha"
                case 5:
                    pass
                case 6:
                    setfoo('danoquartos', True)
                    setfoo('quarto', rand() % 6)
                    setfoo('numquartos', f['numquartos'] + 1)
                    y = "Um dos quartos"
                case 7:
                    setfoo('podeusarcomms', False)
                    y = 'Sala de Utilitários'
                case 8:
                    setfoo('danoarmazém', True)
                    y = 'Armazém'
                case 9:
                    setfoo('danohangar', True)
                    y = "Microhangar"
                case 10:
                    setfoo('danopropulsores', True)
                    if rand() % 12 == 0 and f['numprops'] < 9:
                        setfoo('novoprop', 1) #corrigido: sucesso é o resto zero
                    velmax[6] -= f['numprops'] + f['pesadoprop']
                    y = "Propulsor"
                case 11:
                    setfoo('danoasa', True)
                    if rand() % 8 == 0 and f['numasas'] < 4:
                        setfoo('novaasa', 1) #corrigido: sucesso é o resto zero
                    pilotagem[6] -= f['numasas'] + f['pesadoasa'] + f['medioasa']
                    y = "Uma asa!"

        elif intensidade == 'p':
            match rand() % 10:
                case 0|5:
                    pass
                case 6:
                    setfoo('pesadoprop', f['pesadoprop'] + 1)
                    setfoo('danopropulsores', True)
                    if rand() % 6 == 0 and f['numprops'] < 9:
                        setfoo('novoprop', 1) #corrigido: sucesso é o resto zero
                    velmax[6] -= f['numprops'] + f['pesadoprop']
                    y = "Um dos propulsores"

        elif intensidade == 'm':
            match rand() % 10:
		case 0|8:
                    pass
                case 9:
                    setfoo('danoasa', True)
                    if rand() % 6 == 0 and f['numasas'] < 4:
                        setfoo('novaasa', 1) #corrigido: sucesso é o resto zero
                    pilotagem[6] -= f['numasas'] + f['pesadoasa'] + f['medioasa']
                    y = "Uma asa!"

    if c < 2:
        print(f"{y} levou um tiro {z}!")

#ações players
def conserto(lugar):
    if lugar == 'prop':
        setfoo('numprops', f['numprops'] - 1)
        velmax[6] += 1 + f['pesadoprop']
    elif lugar == 'grav':
        mobilidade[6] += f['rodssemgrav'] * 2
        cover[6] += f['rodssemgrav']
        setfoo('rodssemgrav', 0)
        setfoo('danograv', False)
    elif lugar == 'crio':
        rolls[6] += f['hitcrio']
        setfoo('hitcrio', f['hitcrio'] - 1)
    elif lugar == 'geradorescudo':
        setfoo('genescudo', True)
        setfoo('escudoefetivof', escudof[0]) #corrigido: repara os escudos destruídos
        setfoo('escudoefetivot', escudot[0])
    elif lugar == 'comms':
        setfoo('podeusarcomms', True)
    elif lugar in QUARTOS:
        _, estado, _ = QUARTOS[lugar]
        setfoo(estado, False) #corrigido: usa o mesmo estado lido por danos()
        setfoo('numquartos', max(f['numquartos'] - 1, 0))
        if f['numquartos'] <= 0:
            setfoo('quarto', -1)
            setfoo('numquartos', 0)

    if f['numprops'] <= 0:
        setfoo('danopropulsores', False) #corrigido: nome do estado usado por danos()
    if f['quarto'] == -1 and f['numquartos'] <= 0:
        setfoo('salacomum', False) #corrigido: estado da sala comum
    if f['hitcrio'] <= 0:
        setfoo('danocrio', False)

#end of round

def inventorycheck(): #corrigido: remove itens aleatórios ao exceder a capacidade
    for inventario, capacidade in LIMITES_INVENTARIO:
        while len(inventario) > capacidade:
            inventario.pop(tuple(inventario)[rand() % len(inventario)]) #corrigido: remove por uma chave existente

def danos():
    if f['danograv']:
        setfoo('rodssemgrav', f['rodssemgrav'] + 1)
        mobilidade[6] -= 2
        cover[6] -= 1
        print("Gerador de Gravidade danificado!")

    desmaio = f['criodesmaio']
    if f['danocrio'] or getstat(crio) == 0:
        setfoo('criodesmaio', desmaio - 1)
        print(f"Sistema de Criogenia desativado! \n Jogadores desmaiarão em {desmaio} rodadas!")
    elif desmaio < 5:
        setfoo('criodesmaio', min(desmaio + 1, 5)) #simplificado: restaura um ponto por rodada

    if not f['podeusarcomms']:
        print("Sistema de Comunicações danificado!")
    if not f['genescudo']:
        print("Falha no Gerador de Escudos!") #corrigido: consulta o estado usado por genescudo()
    if f.get('danomotor', False) and f.get('falhamotor', False): #evita referências a nomes globais inexistentes
        pass

    if f['danopropulsores']:
        if f['novoprop'] == 1 and f['numprops'] < 9:
            setfoo('numprops', min(f['numprops'] + 1, 9)) #corrigido: respeita a capacidade máxima
            print('Um novo propulsor foi danificado!')
            setfoo('novoprop', 0)
        print("Propulsores danificados!")

    depressurizacao_restante = depressurização[0]
    if f['danohangar']:
        depressurização[0] = max(depressurização[0] - 1, 0)
        print(f"Brecha no Microhangar! \n Depressurização em {depressurizacao_restante} rodadas!")
    elif depressurizacao_restante < 3:
        depressurização[0] = min(depressurizacao_restante + 1, 3)
    if depressurizacao_restante >= 0:
        setfoo('hangarselado', True)

    if f['danoasa']:
        if f['novaasa'] == 1 and f['numasas'] < 4:
            setfoo('numasas', min(f['numasas'] + 1, 4)) #corrigido: respeita as quatro asas
            print('Uma nova asa foi danificada!')
            setfoo('novaasa', 0) #corrigido: limpa o indicador de asa
        if f['numasas'] == 1:
            print("Asa Danificada!")
        elif f['numasas'] > 1:
            print("Asas danificadas!")

    for estado, inventario in (
        ('danoarmazém', armazém), ('danomedbay', medbay), ('danocozinha', cozinha),
    ):
        if f[estado] and inventario:
            inventario.pop(tuple(inventario)[rand() % len(inventario)]) #corrigido: escolhe uma chave existente

    if f['danoquartos']:
        for indice, estado, inventario in QUARTOS.values():
            if f[estado] or f['quarto'] == indice:
                if inventario:
                    inventario.pop(tuple(inventario)[rand() % len(inventario)]) #corrigido: escolhe uma chave existente
                setfoo(estado, True)

def genescudo():
    if f['genescudo']:
        if f['escudoefetivof'] > 0:
            setfoo('escudoefetivof', escudof[0]) #regenera apenas se o escudo não foi destruído
        if f['escudoefetivot'] > 0:
            setfoo('escudoefetivot', escudot[0]) #regenera apenas se o escudo não foi destruído

#Overclocked: +5 Geração de Escudo, mas +¼ chance de fritar o Gerador por rodada utilizada (¼, ½ , ¾…)
def atualizaroverclock(): #risco de fritar o motor usando overclock
    if f['motorquente']:
        if getstat(overclock) == True:
            setfoo('riscoverclock', max(f['riscoverclock'] + 1,4))
        riscomotor[0] = f['riscoverclock'] #corrigido: remove expressão inválida
        #marchas: 1/9, 1/6, 1/3
        #oclock: +¼ por rod 
    else:
        riscomotor[0] = getstat(riscomotor) - f['riscoverclock']
def eor(): #executa atualizações no fechamento da rodada
    inventorycheck()
    genescudo()
    danos()
    atualizaroverclock()

#inimigo

def criarinimigo(tipo):
  if len(inimigos) > 10:
    return 0
  n = len(inimigos)
  inimigos[f'i{(n+1)}'] = {
  "tipo" : tipo,
  "hp" : 30 + float(((sin(rand())) * 6.66)),
  }

i1 = {
    "tipo de inimigo": "leve",
    "hp" : int((30 + (sin(rand())) * 6.66)),
    "velocidade": 6,
    "mísseis" : rand()%2,
    "escudo": 10,
    #"tipo de missel": tipomissel(),
    #"tipo de escudo": tipoescudo(),
    #"tipo de dano": tipodano(),
  }

i2 = {
  "tipo" : "medio",
  "hp" : 80
}

i3 = {
  "tipo" : "pesado",
  "hp" : 120
}

inimigos = {
  "i1" : i1,
  "i2" : i2,
  "i3" : i3
} 

def tipodano():
    tpd = rand()%6
    match tpd:
        case 0:
            return "íon" # +dano escudo -dano casco
        case 1|2: 
            return "plasma" #-dano escudo +dano casco
        case 3|4|5: 
            return "proton" #sem modificadores

def tipoescudo():
    scd = rand()%8
    match scd:
        case 0:
            return "Deflector" #padrao
        case 1: 
            return "Conversion" #quando o escudo é desativado, desliga todas as armas mas cria uma barreira forte
        case 2: 
            return "Fortificado" #mais forte, regenera mais devagar
        case 3:
            return "Nimble" #mais fraco, regenera mais rapido
        case 4:
            return "Overloaded" #muito mais forte, regenera lento, não regenera se completamente derrubado
        case 5:
            return "Ray" #leva menos dano de torretas e mais dano de torpedos
        case 6:
            return "Resonant" #Mais fraco, aumenta o dano das proprias armas
        case 7:
            return "Scrambler" #Dificulta lock in misseis e torretas quando 100%, demora mais p/ começar a regenerar


def tipomissel():
    msl = rand()%4
    match msl:
        case 0: #misseis
            if i[['tipo']]=="pesado":
                msl1=rand()%4
            else:
                msl1=rand()%3
            match msl1:
                case 0:
                    return "Concussion"
                case 1:
                    return "Ion"
                case 2:
                    return "Multi-Lock"
                case 3:
                    return "Goliath"
        case 1: #torpedos
            pass
        case 2: #bombas
            pass
        case 3: #foguetes
            pass


for x in range(1, 19):
    additem(armazém, str(x), rand()%90)
print(armazém)
print(len(armazém)) 

setfoo('turnosatuais', 0)


#testes de DT

tipodadonivel = {1: 6, 2: 8, 3: 10, 4: 12, 5: 20}

DT = {1: (10, 12, 14),
    2: (11, 14, 18),
    3: (12, 16, 21),
    4: (13, 18, 24),
    5: (18, 26, 36)}

criançasproblema = {
    'conserto': (2, 2, 3),
    'comunicacao': (-2, 2, 4), 'comunicacoes': (-2, 2, 4),
    'forca': (2, 1, 3),
    'intimidacao': (3, 3, 3),
    'medicina': (3, 2, 3),
    'mira': (2, 0, 2),
    'percepcao': (3, 0, 2),
    'saude': (2, -1, 1),
    'tecnica': (2, -1, 1),
} #casos especiais

bonuscargosempre = {
    'piloto': {'nave': 3, 'percepcao': 1, 'carisma': 1},
    'engenheiro': {'conserto': 3, 'abrir travas': 2},
    'atirador': {'forca': 2, 'comunicacao': 1, 'intimidacao': 1, 'resistencia': 1},
    'atirador aae': {'mira': 3, 'furtividade': 1, 'desvio': 1},
    'copiloto': {'nave': 2, 'saude': 1, 'sorte': 1, 'agilidade': 1},
} 

def rolar_teste(stats, dificuldade='medio', cargo=None, nomes_stats=None,
                 bonus_cargo=0, modificador_stat=0, modificador_rolagem=0,
                 caso_especial=None, dados_forcados=None):
    match cargo:
        case 'piloto':
            nave[7], percepçao[7] = 3, 2
        case 'engenheiro':
        case 'atirador':
        case 'atirador_aae':
        case 'copiloto':


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

def draw_menu_horizontal(stdscr, items, selected, draw_extras=None):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

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
    stdscr.clear()
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

def run_menu(stdscr, items, layout="vertical", draw_extras=None):
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
                result = run_menu(stdscr, item.submenu)   # always vertical
                if result is EXIT:
                    return EXIT
                # BACK from child → fall through, redraw this level
            elif item.action:
                result = item.action(stdscr)
                if result is EXIT:
                    return EXIT
                if result is BACK:
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
    stdscr.clear()
    msg = "Ações Confirmadas"
    stdscr.addstr(h // 2, w // 2 - len(msg) // 2, msg)
    stdscr.refresh()
    timer(25)



def escape_seq():
    setfoo('gameon', 0)
    setfoo('gamewin', 1)

def force_confirm():
    setfoo('turnosatuais', 3)

# ── Menu tree (only edit this to add new menus/submenus) ──────────────────────
MENU = [
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
        opt("Não", action = lambda s: None),]),        
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
        opt("Não", action = lambda s: None),]),        
        ]),

    opt("Engenheiro", submenu=[
        opt("Consertar",   action=lambda s: None),
        opt("Abrir Painel de Utilitários", submenu=[
            opt("Ajustar Gravidade", action=lambda s: None),
            opt("Ajustar Sonar",   action=lambda s: None),
            opt("Ajustar Rádio",   action=lambda s: None),
            opt("Ajustar Criogenia", action=lambda s: None),
            opt("Voltar", action = back_action)
        ]),
        opt("Deslocar", action=lambda s: None),
        opt("Interagir", action=lambda s: None),
        opt("Confirmar Ações",        action=confirmar_acoes, submenu=[
        opt("Sim", action = force_confirm),
        opt("Não", action = lambda s: None),
        ]),
        opt("Voltar",        action=back_action),
    ]),   

    opt("Atirador",submenu=[
        opt("Atirar em um Inimigo",   action=lambda s: None),
        opt("Abrir Painel de Utilitários", submenu=[
            opt("Ajustar Gravidade", action=lambda s: None),
            opt("Ajustar Sonar",   action=lambda s: None),
            opt("Ajustar Rádio",   action=lambda s: None),
            opt("Ajustar Criogenia", action=lambda s: None),
            opt("Voltar", action=back_action)
        ]),
        opt("Abrir Painel de Comunicações", submenu=[
            opt("Interceptar Comms Inimigas", action=lambda s: None),
            opt("Enviar Mensagem", action=lambda s: None),
            opt("Sabotar Comms Inimigas", action=lambda s: None),
            opt("Voltar", action=back_action)
        ]),
        opt("Confirmar Ações",        action=confirmar_acoes, submenu=[
        opt("Sim", action = force_confirm),
        opt("Não", action = lambda s: None),
        ]),
        opt("Voltar",        action=back_action),
    ]),

    opt("Atirador AAE", submenu=[
        opt("Atirar em um Inimigo",   action=lambda s: None),
        opt("Trocar Tipo de Munição", action=lambda s: None),
        opt("Procurar Ponto Fraco",   action=lambda s: None),
        opt("Levantar",               action=lambda s: None),
        opt("Confirmar Ações",        action=confirmar_acoes, submenu=[
        opt("Sim", action = force_confirm),
        opt("Não", action = lambda s: None),
        ]),
        opt("Voltar",        action = back_action),
    ]),

    opt("Confirmar Ações", action=confirmar_acoes),
    opt("Desligar Jogo",   action=escape_seq),
]


#entry point
def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    run_menu(stdscr, MENU, layout="horizontal")
    # To add game-state overlays to the top layer:
    # run_menu(stdscr, MENU, layout="horizontal", draw_extras=my_hud_fn)



while f['gameon'] == 1: #stats derivados são calculados diretamente com getstat()
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


def atirador_aae(ação):
    match ação:
        case "atirar":
            pass


#criar função pra ler input e output
#criar cli bonitinha
#tabs 1 2 3 4 5 com ações de cada player, quando todas escolhidas, turno dos inimigos
#calculo e ajustes, repete
