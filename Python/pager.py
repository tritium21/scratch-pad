import itertools
import os
import sys

if sys.platform == 'win32':
    from msvcrt import getwch as getch
else:
    import tty
    import termios
    def getch():
        fd = sys.stdin.fileno()
        attr = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSANOW, attr)

def pager(iterable, page_size=os.get_terminal_size().lines):
    groups = [iter(iterable)] * page_size
    fill = object()
    for group in itertools.zip_longest(*groups, fillvalue=fill):
        for line in group:
            if line is fill:
                return
            print(line)
        print('--MORE--', end="\r")
        while (hit := getch()):
            match hit:
                case '\x1b' | 'q':
                    return
                case ' ' | '\r':
                    break
                case _:
                    continue
        print("        \r", end="")

if __name__ == '__main__':
    pager(range(100))
