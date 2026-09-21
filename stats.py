import funções_e_macros.py
import setup.py

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
