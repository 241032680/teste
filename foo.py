def mostrar_status(stdscr, items):
    status = ["STATUS DA NAVE",
        f"Casco: {getstat(hp)}",
        f"Escudo frontal: {escudof[0]}",
        f"Escudo traseiro: {escudot[0]}",
        f"Velocidade máxima: {getstat(velmax)}",
        f"Modo de energia: {getstat(modoativo)}",
        f"Overclock: {'Ligado' if getstat(overclock) else 'Desligado'}",
        f"Criogenia: {'Ligada' if getstat(crio) else 'Desligada'}",
        f"Sonar: {'Ligado' if getstat(sonar) else 'Desligado'}",
        f"Rádio: {'Ligado' if getstat(radio) else 'Desligado'}",
        f"Gravidade: {'Ligada' if getstat(grav) else 'Desligada'}"]
    largura = max(len(text) for text in status) + 2
    y, x = stdscr.getmaxyx()
    coluna = x // 4
    stdscr.addstr(1, coluna, "┌" + "─" * largura + "┐")

    for i, text in enumerate(status):
        stdscr.addstr(2 + i, coluna, "│ " + text.ljust(largura - 2) + " │")
    stdscr.addstr(2 + len(status), coluna, "└" + "─" * largura + "┘")