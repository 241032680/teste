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

f = {}
def setfoo(foo, valor): #seta as flags do jogo
    f[foo] = valor

#randomizador
setrand('d', 1)
setrand('a', 42)
setrand('b', 67)
setrand('z', 1)

#controles de jogo
setfoo('gameon', True)
setfoo('gamewin', False)
setfoo('hp', 80) #valores provisórios do MVP
setfoo('escudo', 20)
setfoo('escudomax', 20)
setfoo('rods', 1)
setfoo('acoes', 3)
setfoo('desvio', False)
setfoo('mensagem', 'Escolha uma ação.')
setfoo('mensagem_inimigos', '')

#inimigo
inimigos = {}
proximo_inimigo = 0
def criarinimigo(tipo):
    global proximo_inimigo
    qthp =      40 if tipo=="medio" else 80   if tipo=="pesado" else 0
    qtesc =      5 if tipo=="medio" else 10   if tipo=="pesado" else 0
    v =       4.56 if tipo=="medio" else 6.66 if tipo=="pesado" else 1.5
    n = proximo_inimigo
    proximo_inimigo += 1
    inimigos[f'Inimigo {(n+1)}'] = {
    "tipo": tipo,
    "hp": int(30 + qthp + sin(rand()) * 6.66),
    "escudo": max(0, int(10 + qtesc + sin(rand()) * v)) if tipo != "leve" or rand()%2 else 0,
    "marcado": False
    }

criarinimigo("leve")
criarinimigo("medio")
criarinimigo("pesado")

#dano do inimigo
def hitnave(intensidade):
    intensidade = intensidade.lower()
    danos_base = {'l': 5, 'm': 8, 'p': 12}
    dano = danos_base[intensidade]
    if f['desvio']: dano = (dano+1)//2
    if f['escudo'] > 0:
        dano = min(f['escudo'], dano)
        f['escudo'] -= dano
        return f'Escudo absorveu {dano} de dano'
    dano = min(f['hp'], dano)
    f['hp'] -= dano
    return f'Casco recebeu {dano} de dano'

#end of round
def eor():
    hp, escudo = f['hp'], f['escudo']
    for inimigo in inimigos.values():
        hitnave(inimigo['tipo'][0])
        if f['hp'] == 0:
            setfoo('gameon', False)
            break
    msg = f"R{f['rods']}: inimigos causaram {hp-f['hp']} no casco e {escudo-f['escudo']} no escudo."
    if f['hp'] > 0:
        if f['escudo'] > 0:
            setfoo('escudo', f['escudomax']) #só regenera se não foi destruído
            msg += ' Escudo regenerado.'
        setfoo('rods', f['rods']+1)
        setfoo('acoes', 3)
    setfoo('desvio', False)
    setfoo('mensagem_inimigos', msg)

def consumir_acao():
    f['acoes'] -= 1
    if not inimigos:
        setfoo('gamewin', True)
        setfoo('gameon', False)
    elif f['acoes'] == 0: eor()

#ações players
def desviar():
    if not f['gameon'] or f['acoes'] <= 0: return False
    if f['desvio']:
        setfoo('mensagem', 'Desvio já ativo nesta rodada.')
        return False
    setfoo('desvio', True)
    setfoo('mensagem', 'Desvio ativo: dano inimigo reduzido pela metade nesta rodada.')
    consumir_acao()
    return True

def atirar(tipo, alvo):
    if not f['gameon'] or f['acoes'] <= 0 or alvo not in inimigos: return False
    inimigo = inimigos[alvo]
    danos = {'normal': (8,16), 'torpedo': (24,5)} #escudo, casco
    if tipo not in danos: return False
    escudo = inimigo['escudo'] > 0
    dano = danos[tipo][0 if escudo else 1] + 4*inimigo['marcado']
    parte = 'escudo' if escudo else 'hp'
    dano = min(dano, inimigo[parte])
    inimigo[parte] -= dano #o escudo absorve o tiro inteiro
    msg = f"{alvo}: {dano} de dano no {'escudo' if escudo else 'casco'}."
    if inimigo['hp'] == 0:
        inimigos.pop(alvo)
        msg += ' Destruído!'
    setfoo('mensagem', msg)
    consumir_acao()
    return True

def procurar_ponto_fraco(alvo):
    if not f['gameon'] or f['acoes'] <= 0 or alvo not in inimigos: return False
    if inimigos[alvo]['marcado']:
        setfoo('mensagem', f'{alvo} já possui ponto fraco identificado.')
        return False
    inimigos[alvo]['marcado'] = True #+4 de dano permanente contra este alvo
    setfoo('mensagem', f'{alvo}: ponto fraco identificado (+4 de dano).')
    consumir_acao()
    return True

import curses
from dataclasses import dataclass, field
from typing import Callable, List, Optional

#sentinels

BACK = object()   # close this level, return to parent

#data model
@dataclass
class opt:
    label:   str
    submenu: List["opt"]   = field(default_factory=list)
    action:  Optional[Callable] = None   # (stdscr) → EXIT | BACK | None
    depth:   int = 0

def status_nave():
    return ["STATUS DA NAVE",
        f"Casco: {f['hp']}/80",
        f"Escudo: {f['escudo']}/{f['escudomax']}",
        f"Rodada: {f['rods']}",
        f"Ações restantes: {f['acoes']}",
        f"Desvio: {'Ativo' if f['desvio'] else 'Inativo'}"]

def mostrar_status(stdscr, items):
    largura = max(len(text) for text in items) + 2
    y, x = stdscr.getmaxyx()
    x = 1
    stdscr.addstr(1, x, "┌" + "─" * largura + "┐")
    for i, text in enumerate(items): stdscr.addstr(2 + i, x, "│ " + text.ljust(largura - 2) + " │")
    stdscr.addstr(2 + len(items), x, "└" + "─" * largura + "┘")

def mostrar_inimigos(stdscr, items):
    if not items: return
    y, x = stdscr.getmaxyx()
    linhas = ['INIMIGOS']
    for nome, inimigo in items.items():
        linhas.append(f"{nome} ({inimigo['tipo']})" + (' *' if inimigo['marcado'] else ''))
        linhas.append(f"HP: {inimigo['hp']} | Escudo: {inimigo['escudo']}")
    largura = max(len(text) for text in linhas)+2
    w = x-largura-3
    stdscr.addstr(1, w, "┌" + "─"*largura + "┐")
    for i, text in enumerate(linhas): stdscr.addstr(2+i, w, "│ " + text.ljust(largura-2) + " │")
    stdscr.addstr(2+len(linhas), w, "└" + "─"*largura + "┘")

menu_inputs = ["SETAS: Mover | ENTER: Selecionar | ESC: Voltar | DEL/F12: Sair"]
def mostrar_inputs(stdscr, items):
    y, x = stdscr.getmaxyx()
    stdscr.addstr(y-5, 1, items[0][:x-2])
    stdscr.addstr(y-7, 1, f['mensagem'][:x-2])
    stdscr.addstr(y-6, 1, f['mensagem_inimigos'][:x-2])

def draw_extras(stdscr):
    mostrar_status(stdscr, status_nave())
    mostrar_inimigos(stdscr, inimigos)
    mostrar_inputs(stdscr, menu_inputs)

def draw_menu_horizontal(stdscr, items, selected, draw_extras=None):
    stdscr.erase()
    h, w = stdscr.getmaxyx()
    if draw_extras: draw_extras(stdscr)
    gap = 2
    espaçamento = 1
    button_widths = [len(item.label) + (espaçamento * 2) for item in items]
    x = 1
    y = h - 4
    for idx, item in enumerate(items):
        bw   = button_widths[idx]
        text = item.label.center(bw - 2)
        stdscr.addstr(y + 1, x, "┌" + "─" * (bw - 2) + "┐")
        if idx == selected: stdscr.attron(curses.color_pair(1))
        stdscr.addstr(y + 2, x, "│" + text + "│")
        if idx == selected: stdscr.attroff(curses.color_pair(1))
        stdscr.addstr(y + 3, x, "└" + "─" * (bw - 2) + "┘")
        x += bw + gap
    stdscr.refresh()

def draw_menu_vertical(stdscr, items, selected, draw_extras=None):
    stdscr.erase()
    h, w = stdscr.getmaxyx()
    if draw_extras: draw_extras(stdscr)
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
    current = 0
    if layout == "horizontal":
        draw, anterior, proximo = draw_menu_horizontal, curses.KEY_LEFT, curses.KEY_RIGHT
    else:
        draw, anterior, proximo = draw_menu_vertical, curses.KEY_UP, curses.KEY_DOWN
    while f['gameon']:
        h,w = stdscr.getmaxyx()
        if h < 24 or w < 80: #evita escrever fora do terminal
            stdscr.erase()
            stdscr.addstr(0, 0, 'Terminal mínimo: 80x24'[:max(0,w-1)])
            stdscr.refresh()
            if stdscr.getch() in (curses.KEY_DC, curses.KEY_F12): return escape_seq()
            continue
        draw(stdscr, items, current, draw_extras)
        key = stdscr.getch()
        if key == anterior and current > 0: current -= 1
        elif key == proximo and current < len(items)-1: current += 1
        elif key in (curses.KEY_ENTER, 10, 13):
            item = items[current]
            if item.submenu:
                submenu = item.submenu() if callable(item.submenu) else item.submenu
                if submenu: run_menu(stdscr, submenu, draw_extras=draw_extras)
            elif item.action:
                result = item.action(stdscr)
                if result is BACK or (result is True and layout == "vertical"): return BACK
        elif key == 27 and layout == "vertical": return BACK
        elif key == curses.KEY_F12 or key == curses.KEY_DC: return escape_seq()

#game actions
def escape_seq(stdscr=None):
    setfoo('gameon', False)

def listar_inimigos(opçao):
    lista = []
    for nome in inimigos:
        if opçao == 'ponto_fraco':
            lista.append(opt(nome, action=lambda s, alvo=nome: procurar_ponto_fraco(alvo)))
        else:
            lista.append(opt(nome, action=lambda s, alvo=nome: atirar(opçao, alvo)))
    lista.append(opt("Voltar", action=lambda s: BACK))
    return lista

#menu tree
MENU = [opt("Desviar", action=lambda s: desviar()),
    opt("Atirar", submenu=lambda: listar_inimigos('normal')),
    opt("Atirar Torpedo", submenu=lambda: listar_inimigos('torpedo')),
    opt("Procurar Ponto Fraco", submenu=lambda: listar_inimigos('ponto_fraco'))]

#entry point
def main(stdscr):
    curses.curs_set(0)
    curses.noecho()
    stdscr.keypad(True)
    curses.typeahead(-1)
    curses.set_escdelay(25)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    run_menu(stdscr, MENU, layout="horizontal", draw_extras=draw_extras)
    if f['gamewin'] or f['hp'] <= 0:
        stdscr.erase()
        h,w = stdscr.getmaxyx()
        if h >= 24 and w >= 80: draw_extras(stdscr)
        msg = 'VITÓRIA! Todos os inimigos destruídos.' if f['gamewin'] else 'DERROTA! Sua nave foi destruída.'
        stdscr.addstr(h//2, max(0,(w-len(msg))//2), msg[:max(0,w-1)])
        stdscr.addstr(h-2, 1, 'Pressione qualquer tecla para sair.'[:max(0,w-2)])
        stdscr.refresh()
        stdscr.getch()

if __name__ == '__main__':
    curses.wrapper(main)
