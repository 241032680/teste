
#stats
s = {}

def setstat(name, value):
    s[name] = value

#statsnave
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

#buffs player
setstat('bmobil',0)
setstat('bmira',0)
setstat('bpercep',0)

#print(s['torpedos'], s['plasma'], s['av'], s['gas'], s['aae'], s['frontal'], s['icss'], s['bateria'], s['cohm'], s['hp'], s['escudo'])

#modos de distribuição de energia
def setmodo(modo):
    if modo == int(1):
        setstat('escudo', 10)
        setstat('velmax', 7)
    elif modo == int(2):
        setstat('escudo', 15)
        setstat('velmax', 5)
        setstat('aae', s['aae'] - 8)
        setstat('torpedos', s['torpedos'] - 5)
    elif modo == int(3):
        setstat('escudo', 9)
        setstat('velmax', 10)
        setstat('aae', s['aae'] - 5)
        setstat('torpedos', s['torpedos'] - 5)
    elif modo == int(4):
        setstat('escudo', 7)
        setstat('velmax', 6)
        setstat('aae', s['aae'] + 6)
        setstat('torpedos', s['torpedos'] + 1)
    elif modo == int(5):
        modo = 5
        setstat('escudo', 8)
        setstat('velmax', 6)
        setstat('aae', s['aae'] - 3)
        setstat('torpedos', s['torpedos'] +5 )
    else:
        modo = setmodo(1)
    setstat('escudo', s['escudo'])
    return modo

#modo = setmodo(1)
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
    return ()
def setdirect(direct):
    if (direct) == 1:
        setstat ('escudof', int((s['escudo'] + (5*s['overclock']))))
        setstat ('escudot', int((s['escudo'] + (5*s['overclock']))))
    elif (direct) == 2:
        setstat ('escudof', int((s['escudo'] + (5*s['overclock']))*1.5))
        setstat ('escudot', int((s['escudo'] + (5*s['overclock']))*0.5))
    elif (direct) == 3:
        setstat ('escudof', int((s['escudo'] + (5*s['overclock']))*0.5))
        setstat ('escudot', int((s['escudo'] + (5*s['overclock']))*1.5))
    else:
        setstat ('escudof', int(s['escudo']))
        setstat ('escudot', int(s['escudo']))
    setstat('direct', direct)
    return direct
#print(s['overclock'])
#flip()
#print(s['overclock'])

#setmodo(2)
#setdirect(3)
#print(s['escudof'], s['escudot'])
#flip()
#print(s['escudof'], s['escudot'])

