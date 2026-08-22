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

#buffs player
setstat('bmobil',0)
setstat('bmira',0)
setstat('bpercep',0)
setstat('bpilot', 0)
setstat('butil', 0)
setstat('btorp', 0)
setstat('baae', 0)
setstat('bfront', 0)

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
        setstat('baae',  -3)
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
print(modo, s['escudo'])
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
    else:
        print ("Crio Off")
    if sonar == True:
        print ("Sonar On")
    else:
        print ("Sonar Off")
    if radio == True:
        print ("Radio On")
    else:
        print ("Radio Off")
    if grav == True:
        print ("Gravity On")
    else:
        print ("Gravity Off")

