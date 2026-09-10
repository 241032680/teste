#arrendondar pra cima
def ceil(a, b):
    return int(-(-a // b))
#ceil (5, 2)
#print (ceil (5, 2))
#dividir por 1 se só quiser arrendondar sem operação


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
setstat('grav', 1)
setstat('sonar', 1)
setstat('radio', 1)
setstat('crio', 1)
setstat('podeusartorpedo', True)
setstat('podeusarcomms', True)

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
#print(modo, s['escudo'])
#modo = setmodo(3)
#print(modo, s['escudo'])
#modo = setmodo(5)
#print(modo, s['escudo'])
#modo = setmodo(90)
#print(modo, s['escudo'])
#modo = setmodo(-1)
#print(modo, s['escudo'])
#modo = setmodo(3.5)
#print(modo, s['escudo'])


#print("escudof:", s['escudof'], "escudot:", s['escudot'], "escudo:", s['escudo'], "overclock:", s['overclock'], "direct:", s['direct'], "modo:", s['modo'])
#setmodo(2)
#setdirect(3)
#print("escudof:", s['escudof'], "escudot:", s['escudot'], "escudo:", s['escudo'], "overclock:", s['overclock'], "direct:", s['direct'], "modo:", s['modo'])
#flip()
#print("escudof:", s['escudof'], "escudot:", s['escudot'], "escudo:", s['escudo'], "overclock:", s['overclock'], "direct:", s['direct'], "modo:", s['modo'])
#modo = setmodo(3)
#print("escudof:", s['escudof'], "escudot:", s['escudot'], "escudo:", s['escudo'], "overclock:", s['overclock'], "direct:", s['direct'], "modo:", s['modo'])
#setdirect(2)
#flip()
#print("escudof:", s['escudof'], "escudot:", s['escudot'], "escudo:", s['escudo'], "overclock:", s['overclock'], "direct:", s['direct'], "modo:", s['modo'])
#setmodo(4)
#flip()
#setdirect(1)
#print("escudof:", s['escudof'], "escudot:", s['escudot'], "escudo:", s['escudo'], "overclock:", s['overclock'], "direct:", s['direct'], "modo:", s['modo'])
#setdirect(3)
#flip()
#setmodo(5)
#print("escudof:", s['escudof'], "escudot:", s['escudot'], "escudo:", s['escudo'], "overclock:", s['overclock'], "direct:", s['direct'], "modo:", s['modo'])

#for modo in range(6):
#    modo = setmodo(modo)
#    #for direct in range(4):
#        #direct = setdirect(direct)
#    if modo > 5:
#        break
#    print("escudof:", s['escudof'], "escudot:", s['escudot'], "escudo:", s['escudo'], "overclock:", s['overclock'], "direct:", s['direct'], "modo:", s['modo'])

def util(crio, sonar, radio, grav):
    if crio == True:
        print ("Crio On")
        setstat('crio', 1)
        #return s['crio']
    else:
        print ("Crio Off")
        setstat('brolls', -1)
        setstat('criodesmaio', 5)
        setstat('bvelmax', 0)
        setstat('baae', 4)
        setstat('bfront', 4)
        setstat('crio', 0)
        #return s['crio']
    if sonar == True:
        print ("Sonar On")
        setstat('sonar', 1)
        #return s['sonar']
    else:
        print ("Sonar Off")
        setstat('podeusartorpedo', True)
        setstat('bmira', -2)
        setstat('bpercep', -1)
        setstat('baae', 3)
        setstat('bfront', 1)
        setstat('bvelmax', 1)
        setstat('sonar', 0)
        #return s['sonar']
    if radio == True:
        print ("Radio On")
        setstat('radio', 1)
        #return s['radio']
    else:
        print ("Radio Off")
        setstat('podeusarcomms', False)
        setstat('bvelmax', 1)
        setstat('radio', 0)
        #return s['radio']
    if grav == True:
        print ("Gravity On")
        setstat('grav', 1)
        #return s['grav']
    else:
        print ("Gravity Off")
        setstat('bmobil', -2)
        setstat('bcover', -2)
        setstat('bmira', -1)
        setstat('bescudo', 2)
        setstat('baee', 1)
        setstat('bfront', 1)
        setstat('grav', 0)
        #return s['grav']

util(1,0,1,0)
print(s['bmobil'], s['bmira'], s['bpercep'], s['bpilot'],s['butil'], s['btorp'], s['baae'], s['bfront'], s['bvelmax'], s['brolls'],s['bcover'], s['bescudo'],s['podeusartorpedo'], s['podeusarcomms'])

#rodada: cada jogador e inimmigo tem seu turno
#turno de cada jogador: 3 ações
#turno de cada inimigo: instantâneo
#ordem de turnos: piloto, copiloto, engenheiro, atirador, atirador aae, ajuste de distância, inimigos

def hitnave(intensidade):
    if intensidade == "L" or intensidade == "l": #leve
        setstat('hp', s['hp'] -5)

    elif intensidade == "P" or intensidade == "p": #pesado
        setstat('hp', s['hp'] -12)
    else:
        setstat('hp', s['hp'] -8)

#função de randomização
#Xn+1 = (aXn + c) mod mod

def lcg(Xn, a, c, m, n):
    resultados = []
    for _ in range(n):
        Xn = (a * Xn + c) % m
        resultados.append(Xn)
    return resultados
setstat('d', 1)
setstat('a', 42)
setstat('b', 67)
setstat('z', 1)
def rand():
    z = s['z']
    y = 1
    t = (int(s['crio']) ^ int(s['sonar']) ^ int(s['grav']) ^ int(s['radio']) ^ s['escudo'])
    j = (int(s['crio']) & int(s['sonar']) & int(s['grav']) & int(s['radio']) & s['escudo'])
    k = (int(s['crio']) | int(s['sonar']) | int(s['grav']) | int(s['radio']) | s['escudo'])
    setstat('d', s['d'])
    if s['d']<0:
        setstatat('d', ceil(s['d'], -1))
    setstat('a', s['a'] + int(s['crio']) + int(s['sonar']) + int(s['grav']) + int(s['radio']) + s['escudo'])
    setstat('b', s['b'] + int(s['crio']) + int(s['sonar']) + int(s['grav']) + int(s['radio']) + s['hp'])
    seedgen = lcg (((s['a']+s['d'])**2)/(s['d']), 1103515245, 12345+s['d'], (2**31)-1, n=100)
    pos = lcg (s['b'], 1103515245, int(12345+((s['overclock']|s['sonar'])*(s['d'])/(s['d']**(s['direct'])))), (2**31)-1, n=100)
    for _ in pos:
        y = len(str(_)) + t
        z = (z+(s['z'])+y+modo+((s['btorp']%4)+1)%2048)
        if z <= 0:
            z = (lcg(ceil(z, -1), 1103515245, 12345+s['d']+s['a']+s['av'], (2**31)-1, n=1)[0])
        setstat('z', ((z%20)+1))
    pos = (pos[z%100]%99)+1
    #print(f'pos: {pos}')
    seed = int((seedgen[pos]%999998) +1)
    #print(f'seed: {seed}')
    lista = lcg(seed+(s['bfront']-s['d']%6), 1103515245, 12345, (2**31)-1, n=100)
    f = lista[(pos%((seed%pos)+1)+1)]%(((s['a']*s['b'])%z)+1)
    #mais randomização
    seedgen = seed + (lcg(f, 1103515245, 12345+((y%8)+1), (2**16)-1, n=1)[0])
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
    print(f'f: {f}')
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
        setstat('b', ((((z+y+s['a']+s['b']+modo)**((s['b']+s['a'])*(int(s['sonar'])+1)))%255)+1))
        setstat('z', (s['z'] + (((((s['a'] & s['b'] & s['d'])+1) - ((~((s['a'] ^ s['b'] ^ s['d'])+1)))%1987)+1) + (((s['a']*s['b'])%32)+1))))
    else:
        setstat('d', 404)
        setstat('a', 101)
        setstat('b', 303)
    print (f'{s['a']},{s['b']}, {s['d']}, {s['z']}')
    setstat('d', s['d']+1)  
    setstat('a', s['a']+1)
    setstat('b', s['b']+1)
    setstat('z', s['z']+1)    
    return f

for h in range(1, 50):
    rand()