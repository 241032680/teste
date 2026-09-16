#arrendondar pra cima
def ceil(a, b):
    return int(-(-a // b))
#ceil (5, 2)
#print (ceil (5, 2))
#dividir por 1 se só quiser arrendondar sem operação

#função de randomização
#Xn+1 = (aXn + c) mod mod (segundo a wikipedia)
#sem IA essa bomba foi na raça

r = {}
def setrand(num, val)
    r[num] = val
def lcg(Xn, a, c, m, n): 
    resultados = []
    for _ in range(n):
        Xn = (a * Xn + c) % m
        resultados.append(Xn)
    return resultados
def rand():
    z = r['z']
    y = 1
    t = (int(s['crio']) ^ int(s['sonar']) ^ int(s['grav']) ^ int(s['radio']) ^ s['escudo'])
    j = (int(s['crio']) & int(s['sonar']) & int(s['grav']) & int(s['radio']) & s['escudo'])
    k = (int(s['crio']) | int(s['sonar']) | int(s['grav']) | int(s['radio']) | s['escudo'])
    setstat('d', r['d'])
    if r['d']<0:
        setstat('d', ceil(r['d'], -1))
    setstat('a', r['a'] + int(s['crio']) + int(s['sonar']) + int(s['grav']) + int(s['radio']) + s['escudo'])
    setstat('b', r['b'] + int(s['crio']) + int(s['sonar']) + int(s['grav']) + int(s['radio']) + s['hp'])
    seedgen = lcg (((r['a']+r['d'])**2)&(r['d']), 1103515245, 12345+r['d'], (2**31), n=100)
    pos = lcg (r['b'], 1103515245, int(12345+((s['overclock']|s['sonar'])*(r['d'])^(r['d']**(s['direct'])))), (2**31+1), n=100)
    for _ in pos:
        y = len(str(_))
        z = (z+(r['z'])+y+modo+((b['btorp']%4)+1)%2048)
        if z <= 0:
            z = (lcg(ceil(z, -1), 1103515245, 12345+r['d']+r['a']+s['av']-k+j+t, (2**31), n=1)[0])
        setstat('z', ((z%997)+1))
    pos = (pos[z%100]%99)+1
    seed = int((seedgen[pos]%999998) +1)
    lista = lcg(seed+(b['bfront']-r['d']%6), 1103515245, 12345+s['turnos']+s['rods'], (2**31-1), n=100)
    f = lista[(pos%((seed%pos)+1)+1)]%(((r['a']*r['b'])%z)+1)
    #mais randomização
    seedgen = seed + (lcg(f, 1103515245, 12345+((y%8)+1), (2**16), n=1)[0])
    if f%10 > 4 or int(r['d']%64) > 22:
        setstat('d', (((r['a']|r['b'])<<1)%8092)+1)
        setstat('z', (r['a']+((r['b']^((y+1)//(s['torpedos']+1)))%1024)+1))
        setstat('b', (b['bvelmax']&b['bescudo']|b['btorp']%2048)+1)
        setstat('a', b['baae']+(z^y)+1)
    if [(z ^ y) and r['a']|r['b'] >= seedgen&pos] or seedgen<<(s['sonar']^s['grav']^s['hp']^(~b['baae'])) <= 69420:
        setstat('a', ((r['a']-69)%69)+1)
        setstat('b', ((r['b']-420)%69)+1)
        setstat('z', ((r['z']-67)%69)+1)
        setstat('d', ((r['d']-42)%69)+1)
    if  (r['d']<<1) < (int((r['z']>>5)) ** ((((~(b['bescudo'])+(s['direct'])>>1)))%3)+1):
        setstat('d', (((r['a']|s['velmax'])<<1)%8092)+1)
        setstat('z', (r['d']+((f^((b['bpilot']+1)*(b['butil']+1)))%1024)+1))
        setstat('b', (r['b']&s['escudo']|s['hp']%2048)+1)
    if r['a'] ^ r['b'] < 4096:
        setstat('a', r['a']+(r['a']^r['b'])+1)
        setstat('z', r['z']+((r['a']%255)+1))
        setstat('d', (((r['d']^y)%r['d'])+1))
    if f%10 in range(1, 4):
        setstat('d', r['d']+1)
        setstat('a', r['a']+3)
        setstat('b', r['b']+2)
        setstat('z', r['z']+ ((r['a'] ^ r['b'] ^ r['d'])+1))
    elif f%10 in range(4, 8):
        setstat('d', r['d']+2)
        setstat('a', r['a']+1)
        setstat('b', r['b']+3)
        setstat('z', r['z'] + ((r['a'] | r['b'] | r['d'])+1))
    elif f%10 in range(8, 10):
        setstat('d', r['d']+3)
        setstat('a', r['a']+2)
        setstat('b', r['b']+1)
        setstat('z', r['z'] + ((r['a'] & r['b'] & r['d'])+1))        
    elif f%10 == 0:
        setstat('d', (r['d']%512)+4)
        setstat('a', ((z*(int(s['crio'])+1) * int(s['sonar']) + int(s['grav']) + (int(s['radio'])))**((r['a']*r['b'])%999998)+1))
        setstat('b', ((((z+y+r['a']+r['b']+modo)&((r['b']+r['a'])*(int(s['sonar'])+1)))%255)+1))
        setstat('z', (r['z'] + (((((r['a'] & r['b'] & r['d'])+1) - ((~((r['a'] ^ r['b'] ^ r['d'])+1)))%1987)+1) + (((r['a']*r['b'])%32)+1))))
    else:
        setstat('d', 404)
        setstat('a', 101)
        setstat('b', 303)
    setstat('d', r['d']+1)  
    setstat('a', r['a']+1)
    setstat('b', r['b']+1)
    setstat('z', r['z']+1)
    return f ^ (f >> 16)

#função seno
pi = 3.141592653589793
def sin(x): #formula roubada da wikipedia, adaptada
    x = (x + pi)%(2*pi) - pi
    if x > pi/2: x = pi - x
    elif x < -pi/2: x = -pi - x
    y = x**2
    return x*(1 - y/6*(1 - y/20*(1 - y/42*(1 - y/72))))

#função de média:
def avg(list):
  l = list.copy()
  average = ((sum(l) / float(len(l))))
  return (int(average * 100))/100 #2 casas decimais

#stats
s = {}
f = {}
n = {}

#começando a separar por causa do display/GUI, talvez desnecessário com método...
def setstat(nome, valor):
    s[nome] = valor
def setfoo(foo, valor):
    f[foo] = valor
def setbuff(buff, valor):
    b[buff] = valor
def setbase(stat, valor):
    n[stat] = valor


#stats nave

setstat('torpedos', 5)
setstat('plasma', 20)
setstat('av', 60)
setstat('gas', 50)
setstat('aaebase', 8)
setstat('frontalbase', 6)
setstat('icss', 120)
setstat('bateria', 100)
setstat('cohm', 70)
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
setstat('criodesmaio', 5)
setstat('depressurização', 3)
setstat('hangarselado', False)

#buffs player
setbuff('bmobil',0)
setbuff('bmira',0)
setbuff('bpercep',0)
setbuff('bpilot', 0)
setbuff('butil', 0)
setbuff('btorp', 0)
setbuff('baae', 0)
setbuff('bfront', 0)
setbuff('bvelmax',0)
setbuff('brolls',0)
setbuff('bcover',0)
setbuff('bescudo',0)

#stats players
setstat('pilotbase', 1)
setstat('mobil',1)
setstat('velmax',1)
setstat('rollsbase',1)
setstat('coverbase',1)
setstat('mirabase',1)
setstat('percepbase',1)
setstat('utilbase', 1)

#controles de jogo
setstat('turnos', 1)
setstat('rods', 1)

#randomizador
setrand('d', 1)
setrand('a', 42)
setrand('b', 67)
setrand('z', 1)

#placeholders/modificadores
setfoo('foo', 1)
setstat('pesadoprop', 0)
setstat('numasas', 1) #numero de asas DANIFICADAS, numero de asas na nave é 4
setstat('numprops', 1) #mesma coisa das asas mas pra propulsores

#print(s['torpedos'], s['plasma'], s['av'], s['gas'], s['aaebase'], s['frontalbase'], s['icss'], s['bateria'], s['cohm'], s['hp'], s['escudo'])

def updater(): #update stats
    setstat('frontal', s['frontalbase']+b['bfront'])
    setstat('aaebase', s['aaebase']+b['baae'])
    setstat('velmax', b['bvelmax']+b['bvelmax'])
    setbuff('btorp', s['torpbase'] + b['btorp'])
    setstat('util', s['utilbase'] + b['butil'])
    setstat('pilot', s['pilotbase'] + b['bpilot'])
    setstat('rolls', s['rollsbase']+ s['brolls'])
    setstat('cover', s['coverbase'] + b['bcover'])
    
#distribuição de escudo
#Padrão: Geração de Escudo Total = 10
#frontal: Geração de Escudo frontal x Traseiro = [15 , 5]
#Traseira: Geração de Escudo frontal x Traseiro = [5 , 15]
#Overclocked: +5 Geração de Escudo, mas +¼ chance de fritar o Gerador por rodada utilizada (¼, ½ , ¾…)

def flip(): #ativar/desativar overclock
    if (s['overclock']) == 1:
        setstat ('overclock', int(0))
    elif (s['overclock']) == 0:
        setstat ('overclock', int(1))
    else:
        setstat('overclock', int(0))
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
        setbuff('bvelmax', 0)
        setbuff('btorp', 0)
        setbuff('baae', 0)
        setbuff('bfront', 0)
        setbuff('bpilot', 0)
        setbuff('butil', 0)
    elif modo == int(2): #escudo
        setstat('escudo', 15)
        setbuff('bvelmax', -2)
        setbuff('btorp', -5)
        setbuff('baae', -8)
        setbuff('bfront', -6)
        setbuff('bpilot', -1)
        setbuff('butil', -1)
    elif modo == int(3): #propulsores
        setstat('escudo', 9)
        setbuff('bvelmax', 3)
        setbuff('baae', -5)
        setbuff('btorp', -5)
        setbuff('bfront', -4)
        setbuff('bpilot', 2)
        setbuff('butil', -1)
    elif modo == int(4): #torretas
        setstat('escudo', 7)
        setbuff('bvelmax', -1)
        setbuff('baae', 6)
        setbuff('btorp', 1)
        setbuff('bfront', 4)
        setbuff('bpilot', 0)
        setbuff('butil', -1)
    elif modo == int(5): #utilitários
        modo = 5
        setstat('escudo', 8)
        setbuff('bvelmax', -1)
        setbuff('baae', -3)
        setbuff('btorp', 5 )
        setbuff('bfront', -2)
        setbuff('bpilot', 1)
        setbuff('butil', 2)
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
        setstat('crio', crio)
        #return s['crio']
    else:
        print ("Crio Off")
        setbuff('brolls', -1)
        setbuff('bvelmax', 0)
        setbuff('baae', 4)
        setbuff('bfront', 4)
        setstat('crio', crio)
        #return s['crio']
    if sonar == True or sonar == 1 or s['sonar']==1:
        print ("Sonar On")
        setstat('sonar', sonar)
        #return s['sonar']
    else:
        print ("Sonar Off")
        setstat('podeusartorpedo', True)
        setbuff('bmira', -2)
        setbuff('bpercep', -1)
        setbuff('baae', 3)
        setbuff('bfront', 1)
        setbuff('bvelmax', 1)
        setstat('sonar', sonar)
        #return s['sonar']
    if radio == True or radio == 1 or s['radio']==1:
        print ("Radio On")
        setstat('radio', radio)
        #return s['radio']
    else:
        print ("Radio Off")
        setstat('podeusarcomms', False)
        setbuff('bvelmax', 1)
        setstat('radio', radio)
        #return s['radio']
    if grav == True or grav == 1 or s['grav']==1:
        print ("Gravity On")
        setstat('grav', grav)
        #return s['grav']
    else:
        print ("Gravity Off")
        setbuff('bmobil', -2)
        setbuff('bcover', -2)
        setbuff('bmira', -1)
        setbuff('bescudo', 2)
        setstat('baee', 1)
        setbuff('bfront', 1)
        setstat('grav', grav)
        #return s['grav']

#inventários

#armazém (18 slots)
#gera 18 itens de valor aleatório, que definem o valor da recomepensa no final do jogo
#quanto mais itens chegarem no checkpoint final, melhor o score
#varias mecanicas fazem os itens perderem valor

a = {}
c = {}
m = {}
w = {}
def armazém(nome, valor):
    a[nome.upper()] = valor

armazém('caixa de madeira', 90)
#medbay (12 slots)
#itens de cura
print(a)
print(s)
def medbay(nome, valor, tipo)
    m[nome.capitalize()] = valor
    m['Tipo:'] = tipo.capitalize()

#cozinha (12 slots)
#itens de cura, rango e alguns valiosos

def cozinha(nome, valor, tipo)
    c[nome.capitalize()] = valor
    c['Tipo:'] = tipo.capitalize()

#sala comum (6 slots)
#itens pessoais de players, o que não couber em outros espaçoes

def salacomum(nome, valor, tipo)
    w[nome.capitalize()] = valor
    w['Tipo:'] = tipo.capitalize()



#utilbase(1,0,1,0)
#utilbase(0, sonar=s['sonar'], radio=s['radio'], grav=s['grav'])

#print(b['bmobil'], b['bmira'], b['bpercep'], b['bpilot'],b['butil'], b['btorp'], b['baae'], b['bfront'], b['bvelmax'], s['brolls'],b['bcover'], b['bescudo'],s['podeusartorpedo'], s['podeusarcomms'])

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
            if 
            match a:
                case 0:
                    utilbase(0, sonar=s['sonar'], radio=s['radio'], grav=s['grav'])
                    setstat('danocrio', True)
                    setbuff('brolls', s['brolls'] - 1)
                    y = "Criogênicos"
                case 1:
                    setstat('danograv', True)
                    utilbase(crio=s['crio'], sonar=s['sonar'], radio=s['radio'], grav=0)
                    y = "Gerador de Gravidade"
                case 2:
                    setstat('genescudo', False)
                    y = "Gerador de Escudo"
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
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
                    setbuff('bvelmax', (b['bvelmax']) -(1*(s['numprops']+s['pesadoprop'])))
                    y = "Propulsor"
                case 11:
                    setstat('danoasa', True)
                    k = rand()%8
                    if k == 8 and s['numasas']<4:
                        setstat('novaasa', 1)
                    setbuff('bpilot', (b['bpilot']) -(1*(s['numasas']+s['pesadoasa']+s['medioasa'])))
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
                    setstat('pesadoprop', s['pesadoprop']+ 1)
                    setstat('danopropulsores', True)
                    k = rand()%6
                    if k == 6 and s['numprops'] < 9:
                        setstat('novoprop', 1)
                    setbuff('bvelmax', (b['bvelmax']) -(1*(s['numprops']+s['pesadoprop'])))
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
                    if k == 6 and s['numasas']<4:
                        setstat('novaasa', 1)
                    setbuff('bpilot', (b['bpilot']) -(1*(s['numasas']+s['pesadoasa']+s['medioasa'])))
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
    #entropia pro randomizador
    o = rand()
    p = (rand()//rand()) << 2
    q = (rand()*rand()) >> 2
    r = (rand()^rand()&rand()|rand())
    if o%10 > 5:
        setstat('d', int(r['d']+((rand()%127)+1)))
    else:
        setstat('d', int(r['d']-((rand()%127)+1)))
    if q%10 > 6:
        setstat('a', int(r['a']*((rand()%63)+1)))
    else:
        setstat('a', int(r['a']//((rand()%63+1))))
    if p%10 > 6:
        setstat('b', int(r['b']**((rand()%7)+1)))
    else:
        setstat('b', int(r['b']**((1/((rand()%7)+1)))))
    if r%10 > 4: 
        setstat('z', int(r['z']+((r%10)+1)*((rand()%31)+1)))
    else:
        setstat('z', int(r['z']-((r%10)+1)*((rand()%31)+1)))

#ações players
def conserto(lugar):
    match lugar:
        case 'prop':
            setstat('numprops', s['numprops'] -1)
            setbuff('bvelmax', b['bvelmax'] + (1*(1+s['pesadoprop'])))
            if s['numprops'] <= 0:
                setstat('danoprop', False)
        case 'grav':
            setbuff('bmobil', b['bmobil']+s['rodssemgrav']*2)
            setbuff('bcover', b['bcover']+s['rodssemgrav']*1)
            setstat('rodssemgrav', 0)
            setstat('danograv', False)
        case 'crio':
            setbuff('brolls', s['brolls'] + 1)
            setstat('danocrio', False)
        case 'geradorescudo':
            setstat('genescudo', True)
        case 'comms':
            setstat('podeusarcomms', True)


#while s['gameon'] == 1:
if s['foo'] > 1 or s['foo'] <= 0:
    setfoo('foo', 1)



#end of round
def genescudo():
    if s['genescudo'] == True:
        setstat('escudoefetivof', s['escudof'] + b['bescudo'])
        setstat('escudoefetivot', s['escudot'] + b['bescudo'])

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
            setstat('numasas', max(s['numasas']+1, 4))
            print('Uma nova asa foi danificada!')
            setstat('novoprop', 0)
        if s['numasas'] == 1:
            print("Asa Danificada!")
        elif s['numasas'] > 1:
            print("Asas danificadas!")
    if danoarmazém == True:
        armazém.pop(rand%18)



#inimigo, falta fazer a função

i = {
  "1": {
  "tipo": "leve",
  "hp" : int((10 + (sin(random.randint(0, 9999)))*2.22) + 0.5),
  "velocidade": 6,
  "mísseis" : rand()%2
  }
}


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