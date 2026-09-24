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
s = {}
f = {}
b = {}
t = {}
def setstat(name, value):
    s[name] = value
def setfoo(foo, valor):
    f[foo] = valor
def setbuff(buff, valor):
    b[buff] = valor
def settipo(tipo, nome):
    t[tipo] = nome
def updater(): #atualiza stats globais
    setstat('danoaae', (s['aaebase']+b['bcaae']+b['bmaae']+b['bdaae']+b['braae']+b['bgaae']+b['bsaae'])* t['tipoaae'])
    setbuff('danotorp', (s['torpbase'] +b['bctorp']+b['bmtorp']+b['bdtorp']+b['brtorp']+b['bgtorp']+b['bstorp']) * t['tipotorp'])
    setstat('velmax', s['velmaxbase']+b['bcvelmax']+b['bmvelmax']+b['bdvelmax']+b['brvelmax']+b['bgvelmax']+b['bsvelmax'])
    setstat('danofrontal', s['frontalbase']+b['bcfront']+b['bmfront']+b['bdfront']+b['brfront']+b['bgfront']+b['bsfront'])

#stats individuais:
#setstat(stat qualquer) (alvo) = statbase(alvo) + b(buff)(stat)
    #setstat('mobil', s['mobilbase'] +b['bcmobil']+b['bmmobil']+b['bdmobil']+b['brmobil']+b['bgmobil']+b['bsmobil'])
    #setstat('util', s['utilbase'] +b['bcutil']+b['bmutil']+b['bdutil']+b['brutil']+b['bgutil']+b['bsutil'])
    #setstat('pilot', s['pilotbase'] +b['bcpilot']+b['bmpilot']+b['bdpilot']+b['brpilot']+b['bgpilot']+b['bspilot'])
    #setstat('rolls', s['rollsbase']+b['bcpilot']+b['bmpilot']+b['bdpilot']+b['brpilot']+b['bgpilot']+b['bspilot'])
    #setstat('cover', s['coverbase'] +b['bccover']+b['bmcover']+b['bdcover']+b['brcover']+b['bgcover']+b['bscover'])


#stats nave

setstat('numtorpedos', 5)
setstat('numaae', 8)
setstat('numfrontal', 6)
setstat('hp', 20)
setstat('escudo', 0)
setstat('velmax', 7)
setstat('escudof', 0)
setstat('escudot', 0)
setstat('overclock', 0)
setstat('direct', 1)
setstat('modo', 1)
setstat('grav', 3)
setstat('sonar', 3)
setstat('radio', 3)
setstat('crio', 3)
setstat('podeusartorpedo', True)
setstat('podeusarcomms', True)
setstat('torpbase', 1)
setstat('aaebase', 1)
setstat('frontalbase', 1)
setstat('criodesmaio', 5)
setstat('depressurização', 3)
setstat('hangarselado', False)
setstat('motorfrito', False)
setstat('motorquente', False)
setstat('riscomotor', 8)
#buffs crio
setbuff('bcmobil',0)
setbuff('bcmira',0)
setbuff('bcpercep',0)
setbuff('bcpilot', 0)
setbuff('bcutil', 0)
setbuff('bctorp', 0)
setbuff('bcaae', 0)
setbuff('bcfront', 0)
setbuff('bcvelmax',0)
setbuff('bcrolls',0)
setbuff('bccover',0)
setbuff('bcescudo',0)
#buffs modo
setbuff('bmmobil',0)
setbuff('bmmira',0)
setbuff('bmpercep',0)
setbuff('bmpilot', 0)
setbuff('bmutil', 0)
setbuff('bmtorp', 0)
setbuff('bmaae', 0)
setbuff('bmfront', 0)
setbuff('bmvelmax',0)
setbuff('bmrolls',0)
setbuff('bmcover',0)
setbuff('bmescudo',0)
#buffs radio
setbuff('brmobil',0)
setbuff('brmira',0)
setbuff('brpercep',0)
setbuff('brpilot', 0)
setbuff('brutil', 0)
setbuff('brtorp', 0)
setbuff('braae', 0)
setbuff('brfront', 0)
setbuff('brvelmax',0)
setbuff('brrolls',0)
setbuff('brcover',0)
setbuff('brescudo',0)
#buffs sonar
setbuff('bsmobil',0)
setbuff('bsmira',0)
setbuff('bspercep',0)
setbuff('bspilot', 0)
setbuff('bsutil', 0)
setbuff('bstorp', 0)
setbuff('bsaae', 0)
setbuff('bsfront', 0)
setbuff('bsvelmax',0)
setbuff('bsrolls',0)
setbuff('bscover',0)
setbuff('bsescudo',0)
#buffs grav
setbuff('bgmobil',0)
setbuff('bgmira',0)
setbuff('bgpercep',0)
setbuff('bgpilot', 0)
setbuff('bgutil', 0)
setbuff('bgtorp', 0)
setbuff('bgaae', 0)
setbuff('bgfront', 0)
setbuff('bgvelmax',0)
setbuff('bgrolls',0)
setbuff('bgcover',0)
setbuff('bgescudo',0)
#buffs danonave
setbuff('bdmobil',0)
setbuff('bdmira',0)
setbuff('bdpercep',0)
setbuff('bdpilot', 0)
setbuff('bdutil', 0)
setbuff('bdtorp', 0)
setbuff('bdaae', 0)
setbuff('bdfront', 0)
setbuff('bdvelmax',0)
setbuff('bdrolls',0)
setbuff('bdcover',0)
setbuff('bdescudo',0)
#stats players
setstat('pilotbase', 1)
setstat('mobil',1)
setstat('velmaxbase',1)
setstat('rollsbase',1)
setstat('coverbase',1)
setstat('mirabase',1)
setstat('percepbase',1)
setstat('utilbase', 1)

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

#tipos de dano
settipo('tipoaae', 1)
settipo('tipotorp', 1)

#print(s['torpedos'], s['plasma'], s['av'], s['gas'], s['aaebase'], s['frontalbase'], s['icss'], s['bateria'], s['cohm'], s['hp'], s['escudo'])

#distribuição de escudo
#Padrão: Geração de Escudo Total = 10
#frontal: Geração de Escudo frontal x Traseiro = [15 , 5]
#Traseira: Geração de Escudo frontal x Traseiro = [5 , 15]
#Overclocked: +5 Geração de Escudo, mas +¼ chance de fritar o Gerador por rodada utilizada (¼, ½ , ¾…)

def flip(): #ativar/desativar overclock
    if (s['overclock']) == 0:
        setstat ('overclock', int(1))
        setstat('motorquente', True)
    else:
        setstat('overclock', int(0))
        setstat('motorquente', False)
    setdirect(s['direct'])
    setmodo(modo)
    return ()
def setdirect(direct): #direcionar foco dos escudos (equilibrado, frente, atrás)
    if (direct) == 1:
        setstat ('escudof', ceil((s['escudo'] + (5*s['overclock'])),1))
        setstat ('escudot', int((s['escudo'] + (5*s['overclock']))))
    elif (direct) == 2:
        setstat ('escudof', int((s['escudo'] + (5*s['overclock']))*(1.5)))
        setstat ('escudot', ceil((s['escudo'] + (5*s['overclock']))*(0.5),1))
    elif (direct) == 3:
        setstat ('escudof', ceil((s['escudo'] + (5*s['overclock']))*(0.5), 1))
        setstat ('escudot', int((s['escudo'] + (5*s['overclock']))*(1.5)))
    else:
        setstat ('escudof', ceil(s['escudo'], 1))
        setstat ('escudot', int(s['escudo']))
    setstat('direct', direct)
    updater()
    return direct

def setmodo(modo): #modos de distribuição de energia
    if modo == int(1): #padrao
        setstat('escudo', 10)
        setbuff('bmvelmax', 0)
        setbuff('bmtorp', 0)
        setbuff('bmaae', 0)
        setbuff('bmfront', 0)
        setbuff('bmpilot', 0)
        setbuff('bmutil', 0)
    elif modo == int(2): #escudo
        setstat('escudo', 15)
        setbuff('bmvelmax', -2)
        setbuff('bmtorp', -5)
        setbuff('bmaae', -8)
        setbuff('bmfront', -6)
        setbuff('bmpilot', -1)
        setbuff('bmutil', -1)
    elif modo == int(3): #propulsores
        setstat('escudo', 9)
        setbuff('bmvelmax', 3)
        setbuff('bmaae', -5)
        setbuff('bmtorp', -5)
        setbuff('bmfront', -4)
        setbuff('bmpilot', 2)
        setbuff('bmutil', -1)
    elif modo == int(4): #torretas
        setstat('escudo', 7)
        setbuff('bmvelmax', -1)
        setbuff('bmaae', 6)
        setbuff('bmtorp', 1)
        setbuff('bmfront', 4)
        setbuff('bmpilot', 0)
        setbuff('bmutil', -1)
    elif modo == int(5): #utilitários
        modo = 5
        setstat('escudo', 8)
        setbuff('bmvelmax', -1)
        setbuff('bmaae', -3)
        setbuff('bmtorp', 5 )
        setbuff('bmfront', -2)
        setbuff('bmpilot', 1)
        setbuff('bmutil', 2)
    else:
        modo = setmodo(1)
    setstat('escudo', s['escudo'])
    setstat('modo', modo)
    setdirect(s['direct'])
    updater()
    return modo

modo = setmodo(1)

def utilbase(crio, sonar, radio, grav): #utilitários
    setstat('crio', crio)
    setstat('sonar', sonar)
    setstat('radio', radio)
    setstat('grav', grav)
    if crio == True or crio == 1 or s['crio']==1:
        print ("Crio On")
        setbuff('bcrolls', 0)
        setbuff('bcvelmax', 0)
        setbuff('bcaae', 0)
        setbuff('bcfront', 0)
        setstat('crio', crio)
        #return s['crio']
    else:
        print ("Crio Off")
        setbuff('bcrolls', -1)
        setbuff('bcvelmax', 3)
        setbuff('bcaae', 4)
        setbuff('bcfront', 4)
        setstat('crio', crio)
        #return s['crio']
    if sonar == True or sonar == 1 or s['sonar']==1:
        print ("Sonar On")
        setbuff('bsmira', 0)
        setbuff('bspercep', 0)
        setbuff('bsaae', 0)
        setbuff('bsfront', 0)
        setbuff('bsvelmax', 0)
        setstat('sonar', sonar)
        #return s['sonar']
    else:
        print ("Sonar Off")
        setstat('podeusartorpedo', True)
        setbuff('bsmira', -2)
        setbuff('bspercep', -1)
        setbuff('bsaae', 3)
        setbuff('bsfront', 1)
        setbuff('bsvelmax', 1)
        setstat('sonar', sonar)
        #return s['sonar']
    if radio == True or radio == 1 or s['radio']==1:
        print ("Radio On")
        setbuff('brvelmax', 0)
        setstat('radio', radio)
        #return s['radio']
    else:
        print ("Radio Off")
        setstat('podeusarcomms', False)
        setbuff('brvelmax', 1)
        setstat('radio', radio)
        #return s['radio']
    if grav == True or grav == 1 or s['grav']==1:
        print ("Gravity On")
        setbuff('bgmobil', 0)
        setbuff('bgcover', 0)
        setbuff('bgmira', 0)
        setbuff('bgescudo', 0)
        setstat('bgaee', 0)
        setbuff('bgfront', 0)
        setstat('grav', grav)
        #return s['grav']
    else:
        print ("Gravity Off")
        setbuff('bgmobil', -2)
        setbuff('bgcover', -2)
        setbuff('bgmira', -1)
        setbuff('bgescudo', 2)
        setstat('bgaee', 1)
        setbuff('bgfront', 1)
        setstat('grav', grav)
        #return s['grav']

#inventários

#armazém (18 slots)
#gera 18 itens de valor aleatório, que definem o valor da recomepensa no final do jogo
#quanto mais itens chegarem no checkpoint final, melhor o score
#varias mecanicas fazem os itens perderem valor

armazém = {}
cozinha = {}
medbay = {}
salacomum = {}

def arm(nome, valor):
    armazém[nome.upper()] = valor

#armazém('caixa de madeira', 90)


#medbay (12 slots)
#itens de cura
def med(nome, valor, tipo):
    medbay[nome.upper()] = valor
    medbay['Tipo:'] = tipo.capitalize()

#cozinha (12 slots)
#itens de cura, rango e alguns valiosos

def coz(nome, valor, tipo):
    cozinha[nome.capitalize()] = valor
    cozinha['Tipo:'] = tipo.capitalize()

#sala comum (6 slots)
#itens pessoais de players, o que não couber em outros espaçoes

def sala(nome, valor, tipo):
    salacomum[nome.capitalize()] = valor
    salacomum['Tipo:'] = tipo.capitalize()



#rodada: cada jogador e inimmigo tem seu turno
#turno de cada jogador: 3 ações
#turno de cada inimigo: instantâneo
#ordem de turnos: piloto, copiloto, engenheiro, atirador, atirador aaebase, ajuste de distância, inimigos

def hitnave(intensidade): #acertos de inimigos
    c = 0 + s['foo']
    y = "O casco"
    match intensidade:
        case"L" | "l": #leve
            if s['escudoefetivof'] > 0 and s['direçãoinimigo'] == "Frente":
                setstat('escudoefetivof', s['escudoefetivof'] - 5)
            elif s['escudoefetivot'] > 0 and s['direçãoinimigo'] == "Atras":
                setstat('escudoefetivot', s['escudoefetivot'] - 5)
            else:
                setstat('hp', s['hp'] -5)
            z = str("leve")
            a = (rand()%12)
            #if 
            match a:
                case 0:
                    utilbase(0, sonar=s['sonar'], radio=s['radio'], grav=s['grav'])
                    setstat('danocrio', True)
                    setbuff('bdrolls', b['bdrolls'] - 1)
                    setfoo('hitcrio', s['hitcrio'] + 1)
                    y = "Criogênicos"
                case 1:
                    setstat('danograv', True)
                    utilbase(crio=s['crio'], sonar=s['sonar'], radio=s['radio'], grav=0)
                    y = "Gerador de Gravidade"
                case 2:
                    setstat('genescudo', False)
                    y = "Gerador de Escudo"
                case 3:
                    setstat('danomedbay', True)
                    y = "Medbay"
                case 4:
                    setstat('danocozinha', True)
                    y = "Cozinha"
                case 5:
                    pass
                case 6:
                    setstat('danoquartos', True)
                    setfoo('quarto', rand()%6)
                    setfoo('numquartos', f['numquartos']+1)
                    y = "Um dos quartos"
                case 7:
                    setstat('podeusarcomms', False)
                    y = 'Sala de Utilitários'
                case 8:
                    setstat('danoarmazém', True)
                    y = 'Armazém'
                case 9:
                    setstat('danohangar', True)
                    y = "Microhangar"
                case 10:
                    setstat('danopropulsores', True)
                    k = rand()%12
                    if k == 12:
                        setstat('novoprop', 1)
                    setbuff('bdvelmax', (b['bdvelmax']) -(1*(s['numprops']+f['pesadoprop'])))
                    y = "Propulsor"
                case 11:
                    setstat('danoasa', True)
                    k = rand()%8
                    if k == 8 and f['numasas']<4:
                        setstat('novaasa', 1)
                    setbuff('bdpilot', (b['bdpilot']) -(1*(f['numasas']+f['pesadoasa']+f['medioasa'])))
                    y = "Uma asa!"

        case "P" | "p": #pesado
            setstat('hp', s['hp'] -12)
            z = str("pesado")
            c = 0
            p = rand()%10
            match p:
                case 0|5:
                    pass
                case 6:
                    setstat('pesadoprop', f['pesadoprop']+ 1)
                    setstat('danopropulsores', True)
                    k = rand()%6
                    if k == 6 and s['numprops'] < 9:
                        setstat('novoprop', 1)
                    setbuff('bdvelmax', (b['bdvelmax']) -(1*(s['numprops']+f['pesadoprop'])))
                    y = "Um dos propulsores"
                case 7|9:
                    pass
        case "M" | "m":
            setstat('hp', s['hp'] -8)
            z = str("médio")
            c = 0
            m = rand()%10
            match m:
                case 0|8:
                    pass
                case 9:
                    setstat('danoasa', True)
                    k = rand()%6
                    if k == 6 and f['numasas']<4:
                        setstat('novaasa', 1)
                    setbuff('bdpilot', (b['bdpilot']) -(1*(f['numasas']+f['pesadoasa']+f['medioasa'])))
                    y = "Uma asa!"
        case _:
            setstat('hp', s['hp'] -8)
            z = ""
            c += 1
            #setfoo('foo', s['foo'] + 1)
    if c < 2:
        print(f"{y} levou um tiro {z}!")
    if intensidade == "r" or intensidade == "R":
        b = rand()%3
        y = "Algo"
        z = ""
        c = 0
        if b == 0:
            hitnave('l')
            setfoo('foo', 1)
        elif b == 1:
            hitnave('m')
            setfoo('foo', 1)
        elif b == 2:
            hitnave('p')
            setfoo('foo', 1)
        setfoo('foo', 1)
    
#ações players
def conserto(lugar):
    match lugar:
        case 'prop':
            setstat('numprops', s['numprops'] -1)
            setbuff('bdvelmax', b['bdvelmax'] + (1*(1+f['pesadoprop'])))
            if s['numprops'] <= 0:
                setstat('danoprop', False)
        case 'grav':
            setbuff('bdmobil', b['bdmobil']+s['rodssemgrav']*2)
            setbuff('bdcover', b['bdcover']+s['rodssemgrav']*1)
            setstat('rodssemgrav', 0)
            setstat('danograv', False)
        case 'crio':
            setbuff('bdrolls', b['bdrolls'] + (1*f['hitcrio']))
            setfoo('hitcrio', f['hitcrio'] -1)
            if f['hitcrio'] <=0:
                setstat('danocrio', False)
        case 'geradorescudo':
            setstat('genescudo', True)
        case 'comms':
            setstat('podeusarcomms', True)
        case 'quarto1':
            setfoo('quarto1dano', False)
            setfoo('numquartos', f['numquartos'] - 1)
            if f['numquartos'] <=0:
                setfoo('quarto',-1)
                setfoo('numquartos', 0)
        case 'quarto2':
            setfoo('quarto2dano', False)
            setfoo('numquartos', f['numquartos'] - 1)
            if f['numquartos'] <=0:
                setfoo('quarto',-1)
                setfoo('numquartos', 0) 
        case 'quarto3':
            setfoo('quarto3dano', False)
            setfoo('numquartos', f['numquartos'] - 1)
            if f['numquartos'] <=0:
                setfoo('quarto',-1)
                setfoo('numquartos', 0)
        case 'quarto4':
            setfoo('quarto4dano', False)
            setfoo('numquartos', f['numquartos'] - 1)
            if f['numquartos'] <=0:
                setfoo('quarto',-1)
                setfoo('numquartos', 0)
        case 'quarto5':
            setfoo('quarto5dano', False)
            setfoo('numquartos', f['numquartos'] - 1)
            if f['numquartos'] <=0:
                setfoo('quarto',-1)
                setfoo('numquartos', 0)
        case 'salacomum':
            setfoo('danosalacomum', False)
            setfoo('numquartos', f['numquartos'] - 1)
            if f['numquartos'] <=0:
                setfoo('quarto',-1)
                setfoo('numquartos', 0)
#end of round
def genescudo():
    if s['genescudo'] == True:
        setstat('escudoefetivof', s['escudof'] + b['bgescudo'] + b['bmescudo'] + b['bsescudo'] + b['bcescudo']+ b['brescudo'] + b['bdescudo'])
        setstat('escudoefetivot', s['escudot'] + b['bgescudo'] + b['bmescudo'] + b['bsescudo'] + b['bcescudo']+ b['brescudo'] + b['bdescudo'])

def inventorycheck():
    while len(armazém) > 18:
      armazém.popitem
    while len(cozinha) > 12:
      medbay.popitem
    while len(medbay) > 12:
      medbay.popitem
    while len(salacomum) > 6:
      salacomum.popitem
def danos():
    rodssemgrav = max(s['rodssemgrav'], 5)
    danograv = s['danograv']
    danocrio = s['danocrio']
    danocomms = s['podeusarcomms']
    danoescudo = s['geradorescudo']
    danohangar = s['danohangar']
    danoasa = s['danoasa']
    if danograv == True:
        setstat('rodssemgrav', s['rodssemgrav'] +1)
        setbuff('bmobil', (b['bmobil']) -2)
        setbuff('bcover', (b['bcover']) -1)
        print("Gerador de Gravidade danificado!")
    desmaio = s['criodesmaio']
    if danocrio == True or s['crio'] == 0 or s['crio'] == False:
        setstat('criodesmaio', s['criodesmaio'] -1)
        print(f"Sistema de Criogenia desativado! \n Jogadores desmaiarão em {desmaio} rodadas!")
    if danocrio == False:
        if desmaio < 5:
            setstat('criodesmaio', min(desmaio - int(~int(danocrio)), 5))
    if danocomms == True:
        print("Sistema de Comunicações danificado!")
    if danoescudo == True:
        print("Falha no Gerador de Escudos!")
    if danomotor == True:
        if falhamotor == True:
            pass
        else:
            pass
    if danopropulsores == True:
        if novoprop == 1 and s['numprops'] != 9:
            setstat('numprops', max(s['numprops']+1, 9))
            print('Um novo propulsor foi danificado!')
            setstat('novoprop', 0)
        print("Propulsores danificados!")
    depressurização = s['depressurização']
    if danohangar == True:
        setstat('depressurização', max(s['depressurização'] -1, 0))
        print(f"Brecha no Microhangar! \n Depressurização em {depressurização} rodadas!")
    if danohangar == False:
        if depressurização < 3:
            setstat('depressurização', min(depressurização - int(~int(danohangar)), 3))
    if depressurização >= 0:
        setstat('hangarselado', True)
    if danoasa == True:
        if novaasa == 1 and s['numprops'] != 4:
            setstat('numasas', max(f['numasas']+1, 4))
            print('Uma nova asa foi danificada!')
            setstat('novoprop', 0)
        if f['numasas'] == 1:
            print("Asa Danificada!")
        elif f['numasas'] > 1:
            print("Asas danificadas!")
    if danoarmazém == True:
        armazém.pop(rand%18)
    if danomedbay == True:
        medbay.pop(rand%12)
    if danocozinha == True:
        cozinha.pop(rand%12)
    if danosalacomum == True:
        if f['salacomum'] or f['quarto'] == 0:
            salacomum.pop(rand%6)
            setfoo('salacomum', True)
        if f['quarto1dano'] or f['quarto'] == 1:
            quarto1.pop(rand%6)
            setfoo('quarto1dano', True)
        if f['quarto2dano'] or f['quarto'] == 2:
            quarto2.pop(rand%6)
            setfoo('quarto2dano', True)
        if f['quarto3dano'] or f['quarto'] == 3:
            quarto3.pop(rand%6)
            setfoo('quarto3dano', True)
        if f['quarto4dano'] or f['quarto'] == 4:
            quarto4.pop(rand%6)
            setfoo('quarto4dano', True)
        if f['quarto5dano'] or f['quarto'] == 5:
            quarto5.pop(rand%6)
            setfoo('quarto5dano', True)

def overclock():
    if s['motorquente']:
        setstat('riscomotor', s['riscomotor'] -1)
        #marchas: 1/9, 1/6, 1/3
        #oclock: +¼ por rod 
def eor():
    inventorycheck()
    genescudo()
    updater()
    danos()
    overclock()

#inimigo

def criarinimigo(tipo):
  n = len(inimigos)
  inimigos[f'i{(n+1)}'] = {
  "tipo" : tipo,
  "hp" : 30 + float(((sin(rand()))*6.66)),
  }

i1 = {
    "tipo de inimigo": "leve",
    "hp" : int((30 + (sin(rand()))*6.66)),
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




#print(f'\n \n {"1"} in {i}')

#tipos de escudo/casco recebem resistencias e danos diferentes de tipos de tiro diferentes

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
#inimigos

#[1 2 3 4...]
#   ^ 
#propriedades (velocidade, tipo, etc)

#função de criar inimigos
#função de ação dos inimigos
#lógica de tripulação pro boarding
#lógica de uso dos mísseis
#lógica de movimento/espaçamento "3d" vulgo inferno provavelmente não vai rolar
#se rolar usar alguma formula de projeção 3d em plano 2d pra descobrir as line of sight
#provavelmente trampo
#variação de velocidade talvez?
#lógica de velocidade, tanto pra inimigo quanto pra player

#antes do while:
#-gerar inimigos, inventario, mapa, display e gerenciar inputs

for x in range(1, 19):
    arm(str(x), rand()%90)
print(armazém)
print(len(armazém))

setfoo('turnosatuais', 0)

import curses

import curses #biblioteca endemoniada

menu = ['Piloto', 'Copiloto', 'Engenheiro', 'Atirador', 'Atirador AAE', 'Desligar Jogo']
#o nome faz juz, essa bomba é amaldiçoada mesmo, roubei esse menu do Indian Pythonista
#adaptei pra ser horizontal e tentei fazer um ascii
#ultima opçao vai virar "confirmar ações na versao final
def print_menu(stdscr, selected_col_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx() #tela
    espaço = 3
    ar = 2
    botaotamanho = [len(col) + ar * 2 for col in menu]
    menutamanho = sum(botaotamanho) + espaço * (len(menu) - 1)
    x = (w - menutamanho) // 2
    y = h - 4
    for idx, col in enumerate(menu):
        botaolargura = botaotamanho[idx]
        stdscr.addstr(y+1, x, "┌" + "─" * (botaolargura - 2) + "┐") #aresta de cima
        text = col.center(botaolargura - 2) #texto
        if idx == selected_col_idx:
            stdscr.attron(curses.color_pair(1))
        stdscr.addstr(y + 2, x, "│" + text + "│") #borda
        if idx == selected_col_idx:
            stdscr.attroff(curses.color_pair(1))
        stdscr.addstr(y + 3, x, "└" + "─" * (botaolargura - 2) + "┘") #aresta de baixo
        x += botaolargura + espaço
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr):
    # Turn off cursor blinking
    curses.curs_set(0)
    # Color scheme for selected column
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    # Specify the current selected column
    current_col = 0
    # Print the menu
    print_menu(stdscr, current_col)
    while 1:
        key = stdscr.getch()
        if key == curses.KEY_LEFT and current_col > 0:
            current_col -= 1
        elif key == curses.KEY_RIGHT and current_col < len(menu) - 1:
            current_col += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            print_center(
                stdscr,
                "You selected '{}'".format(menu[current_col])
            )
            stdscr.getch()
            # If user selected last column, exit the program
            if current_col == len(menu) - 1:
                setfoo('gameon', 0)
                break
        print_menu(stdscr, current_col)


while f['gameon'] == 1:
    updater()
    if f['foo'] > 1 or f['foo'] <= 0:
        setfoo('foo', 1)
    if f['gamewin'] == 1:
        setfoo('gameon', 0)
    if f['turnosatuais'] <3:
        updater()
        setfoo('turnos', f['turnos']+1)
        #[coisas dentro do turno]
        setfoo('turnosatuais', f['turnosatuais'] + 1)
    setfoo('rods', f['rods']+1)
    curses.wrapper(main)

#criar função pra ler input e output
#criar cli bonitinha
#tabs 1 2 3 4 5 com ações de cada player, quando todas escolhidas, turno dos inimigos
#calculo e ajustes, repete


