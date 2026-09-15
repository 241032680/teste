#arrendondar pra cima
def ceil(a, b):
    return int(-(-a // b))
#ceil (5, 2)
#print (ceil (5, 2))
#dividir por 1 se só quiser arrendondar sem operação

#função de randomização
#Xn+1 = (aXn + c) mod mod (segundo a wikipedia)
#sem IA essa merda foi na raça

def lcg(Xn, a, c, m, n): 
    resultados = []
    for _ in range(n):
        Xn = (a * Xn + c) % m
        resultados.append(Xn)
    return resultados
def rand():
    z = s['z']
    y = 1
    t = (int(s['crio']) ^ int(s['sonar']) ^ int(s['grav']) ^ int(s['radio']) ^ s['escudo'])
    j = (int(s['crio']) & int(s['sonar']) & int(s['grav']) & int(s['radio']) & s['escudo'])
    k = (int(s['crio']) | int(s['sonar']) | int(s['grav']) | int(s['radio']) | s['escudo'])
    setstat('d', s['d'])
    if s['d']<0:
        setstat('d', ceil(s['d'], -1))
    setstat('a', s['a'] + int(s['crio']) + int(s['sonar']) + int(s['grav']) + int(s['radio']) + s['escudo'])
    setstat('b', s['b'] + int(s['crio']) + int(s['sonar']) + int(s['grav']) + int(s['radio']) + s['hp'])
    seedgen = lcg (((s['a']+s['d'])**2)&(s['d']), 1103515245, 12345+s['d'], (2**31), n=100)
    pos = lcg (s['b'], 1103515245, int(12345+((s['overclock']|s['sonar'])*(s['d'])^(s['d']**(s['direct'])))), (2**31+1), n=100)
    for _ in pos:
        y = len(str(_))
        z = (z+(s['z'])+y+modo+((s['btorp']%4)+1)%2048)
        if z <= 0:
            z = (lcg(ceil(z, -1), 1103515245, 12345+s['d']+s['a']+s['av']-k+j+t, (2**31), n=1)[0])
        setstat('z', ((z%997)+1))
    pos = (pos[z%100]%99)+1
    seed = int((seedgen[pos]%999998) +1)
    lista = lcg(seed+(s['bfront']-s['d']%6), 1103515245, 12345+s['turnos']+s['rods'], (2**31-1), n=100)
    f = lista[(pos%((seed%pos)+1)+1)]%(((s['a']*s['b'])%z)+1)
    #mais randomização
    seedgen = seed + (lcg(f, 1103515245, 12345+((y%8)+1), (2**16), n=1)[0])
    if f%10 > 4 or int(s['d']%64) > 22:
        setstat('d', (((s['a']|s['b'])<<1)%8092)+1)
        setstat('z', (s['a']+((s['b']^((y+1)//(s['torpedos']+1)))%1024)+1))
        setstat('b', (s['bvelmax']&s['bescudo']|s['btorp']%2048)+1)
        setstat('a', s['baae']+(z^y)+1)
    if [(z ^ y) and s['a']|s['b'] >= seedgen&pos] or seedgen<<(s['sonar']^s['grav']^s['hp']^(~s['baae'])) <= 69420:
        setstat('a', ((s['a']-69)%69)+1)
        setstat('b', ((s['b']-420)%69)+1)
        setstat('z', ((s['z']-67)%69)+1)
        setstat('d', ((s['d']-42)%69)+1)
    if  (s['d']<<1) < (int((s['z']>>5)) ** ((((~(s['bescudo'])+(s['direct'])>>1)))%3)+1):
        setstat('d', (((s['a']|s['velmax'])<<1)%8092)+1)
        setstat('z', (s['d']+((f^((s['bpilot']+1)*(s['butil']+1)))%1024)+1))
        setstat('b', (s['b']&s['escudo']|s['hp']%2048)+1)
    if s['a'] ^ s['b'] < 4096:
        setstat('a', s['a']+(s['a']^s['b'])+1)
        setstat('z', s['z']+((s['a']%255)+1))
        setstat('d', (((s['d']^y)%s['d'])+1))
    if f%10 in range(1, 4):
        setstat('d', s['d']+1)
        setstat('a', s['a']+3)
        setstat('b', s['b']+2)
        setstat('z', s['z']+ ((s['a'] ^ s['b'] ^ s['d'])+1))
    elif f%10 in range(4, 8):
        setstat('d', s['d']+2)
        setstat('a', s['a']+1)
        setstat('b', s['b']+3)
        setstat('z', s['z'] + ((s['a'] | s['b'] | s['d'])+1))
    elif f%10 in range(8, 10):
        setstat('d', s['d']+3)
        setstat('a', s['a']+2)
        setstat('b', s['b']+1)
        setstat('z', s['z'] + ((s['a'] & s['b'] & s['d'])+1))        
    elif f%10 == 0:
        setstat('d', (s['d']%512)+4)
        setstat('a', ((z*(int(s['crio'])+1) * int(s['sonar']) + int(s['grav']) + (int(s['radio'])))**((s['a']*s['b'])%999998)+1))
        setstat('b', ((((z+y+s['a']+s['b']+modo)&((s['b']+s['a'])*(int(s['sonar'])+1)))%255)+1))
        setstat('z', (s['z'] + (((((s['a'] & s['b'] & s['d'])+1) - ((~((s['a'] ^ s['b'] ^ s['d'])+1)))%1987)+1) + (((s['a']*s['b'])%32)+1))))
    else:
        setstat('d', 404)
        setstat('a', 101)
        setstat('b', 303)
    setstat('d', s['d']+1)  
    setstat('a', s['a']+1)
    setstat('b', s['b']+1)
    setstat('z', s['z']+1)
    return f ^ (f >> 16)

#stats
s = {}

def setstat(name, value):
    s[name] = value

#statsnave
#for x in ['torpedos', 'plasma', 'av', 'gas', 'aae', 'frontal', 'icss', 'bateria', 'cohm', 'hp', 'escudo', 'velmax', 'escudof', 'escudot', 'overclock', 'direct', 'modo']:
#    setstat(x, 0)

setstat('torpedos', 5)
setstat('plasma', 20)
setstat('av', 60)
setstat('gas', 50)
setstat('aae', 8)
setstat('frontal', 6)
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
setstat('turnos', 1)
setstat('rods', 1)

#buffs player
setstat('bmobil',0)
setstat('bmira',0)
setstat('bpercep',0)
setstat('bpilot', 0)
setstat('butil', 0)
setstat('btorp', 0)
setstat('baae', 0)
setstat('bfront', 0)
setstat('bvelmax',0)
setstat('brolls',0)
setstat('bcover',0)
setstat('bescudo',0)

#randomizador
setstat('d', 1)
setstat('a', 42)
setstat('b', 67)
setstat('z', 1)

#placeholders/pointers
setstat('foo', 1)
setstat('pesadoprop', 0)

#print(s['torpedos'], s['plasma'], s['av'], s['gas'], s['aae'], s['frontal'], s['icss'], s['bateria'], s['cohm'], s['hp'], s['escudo'])

#distribuição de escudo
#Padrão: Geração de Escudo Total = 10
#Frontal: Geração de Escudo Frontal x Traseiro = [15 , 5]
#Traseira: Geração de Escudo Frontal x Traseiro = [5 , 15]
#Overclocked: +5 Geração de Escudo, mas +¼ chance de fritar o Gerador por rodada utilizada (¼, ½ , ¾…)

def flip():
    if (s['overclock']) == 1:
        setstat ('overclock', int(0))
    elif (s['overclock']) == 0:
        setstat ('overclock', int(1))
    else:
        setstat('overclock', int(0))
    setdirect(s['direct'])
    setmodo(modo)
    return ()
def setdirect(direct):
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
    return direct
#print(s['overclock'])
#flip()
#print(s['overclock'])

#modos de distribuição de energia
def setmodo(modo):
    if modo == int(1):
        setstat('escudo', 10)
        setstat('velmax', 7)
        setstat('btorp', 0)
        setstat('baae', 0)
        setstat('bfront', 0)
        setstat('bpilot', 0)
        setstat('butil', 0)

    elif modo == int(2):
        setstat('escudo', 15)
        setstat('velmax', 5)
        setstat('btorp', -5)
        setstat('baae', -8)
        setstat('bfront', -6)
        setstat('bpilot', -1)
        setstat('butil', -1)
    elif modo == int(3):
        setstat('escudo', 9)
        setstat('velmax', 10)
        setstat('baae', -5)
        setstat('btorp', -5)
        setstat('bfront', -4)
        setstat('bpilot', 2)
        setstat('butil', -1)
    elif modo == int(4):
        setstat('escudo', 7)
        setstat('velmax', 6)
        setstat('baae', 6)
        setstat('btorp', 1)
        setstat('bfront', 4)
        setstat('bpilot', 0)
        setstat('butil', -1)
    elif modo == int(5):
        modo = 5
        setstat('escudo', 8)
        setstat('velmax', 6)
        setstat('baae', -3)
        setstat('btorp', 5 )
        setstat('bfront', -2)
        setstat('bpilot', 1)
        setstat('butil', 2)
    else:
        modo = setmodo(1)
    setstat('escudo', s['escudo'])
    setstat('modo', modo)
    setdirect(s['direct'])
    return modo

modo = setmodo(1)

def util(crio, sonar, radio, grav):
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
        setstat('brolls', -1)
        setstat('criodesmaio', 5)
        setstat('bvelmax', 0)
        setstat('baae', 4)
        setstat('bfront', 4)
        setstat('crio', crio)
        #return s['crio']
    if sonar == True or sonar == 1 or s['sonar']==1:
        print ("Sonar On")
        setstat('sonar', sonar)
        #return s['sonar']
    else:
        print ("Sonar Off")
        setstat('podeusartorpedo', True)
        setstat('bmira', -2)
        setstat('bpercep', -1)
        setstat('baae', 3)
        setstat('bfront', 1)
        setstat('bvelmax', 1)
        setstat('sonar', sonar)
        #return s['sonar']
    if radio == True or radio == 1 or s['radio']==1:
        print ("Radio On")
        setstat('radio', radio)
        #return s['radio']
    else:
        print ("Radio Off")
        setstat('podeusarcomms', False)
        setstat('bvelmax', 1)
        setstat('radio', radio)
        #return s['radio']
    if grav == True or grav == 1 or s['grav']==1:
        print ("Gravity On")
        setstat('grav', grav)
        #return s['grav']
    else:
        print ("Gravity Off")
        setstat('bmobil', -2)
        setstat('bcover', -2)
        setstat('bmira', -1)
        setstat('bescudo', 2)
        setstat('baee', 1)
        setstat('bfront', 1)
        setstat('grav', grav)
        #return s['grav']

#util(1,0,1,0)
#util(0, sonar=s['sonar'], radio=s['radio'], grav=s['grav'])

#print(s['bmobil'], s['bmira'], s['bpercep'], s['bpilot'],s['butil'], s['btorp'], s['baae'], s['bfront'], s['bvelmax'], s['brolls'],s['bcover'], s['bescudo'],s['podeusartorpedo'], s['podeusarcomms'])

#rodada: cada jogador e inimmigo tem seu turno
#turno de cada jogador: 3 ações
#turno de cada inimigo: instantâneo
#ordem de turnos: piloto, copiloto, engenheiro, atirador, atirador aae, ajuste de distância, inimigos

def hitnave(intensidade):
    c = 0 + s['foo']
    y = "O casco"
    o = rand()
    p = (rand()//rand()) << 2
    q = (rand()*rand()) >> 2
    r = (rand()^rand()&rand()|rand())
    if o%10 > 5:
        setstat('d', int(s['d']+((rand()%127)+1)))
    else:
        setstat('d', int(s['d']-((rand()%127)+1)))
    if q%10 > 6:
        setstat('a', int(s['a']*((rand()%63)+1)))
    else:
        setstat('a', int(s['a']//((rand()%63+1))))
    if p%10 > 6:
        setstat('b', int(s['b']**((rand()%7)+1)))
    else:
        setstat('b', int(s['b']**((1/((rand()%7)+1)))))
    if r%10 > 4: 
        setstat('z', int(s['z']+((r%10)+1)*((rand()%31)+1)))
    else:
        setstat('z', int(s['z']-((r%10)+1)*((rand()%31)+1)))
    match intensidade:
        case"L" | "l": #leve
            setstat('hp', s['hp'] -5)
            z = str("leve")
            a = (rand()%12)
            match a:
                case 0:
                    util(0, sonar=s['sonar'], radio=s['radio'], grav=s['grav'])
                    setstat('danocrio', True)
                    setstat('brolls', s['brolls'] - 1)
                    y = "Criogênicos"
                case 1:
                    setstat('danograv', True)
                    util(crio=s['crio'], sonar=s['sonar'], radio=s['radio'], grav=0)
                    y = "Gerador de Gravidade"
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    pass
                case 9:
                    pass
                case 10:
                    pass
                case 11:
                    pass

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
                    if k == 6
                        setstat('novoprop', 1)
                    setstat('bvelmax', (s['bvelmax']) -1(*s['numprop']+s['pesadoprop']))
                    y = "Propulsor"
                case 7|9:
                    pass
        case "M" | "m":
            setstat('hp', s['hp'] -8)
            z = str("médio")
            c = 0
        case _:
            setstat('hp', s['hp'] -8)
            z = ""
            c += 1
            #setstat('foo', s['foo'] + 1)
    if c < 2:
        print(f"{y} foi atingido por um tiro {z}!")
    if intensidade == "r" or intensidade == "R":
        b = rand()%3
        y = "Algo"
        z = ""
        c = 0
        if b == 0:
            hitnave('l')
            setstat('foo', 1)
        elif b == 1:
            hitnave('m')
            setstat('foo', 1)
        elif b == 2:
            hitnave('p')
            setstat('foo', 1)
        setstat('foo', 1)
        

#ações players
def conserto(lugar):
    if lugar == 'prop':
        setstat('numprop', s['numprop'] -1)
        setstat('bvelmax', s['bvelmax'] + (1*(1+s['pesadoprop'])))
        if s['numprop'] <= 0:
            setstat('danoprop', False)
    if lugar == 'grav':
        setstat('bmobil', s['bmobil']+s['rodssemgrav']*2)
        setstat('bcover', s['bcover']+s['rodssemgrav']*1)
        setstat('rodssemgrav', 0)
        setstat('danograv', False)
    if lugar == 'crio':
        setstat('brolls', s['brolls'] + 1)
        setstat('danocrio', False)


#while s['gameon'] == 1:
if s['foo'] > 1 or s['foo'] <= 0:
    setstat('foo', 1)



#end of round





def danos():
    rodssemgrav = max(s['rodssemgrav'], 5)
    danograv = s['danograv']
    danocrio = s['danocrio']
    danocomms = s['danocomms']
    if danograv == True:
        setstat('rodssemgrav', s['rodssemgrav'] +1)
        setstat('bmobil', (s['bmobil']) -2)
        setstat('bcover', (s['bcover']) -1)
        print("Gerador de Gravidade danificado!")
    desmaio = s['criodesmaio']
    if danocrio == True or s['crio'] == 0 or s['crio'] == False:
        setstat('criodesmaio', s['criodesmaio'] -1)
        print(f"Sistema de Criogenia desativado! \n Jogadores desmaiarão em {desmaio} rodadas!")
    if danocrio == False:
        if desmaio < 5:
        setstat('criodesmaio', min(desmaio - int(~int(danocrio)), 5))
    if danocomms == True:
        setstat('podeusarcomms', False)
        print("Sistema de Comunicações danificado!")
    if danocomms == False:
        setstat('podeusarcomms', True)
    if danomotor == True:
        if falhamotor == True:
            pass
        else:
            pass
    if danopropulsores == True:
        if novoprop == 1:
            setstat('numprop', s['numprop']+1)
            print('Um novo propulsor foi danificado!')
            setstat('novoprop', 0)
        print("Propulsores danificados!")