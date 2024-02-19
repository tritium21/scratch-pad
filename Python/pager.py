#!/usr/bin/env python3
import itertools
import os
import sys

if sys.platform == 'win32':
    from msvcrt import getwch as getch
else:
    import tty
    import termios
    def getch():
        with open('/dev/pts/0', 'r') as stdin:
            fd = stdin.fileno()
            attr = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                return stdin.read(1)
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
                    print()
                    return
                case ' ' | '\r':
                    break
                case _:
                    continue
        print("        ", end="\r")

if __name__ == '__main__':
    import fileinput
    with fileinput.FileInput() as f:
        pager(l.removesuffix('\n') for l in f)
