from os import get_terminal_size, system
import cursor

CLEAR_SEQUENCE = "\x1b[1;1H\x1b[2J"

# Todo: check if system("stty...") works on windows

# Prevent user input from being displayed on the terminal
def hide_stdin():
    system("stty -echo")
    cursor.hide()

# Allow user input to be displayed on the terminal
def show_stdin():
    system("stty echo")
    cursor.show()


def clear_terminal():
    print(CLEAR_SEQUENCE, end="")

size = get_terminal_size()

width = int(size.columns / 2)
height = int(size.lines)
