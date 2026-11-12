import curses

def colors(stdscr):
    height, width = stdscr.getmaxyx()
    for i in range(min(256, curses.COLORS)):
        pair = i + 1
        if pair >= curses.COLOR_PAIRS:
            break
        curses.init_pair(pair, i, -1)
        y = i // 16
        x = (i % 16) * 5
        if y < height and x + 4 < width:
            stdscr.addstr(y, x, f"{i+1:3} ", curses.color_pair(pair))

def test(stdscr):
    y,x = stdscr.getmaxyx()
    curses.init_pair(2, 1, -1)
    stdscr.addstr(16, x-x//2, f"I", curses.color_pair(2)|curses.A_BOLD)
    stdscr.addstr(17, x-x//2, f"I", curses.color_pair(2))
    stdscr.addstr(18, x-x//2, f"I", curses.color_pair(10))
    stdscr.addstr(19, x-x//2, f"I", curses.color_pair(161))
    stdscr.addstr(20, x-x//2, f"I", curses.color_pair(197))
    stdscr.addstr(21, x-x//2, f"I", curses.color_pair(125))



def main(stdscr):
    curses.curs_set(0)
    curses.use_default_colors()
    stdscr.clear()
    test(stdscr)
    colors(stdscr)
    stdscr.refresh()
    stdscr.getch()
    
curses.wrapper(main)