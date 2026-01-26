import numpy as np
import copy, os, getch, sys

key_ammount = 0; move_count = 0; all_moves = 0; map_index = 0; retry_count = 0
latch_1 = 0; latch_2 = 0; latch_3 = 0
latch_arr = [0, 0, 0, 0, 0, 0, 0]
deadly_floor = [0, 1, 2]; pure_deadly_floor = 2; pure_deadly_floor_plus = 3; spike_count = 0
x_coord = 9; y_coord = 8
coords = np.array([[9, 8], [7, 7], [1, 10], [1, 12], [2, 10], [6, 13], [7, 11], [13, 11], [2, 13], [6, 8]])
mode = 0; tic = True; space = " "
showpos = 0; noclip = 0; noclip_destroy = 0; god = 0; dots = 1
INDESTRUCTABLE = ["*", "=" "t", "T"]
DEADLY = ["*", "="]
WALLS = np.array(['═', '║', '╚', '╝', '╔', '╗', '╠', '╣', '╩', '╦', '╬'])
LEVEL_TITLECARD = np.array(["LVL01: Introduction", "LVL02: Four way", "LVL03: Boxes", "LVL04: Buttons", "LVL05: Barb Wire", "LVL06: Back 'n' forth", "LVL07: Dance Floor", "LVL08: Maze", "LVL09: Spiral", "THX: Thanks for playing!"])
LEVEL_INSTRUCTION = np.array(["@: Player - Moved with WASD controls\nK: Key; D: Door - Can't be passed without a key", "If you get stuck press R to retry the level", "B: Box - Can be pushed by the player\nH: Hole - kills the player and is filled by a box", "*: spike - Kills the player and destroys boxes\no/O: Button - Can be pushed by a box", " ", "T/t: Teleporter", " ", " ", " ", " "])

lvl01 = np.array([['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '╔', '═', '╗', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '║', 'E', '║', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '║', 'D', '║', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '╔', '═', '═', '╝', '.', '║', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '║', 'K', '.', '.', '@', '║', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '╚', '═', '═', '═', '═', '╝', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']])
lvl01_start = copy.deepcopy(lvl01)

lvl02 = np.array([['.', '.', '.', '.', '╔', '═', '═', '═', '═', '═', '╗', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '║', 'D', '.', '.', '.', '.', '║', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '║', 'K', '╦', '.', '╦', 'D', '║', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '║', 'K', '║', '.', '║', 'N', '║', '.', '.', '.', '.'],
                  ['╔', '═', '═', '═', '╬', '═', '╣', '.', '╠', '═', '╬', '═', '═', '═', '╗'],
                  ['║', '.', '.', 'K', '║', '.', '║', '.', '║', '.', '║', 'E', 'D', '.', '║'],
                  ['║', '.', '╠', '═', '╩', '═', '╝', '.', '╚', '═', '╩', '═', '╣', '.', '║'],
                  ['║', '.', 'K', 'K', 'D', 'D', '.', '@', '.', '.', '.', 'D', 'D', '.', '║'],
                  ['║', '.', '╠', '═', '╦', '═', '╗', '.', '╔', '═', '╦', '═', '╣', '.', '║'],
                  ['║', '.', '.', 'K', '║', '.', '║', '.', '║', '.', '║', 'E', 'D', '.', '║'],
                  ['╚', '═', '═', '═', '╬', '═', '╣', '.', '╠', '═', '╬', '═', '═', '═', '╝'],
                  ['.', '.', '.', '.', '║', '.', '║', '.', '║', 'K', '║', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '║', 'D', '╩', '.', '╩', '.', '║', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '║', '.', '.', '.', '.', '.', '║', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '╚', '═', '═', '═', '═', '═', '╝', '.', '.', '.', '.']])
lvl02_start = copy.deepcopy(lvl02)

lvl03 = np.array([['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '╔', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╗'],
                  ['.', '.', '║', '.', '.', '.', '.', '.', '.', '.', '.', 'H', '.', 'E', '║'],
                  ['.', '.', '║', '.', '╔', '╗', '.', '╔', '╗', '.', '╔', '═', '═', '═', '╝'],
                  ['.', '╔', '╝', '.', '╚', '╝', '.', '╚', '╝', '.', '║', '.', '.', '.', '.'],
                  ['.', '║', '.', 'B', '.', '.', 'B', '.', '.', 'B', '║', '.', '.', '.', '.'],
                  ['.', '╚', '╗', '.', '╔', '╗', '.', '╔', '╗', '.', '║', '.', '.', '.', '.'],
                  ['╔', '═', '╝', '.', '╚', '╝', '.', '╚', '╝', '.', '║', '.', '.', '.', '.'],
                  ['║', '@', '.', '.', '.', '.', '.', '.', '.', '.', '║', '.', '.', '.', '.'],
                  ['╚', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╝', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']])
lvl03_start = copy.deepcopy(lvl03)

lvl04 = np.array([['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['╔', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╗'],
                  ['║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', 'E', '║'],
                  ['║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '╔', '═', '╝'],
                  ['║', '.', '.', '╔', '═', '╗', '.', '╔', '═', '╗', '.', '.', '║', '.', '.'],
                  ['║', '.', '.', '║', '.', '.', '.', '.', '.', '║', '.', '.', '║', '.', '.'],
                  ['║', '.', '.', '╚', '.', '.', '.', '.', '.', '╝', '.', '.', '║', '.', '.'],
                  ['║', '.', '.', '.', '.', '.', 'o', '.', '.', '.', 'B', '.', '║', '.', '.'],
                  ['║', '.', '.', '╔', '.', '.', '.', '.', '.', '╗', '.', '.', '║', '.', '.'],
                  ['║', '.', '.', '║', '.', '.', '.', '.', '.', '║', '.', '.', '║', '.', '.'],
                  ['║', '.', '.', '╚', '═', '╝', '.', '╚', '═', '╝', '.', '.', '║', '.', '.'],
                  ['║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║', '.', '.'],
                  ['║', '@', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║', '.', '.'],
                  ['╚', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╝', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']])
lvl04_start = copy.deepcopy(lvl04)

lvl05 = np.array([['.', '.', '*', '*', '*', '*', '*', '.', '.', '.', '*', '*', '*', '.', '.',],
                  ['.', '.', '*', '.', '.', '.', '*', '.', '.', '.', '*', 'o', '*', '.', '.',],
                  ['.', '.', '*', '.', '*', '.', '*', '*', '*', '*', '*', '.', '*', '*', '*',],
                  ['.', '.', '*', '.', '.', '.', '.', '.', '.', '.', '║', '.', '║', '.', '*',],
                  ['.', '.', '*', '.', '*', '*', '*', '*', '.', '*', '*', '.', '*', '.', '*',],
                  ['.', '.', '*', '.', '*', '.', '.', '*', '.', '*', '*', '.', '║', '.', '*',],
                  ['.', '.', '*', '.', '*', '.', '.', '*', '*', '*', '*', '.', '*', '*', '*',],
                  ['.', '*', '*', '.', '*', '.', '.', '.', '*', '*', '*', '.', '*', '.', '.',],
                  ['.', '*', 'E', 'H', '*', '.', '.', '.', '*', '.', '.', '.', '*', '.', '.',],
                  ['.', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '.', '*', '.', '.',],
                  ['.', '*', '@', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.',],
                  ['.', '*', '*', '*', '*', '*', '*', '*', '*', '.', '*', '.', '*', '.', '.',],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '*', '.', '.',],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '*', '*', '*', '*', '*', '.', '.',],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',]])
lvl05_start = copy.deepcopy(lvl05)

lvl06 = np.array([['╔', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', 'o', '╗'],
                  ['║', 'T', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║'],
                  ['╚', '═', '═', '═', '╗', '.', '╦', '.', '╔', '═', '═', '═', '╗', '.', '║'],
                  ['╔', '═', '╗', '.', '║', '.', '║', '.', '║', '╔', '═', '═', '╝', '.', '║'],
                  ['║', 't', '║', '.', '║', '.', '║', '.', '║', '║', '.', '.', '.', '.', '║'],
                  ['║', '.', '║', '.', '╚', '═', '╩', '═', '╝', '╠', '═', '═', '╣', '.', '║'],
                  ['║', 'B', '║', '.', '.', '.', '.', '.', '.', '║', '.', '.', '.', '.', '║'],
                  ['║', '.', '╚', '═', '═', '╗', '.', '.', '.', '╚', '═', '═', '╗', '.', '║'],
                  ['║', '.', '.', '.', '.', '║', '.', '.', '.', '.', '.', '.', '║', '.', '║'],
                  ['║', '.', '╠', '═', '═', '╣', '.', '╔', '═', '╦', '═', '╗', '║', '.', '║'],
                  ['║', '.', '.', '.', '.', '║', '.', '║', '.', '║', '.', '║', '║', 't', '║'],
                  ['║', '.', '╔', '═', '═', '╝', '.', '║', '.', '║', '.', '║', '╚', '═', '╝'],
                  ['║', '.', '║', '╔', '═', '═', '═', '╝', '.', '╩', '.', '╚', '═', '═', '╗'],
                  ['║', '.', '║', '║', 'E', 'H', '@', '.', '.', '.', '.', '.', '.', 'T', '║'],
                  ['╚', 'o', '╝', '╚', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╝']])
lvl06_start = copy.deepcopy(lvl06)

lvl07 = np.array([['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '╔', '═', '╗', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '╔', '═', '╗', '.', '║', 'T', '║', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '║', 'T', '╠', '═', '╝', '.', '╚', '═', '╦', '═', '╗', '.', '.'],
                  ['.', '.', '║', '.', '║', '.', '.', '.', '.', '.', '║', 'K', '║', '.', '.'],
                  ['.', '.', '║', '.', '╩', '.', '.', '.', '.', '.', '╠', '═', '╣', '.', '.'],
                  ['.', '.', '║', '.', 'B', '.', '.', '.', '.', '.', '.', 'o', '║', '.', '.'],
                  ['.', '.', '╠', '═', '╣', '.', '.', '.', '.', '.', '╔', '═', '╝', '.', '.'],
                  ['.', '.', '║', 'E', 'D', '.', '.', '.', '.', '.', '║', '.', '.', '.', '.'],
                  ['.', '.', '╚', '═', '═', '═', '╗', '.', '╔', '═', '╝', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '║', '@', '║', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '╚', '═', '╝', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']])
lvl07_start = copy.deepcopy(lvl07)

lvl08 = np.array([['╔', 'o', '╦', 'o', '═', '═', '╦', 'o', '═', '═', '╦', 'o', '═', '═', '╗'],
                  ['║', 'B', '║', '.', '.', '.', '║', '.', '.', '.', '║', '.', '.', '.', '║'],
                  ['║', '.', '║', '.', '╦', '.', '║', '.', '╦', '.', '║', '.', '╦', '.', '║'],
                  ['║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║'],
                  ['║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║'],
                  ['║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║'],
                  ['║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║'],
                  ['║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║'],
                  ['║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║'],
                  ['║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║'],
                  ['║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║'],
                  ['║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '.', '║', '@', '║'],
                  ['║', '.', '╩', '.', '║', '.', '╩', '.', '║', '.', '╩', '.', '║', 'H', '║'],
                  ['║', '.', '.', '.', '║', '.', '.', '.', '║', '.', '.', '.', '║', 'E', '║'],
                  ['╚', 'o', '═', '═', '╩', 'o', '═', '═', '╩', 'o', '═', '═', '╩', '═', '╝']])
lvl08_start = copy.deepcopy(lvl08)

lvl09 = np.array([['╔', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╗'],
                  ['║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║'],
                  ['║', '.', '╔', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╗', '.', '║'],
                  ['║', '.', '║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║', '.', '║'],
                  ['║', '.', '║', '.', '╔', '═', '═', '═', '═', '═', '╗', '.', '║', '.', '║'],
                  ['║', '.', '║', '.', '║', '.', '.', '.', '.', '.', '║', '.', '║', '.', '║'],
                  ['║', '.', '║', '.', '║', '.', '╠', '═', '╗', '.', '║', '.', '║', '.', '║'],
                  ['║', '.', '║', '.', '║', '.', '.', 'K', '║', '.', '║', '.', '║', '.', '║'],
                  ['║', '.', '║', '.', '╚', '═', '═', '═', '╝', '.', '║', '.', '║', '.', '║'],
                  ['║', '.', '║', '.', '.', '.', '.', '.', '.', '.', '║', '.', '║', '.', '║'],
                  ['║', '.', '╚', '═', '═', '═', '═', '═', '═', '═', '╝', '.', '║', '.', '║'],
                  ['║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║', '.', '║'],
                  ['╠', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╝', '.', '║'],
                  ['E', 'D', '@', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║'],
                  ['╚', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╝']])
lvl09_start = copy.deepcopy(lvl09)

lvl10 = np.array([['╔', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╗'],
                  ['║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║'],
                  ['║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║'],
                  ['║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║'],
                  ['║', '═', '═', '╦', '═', '═', '.', '.', '.', '.', '.', '.', '.', '.', '║'],
                  ['║', '.', '.', '║', '.', '.', '.', '║', '.', '║', '.', '║', '.', '║', '║'],
                  ['║', '.', '.', '║', '.', '.', '.', '║', '.', '║', '.', '║', '.', '║', '║'],
                  ['║', '.', '.', '║', '.', '.', '.', '║', 'C', '║', '.', '║', '.', '║', '║'],
                  ['║', '.', '.', '║', '.', '.', '@', '╠', '═', '╣', '.', '╚', '╦', '╝', '║'],
                  ['║', '.', '.', '║', '.', '.', '.', '║', '.', '║', '.', '╔', '╩', '╗', '║'],
                  ['║', '.', '.', '║', '.', '.', '.', '║', '.', '║', '.', '║', '.', '║', '║'],
                  ['║', '.', '.', '║', '.', '.', '.', '║', '.', '║', '.', '║', '.', '║', '║'],
                  ['║', '.', '.', '║', '.', '.', '.', '║', '.', '║', '.', '║', '.', '║', '║'],
                  ['║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║'],
                  ['╚', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╝'],])
lvl10_start = copy.deepcopy(lvl10)

LEVELS = np.array([lvl01, lvl02, lvl03, lvl04, lvl05, lvl06, lvl07, lvl08, lvl09, lvl10])
LEVELS_START = np.array([lvl01_start, lvl02_start, lvl03_start, lvl04_start, lvl05_start, lvl06_start, lvl07_start, lvl08_start, lvl09_start, lvl10_start])

class bcolors:
    GRAY = '\033[90m'
    WHITE = '\033[37m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    ORANGE = '\033[33m'
    LIGHTGREEN = "\033[92m"
    GREEN = '\033[32m'
    YELLOW = '\033[93m'
    RED = '\033[31m'
    LIGHTRED = '\033[91m'
    PURPLE = '\033[35m'
    ENDC = '\033[0m'

def color_check(iterator):
    global color
    if iterator == 'K': color = bcolors.GREEN
    elif iterator == 'D': color = bcolors.MAGENTA
    elif iterator == '*': color = bcolors.RED
    elif iterator == '=': color = bcolors.ORANGE
    elif iterator == 'C': color = bcolors.YELLOW
    elif iterator == 'X': color = bcolors.RED
    elif iterator == 'B': color = bcolors.BLUE
    elif iterator == 'E': color = bcolors.YELLOW
    elif iterator == '@': color = bcolors.LIGHTGREEN
    elif iterator == 'o': color = bcolors.LIGHTRED
    elif iterator == 'O': color = bcolors.LIGHTRED
    elif iterator == 'T': color = bcolors.PURPLE
    elif iterator == 't': color = bcolors.PURPLE
    elif iterator == 'H': color = bcolors.ORANGE
    elif iterator in WALLS: color = bcolors.WHITE
    elif iterator == '.': color = bcolors.GRAY
    return color

def clear_screen():
    if sys.platform == "win32":
        os.system("cls")
        return
    os.system("clear")

def print_level():
    global mode, showpos
    clear_screen()
    if mode == 1:
        for i in range(len(lvl01)):
            for j in range(len(lvl01)):
                text = color_check(LEVELS[map_index][i, j])
                if LEVELS[map_index][i, j] == "=":
                    LEVELS[map_index][i, j] = "*"
                if dots == False:
                    if LEVELS[map_index][i, j] == ".":
                        print(" ", end=space)
                    else:
                        print(text + LEVELS[map_index][i, j] + bcolors.ENDC, end=space)
                else:
                    print(text + LEVELS[map_index][i, j] + bcolors.ENDC, end=space)
            print()
    elif mode == 3:
        print_playarea(2, 3)
    elif mode == 4:
        print_playarea(1, 2)
    else:
        print_playarea(4, 5)
    print(LEVEL_TITLECARD[map_index])
    print(f"KEYS={key_ammount} MOVES={move_count} ALL={all_moves} RETRIES={retry_count}")
    if LEVEL_INSTRUCTION[map_index] != " ":
        print(LEVEL_INSTRUCTION[map_index])
    print("Press H for full instructions")
    if showpos == 1:
        print(f"{x_coord}, {y_coord}")

def print_playarea(left, right):
    global space, dots
    for i in range(y_coord - left, y_coord + right):
        for j in range(x_coord - left, x_coord + right):
            if i >= len(lvl01) or j >= len(lvl01):
                print(bcolors.GRAY + "." + bcolors.ENDC, end=space)
                continue
            text = color_check(LEVELS[map_index][i, j])
            if LEVELS[map_index][i, j] == " ":
                LEVELS[map_index][i, j] = "*"
            if dots == False:
                if LEVELS[map_index][i, j] == ".":
                    print(" ", end=space)
                else:
                    print(text + LEVELS[map_index][i, j] + bcolors.ENDC, end=space)
            else:
                print(text + LEVELS[map_index][i, j] + bcolors.ENDC, end=space)
        print()

def character_movement(x_dir, y_dir):
    global key_ammount, map_index, y_coord, x_coord, move_count, all_moves, latch_1, latch_2, latch_3, tic, noclip, god, retry_count, latch_arr
    move_count += 1
    if (LEVELS[map_index][y_coord + y_dir, x_coord + x_dir] in WALLS or y_coord + y_dir == 17 or LEVELS[map_index][y_coord + y_dir, x_coord + x_dir] == "o") and noclip == 0:
        move_count -= 1
        tic = False
        return
    elif x_coord + x_dir == 17 or y_coord + y_dir == 17 or y_coord + y_dir == -18 or x_coord + x_dir == -18:
        move_count -= 1
        tic = False
        return
    elif LEVELS[map_index][y_coord + y_dir, x_coord + x_dir] == "D":
        if key_ammount == 0 and noclip == 0:
            move_count -= 1
            tic = False
            return
        key_ammount -= 1
    elif LEVELS[map_index][y_coord + y_dir, x_coord + x_dir] == "B" and noclip == 0:
        while True:
            if LEVELS[map_index][y_coord + y_dir + y_dir, x_coord + x_dir + x_dir] in WALLS or LEVELS[map_index][y_coord + y_dir + y_dir, x_coord + x_dir + x_dir] == "B":
                move_count -= 1
                tic = False
                return
            elif LEVELS[map_index][y_coord + y_dir + y_dir, x_coord + x_dir + x_dir] in DEADLY or LEVELS[map_index][y_coord + y_dir + y_dir, x_coord + x_dir + x_dir] == "o":
                LEVELS[map_index][y_coord + y_dir + y_dir, x_coord + x_dir + x_dir] = "*"
                break
            elif LEVELS[map_index][y_coord + y_dir + y_dir, x_coord + x_dir + x_dir] == "H":
                LEVELS[map_index][y_coord + y_dir + y_dir, x_coord + x_dir + x_dir] = "."
                break
            LEVELS[map_index][y_coord + y_dir + y_dir, x_coord + x_dir + x_dir] = "B"
            break
    elif LEVELS[map_index][y_coord + y_dir, x_coord + x_dir] == "K":
        key_ammount += 1
    elif LEVELS[map_index][y_coord + y_dir, x_coord + x_dir] == "H" and god == 0:
        LEVELS[map_index][y_coord, x_coord] = "X"
        print_level()
        input("You fell down a hole...")
        map_specific_events()
        retry_count += 1
        pure_deadly_floor = 2
        move_count = 0
        key_ammount = 0
        latch_1 = 0; latch_2 = 0; latch_3 = 0
        latch_arr = [0, 0, 0, 0, 0, 0, 0]
        x_coord, y_coord = coords[map_index, 0], coords[map_index, 1]
        LEVELS[map_index] = copy.deepcopy(LEVELS_START[map_index])
        print_level()
        return
    elif LEVELS[map_index][y_coord + y_dir, x_coord + x_dir] in DEADLY and god == 0:
        LEVELS[map_index][y_coord, x_coord] = "X"
        print_level()
        input("You Died...")
        map_specific_events()
        retry_count += 1
        move_count = 0
        key_ammount = 0
        latch_1 = 0; latch_2 = 0; latch_3 = 0
        latch_arr = [0, 0, 0, 0, 0, 0, 0]
        x_coord, y_coord = coords[map_index, 0], coords[map_index, 1]
        LEVELS[map_index] = copy.deepcopy(LEVELS_START[map_index])
        print_level()
        return
    elif LEVELS[map_index][y_coord + y_dir, x_coord + x_dir] == "E" and noclip == 0:
        pure_deadly_floor = 2
        LEVELS[map_index] = copy.deepcopy(LEVELS_START[map_index])
        map_specific_events()
        map_index += 1
        x_coord, y_coord = coords[map_index, 0], coords[map_index, 1]
        all_moves += move_count
        move_count = 0
        latch_1 = 0; latch_2 = 0; latch_3 = 0
        latch_arr = [0, 0, 0, 0, 0, 0, 0]
        key_ammount = 0
        print_level()
        return
    x_coord += x_dir; y_coord += y_dir
    LEVELS[map_index][y_coord, x_coord] = "@"
    if LEVELS[map_index][y_coord - y_dir, x_coord - x_dir] != "*":
        LEVELS[map_index][y_coord - y_dir, x_coord - x_dir] = "."
    if noclip == 1 and noclip_destroy == 0:
         LEVELS[map_index][y_coord - y_dir, x_coord - x_dir] = LEVELS_START[map_index][y_coord - y_dir, x_coord - x_dir]
    tic = True

def character_input():
    global key_ammount, map_index, y_coord, x_coord, move_count, tic, showpos, noclip, noclip_destroy, god, mode, space, dots, retry_count, latch_1, latch_2, latch_3, latch_arr
    action = getch.getch()
    if action == "r" or action == "R":
        map_specific_events()
        move_count = 0
        key_ammount = 0
        pure_deadly_floor = 2
        retry_count += 1
        latch_1 = 0; latch_2 = 0; latch_3 = 0
        latch_arr = [0, 0, 0, 0, 0, 0, 0]
        x_coord, y_coord = coords[map_index, 0], coords[map_index, 1]
        LEVELS[map_index] = copy.deepcopy(LEVELS_START[map_index])
        print_level()
        return
    elif action  == "w" or action == "W":
        character_movement(0, -1)
        return
    elif action == "s" or action == "S":
        character_movement(0, 1)
        return
    elif action == "a" or action == "A":
        character_movement(-1, 0)
        return
    elif action == "d" or action == "D":
        character_movement(1, 0)
        return
    elif action == "h" or action == "H":
        clear_screen()
        print("Legend for the game:")
        print("@ - Player")
        print("K - Key")
        print("T - Teleporter")
        print("E - Exit")
        print("H - Hole: Kills the player, can be filled by a box")
        print("o/O - Ground button: Can be pushed by a box")
        print("D - Door: Needs a key to open it and takes one from you")
        print("B - Box: Used for filling holes and pressing buttons")
        print("* - Spike: Kills the player and destroys boxes")
        print("Controls:")
        print("WASD for movement of the player")
        print("R to restart level")
        print("C for the console, for which you can find instructions on the github page")
        input("Press Enter to exit this screen")
        print_screen()
    elif action == "c" or action == "C":
        print("Input a command:")
        try:
            command = input().split(" ")
            if command[0].lower() == "changelvl":
                if len(command) < 2:
                    input("No arguments present")
                    return
                elif int(command[1]) > len(LEVELS):
                    input("Map of that index doesnt exist")
                    return
                LEVELS[map_index] = LEVELS_START[map_index]
                map_index = int(command[1]) - 1
                latch_1 = 0; latch_2 = 0; latch_3 = 0
                key_ammount = 0
                map_specific_events()
                x_coord, y_coord = coords[map_index, 0], coords[map_index, 1]
                move_count = 0
                print_level()
            elif command[0].lower() == "setpos":
                if len(command) < 3:
                    input("Not enough arguments present")
                    return
                elif int(command[1]) >= 17 or int(command[2]) >= 17 or int(command[1]) <= -18 or int(command[2]) <= -18:
                    input("This coordinate is beyond reach")
                    return
                LEVELS[map_index][y_coord, x_coord] = "."
                x_coord, y_coord = int(command[1]), int(command[2])
                LEVELS[map_index][y_coord, x_coord] = "@"
            elif command[0].lower() == "startpos":
                LEVELS[map_index][y_coord, x_coord] = "."
                x_coord, y_coord = coords[map_index, 0], coords[map_index, 1]
                LEVELS[map_index][y_coord, x_coord] = "@"
            elif command[0].lower() == "showpos":
                if len(command) < 2:
                    input("No arguments present")
                    return
                showpos = int(command[1])
            elif command[0].lower() == "noclip":
                if len(command) < 2:
                    input("No arguments present")
                    return
                if len(command) == 3:
                    if command[2].lower() == "d1":
                        noclip_destroy = 1
                    else:
                        noclip_destroy = 0
                noclip = int(command[1])
            elif command[0].lower() == "god":
                if len(command) < 2:
                    input("No arguments present")
                    return
                god = int(command[1])
            elif command[0].lower() == "summon":
                if len(command) < 2:
                    input("No arguments present")
                    return
                elif len(command) == 4:
                    if int(command[2]) >= 17 or int(command[3]) >= 17 or int(command[2]) <= -18 or int(command[3]) <= -18:
                        input("This coordinate is beyond reach")
                        return
                    LEVELS[map_index][int(command[3]), int(command[2])] = command[1]
                    return
                LEVELS[map_index][y_coord + 1, x_coord] = command[1]
            elif command[0].lower() == "setkey":
                if len(command) < 2:
                    input("No arguments present")
                    return
                key_ammount = int(command[1])
            elif command[0].lower() == "changedif":
                if len(command) < 2:
                    input("No arguments present")
                    return
                mode = int(command[1])
            elif command[0].lower() == "setmove":
                if len(command) < 2:
                    input("No arguments present")
                    return
                move_count = int(command[1])
            elif command[0].lower() == "space":
                if len(command) < 2:
                    input("No arguments present")
                    return
                if command[1] == "1":
                    space = " "
                    return
                space = ""
            elif command[0].lower() == "dots":
                if len(command) < 2:
                    input("No arguments present")
                    return
                dots = int(command[1])
            print_level()
        except ValueError:
                input("There is no digit")
    tic = False

def map_specific_events():
    global map_index, move_count, latch_1, deadly_floor, absolute_deadly_floor, pure_deadly_floor, absolute_deadly_floor_plus, pure_deadly_floor_plus, x_coord, y_coord, tic, latch_2, latch_3, spike_count, dots
    if map_index == 1:
        if LEVELS[map_index][3, 9] == "@":
            dots = 0
            print_level()
    if map_index == 3:
        absolute_deadly_floor = abs(pure_deadly_floor - 2)
        absolute_deadly_floor_plus = abs(pure_deadly_floor_plus - 2)
        LEVELS[map_index][8 - absolute_deadly_floor_plus, 6 + absolute_deadly_floor - 1] = "."
        pure_deadly_floor = (pure_deadly_floor + 1) % 4
        absolute_deadly_floor = abs(pure_deadly_floor - 2)
        pure_deadly_floor_plus = (pure_deadly_floor_plus + 1) % 4
        absolute_deadly_floor_plus = abs(pure_deadly_floor_plus - 2)
        LEVELS[map_index][8 - absolute_deadly_floor_plus, 6 + absolute_deadly_floor - 1] = "*"
        if LEVELS[map_index][7, 6] == "*":
            if latch_1 == 0:
                LEVELS[map_index][6, 5] = "B"
                LEVELS[map_index][6, 7] = "B"
                LEVELS[map_index][8, 5] = "B"
                LEVELS[map_index][8, 7] = "B"
                latch_1 = 1
                LEVELS[map_index][7, 7] = "@"
                print_level()
            for i in range(2):
                for j in range(2):
                    if LEVELS[map_index][5 + (i*4), 4 + (j*4)] != "B":
                        LEVELS[map_index][5 + (i*4), 4 + (j*4)] = "O"
            if np.count_nonzero(LEVELS[map_index] == "O") == 0:
                if LEVELS[map_index][2, 12] != "@":
                    LEVELS[map_index][2, 12] = "."
                print_level()
    elif map_index == 4:
        if LEVELS[map_index][1, 11] == "*":
            if latch_1 == 0:
                LEVELS[map_index][11, 11] = "B"
                latch_1 = 1
            if LEVELS[map_index][3, 10] != "B":
                LEVELS[map_index][3, 10] = "."
            LEVELS[map_index][3, 12] = "."
            LEVELS[map_index][5, 12] = "."
            if latch_2 == 0:
                print_level()
                latch_2 = 1
        absolute_deadly_floor = abs(pure_deadly_floor - 2)
        LEVELS[map_index][8, 10 + absolute_deadly_floor - 1] = "."
        LEVELS[map_index][4 + absolute_deadly_floor - 1, 8] = "."
        pure_deadly_floor = (pure_deadly_floor + 1) % 4
        absolute_deadly_floor = abs(pure_deadly_floor - 2)
        LEVELS[map_index][4 + absolute_deadly_floor - 1, 8] = "*"
        LEVELS[map_index][8, 10 + absolute_deadly_floor - 1] = "*"
    elif map_index == 5:
        if LEVELS[map_index][1, 1] == "B":
            LEVELS[map_index][13, 12] = "B"
            LEVELS[map_index][1, 1] = "T"
            print_level()
        if LEVELS[map_index][4, 1] == "B":
            LEVELS[map_index][9, 13] = "B"
            LEVELS[map_index][4, 1] = "t"
            print_level()
        pure_deadly_floor += 1
        LEVELS[map_index][10 + (pure_deadly_floor % 4), 8] = "*"
        LEVELS[map_index][10 + ((pure_deadly_floor - 1) % 4), 8] = "."
        LEVELS[map_index][10 + ((pure_deadly_floor + 1) % 4), 10] = "*"
        LEVELS[map_index][10 + (pure_deadly_floor % 4), 10] = "."
        LEVELS[map_index][4 - ((pure_deadly_floor + 1) % 4), 5] = "*"
        LEVELS[map_index][4 - (pure_deadly_floor % 4), 5] = "."
        LEVELS[map_index][4 - ((pure_deadly_floor + 2) % 4), 7] = "*"
        LEVELS[map_index][4 - ((pure_deadly_floor + 1) % 4), 7] = "."
        LEVELS[map_index][4, 10 + (pure_deadly_floor % 4)] = "*"
        LEVELS[map_index][4, 10 + ((pure_deadly_floor - 1) % 4)] = "."
        LEVELS[map_index][6, 10 + ((pure_deadly_floor + 2) % 4)] = "*"
        LEVELS[map_index][6, 10 + ((pure_deadly_floor + 1) % 4)] = "."
        LEVELS[map_index][8, 4 - ((pure_deadly_floor + 1) % 4)] = "*"
        LEVELS[map_index][8, 4 - (pure_deadly_floor % 4)] = "."
        LEVELS[map_index][10, 4 - ((pure_deadly_floor + 3) % 4)] = "*"
        LEVELS[map_index][10, 4 - ((pure_deadly_floor + 2) % 4)] = "."
        LEVELS[map_index][13, 13] = "T"
        LEVELS[map_index][1, 1] = "T"
        LEVELS[map_index][10, 13] = "t"
        LEVELS[map_index][4, 1] = "t"
        if x_coord == 13 and y_coord == 13:
            x_coord = 1; y_coord = 1
            LEVELS[map_index][1, 1] = "@"
            print_level()
            return
        elif x_coord == 1 and y_coord == 1:
            x_coord = 13; y_coord = 13
            LEVELS[map_index][13, 13] = "@"
            print_level()
        elif x_coord == 13 and y_coord == 10:
            x_coord = 1; y_coord = 4
            LEVELS[map_index][4, 1] = "@"
            print_level()
            return
        elif x_coord == 1 and y_coord == 4:
            x_coord = 13; y_coord = 10
            LEVELS[map_index][10, 13] = "@"
            print_level()
            return
        if LEVELS[map_index][14, 1] == "*" and latch_1 == 0:
            LEVELS[map_index][12, 1] = "B"
            print_level()
            latch_1 = 1
        if LEVELS[map_index][0, 13] == "*" and latch_2 == 0:
            LEVELS[map_index][1, 12] = "B"
            print_level()
            latch_2 = 1
        if latch_3 == 0:
            print_level()
            latch_3 = 1
    elif map_index == 6:
        LEVELS[map_index][3, 7] = "T"
        LEVELS[map_index][4, 3] = "T"
        if x_coord == 3 and y_coord == 4:
            x_coord = 7; y_coord = 3
            LEVELS[map_index][3, 7] = "@"
            print_level()
            return
        elif x_coord == 7 and y_coord == 3:
            x_coord = 3; y_coord = 4
            LEVELS[map_index][4, 3] = "@"
            print_level()
            return
        pure_deadly_floor += 1
        if LEVELS[map_index][7, 11] == "*":
            LEVELS[map_index][5, 10] = "."
            if latch_1 == 0:
                print_level()
                latch_1 = 1
        # Moving killing floors
        LEVELS[map_index][9 - (pure_deadly_floor % 5), 6] = '*'
        LEVELS[map_index][9 - ((pure_deadly_floor - 1) % 5), 6] = "."
        LEVELS[map_index][9 - ((pure_deadly_floor + 1) % 5), 8] = "*"
        LEVELS[map_index][9 - (pure_deadly_floor % 5), 8] = "."
        LEVELS[map_index][6, 9 - ((pure_deadly_floor + 1) % 5)] = "="
        LEVELS[map_index][6, 9 - (pure_deadly_floor % 5)] = "."
        LEVELS[map_index][8, 9 - (pure_deadly_floor % 5)] = "="
        LEVELS[map_index][8, 9 - ((pure_deadly_floor - 1) % 5)] = "."
    elif map_index == 7:
        LEVELS[map_index][11, 1 + ((spike_count - 1) % 11)] = LEVELS_START[map_index][11, 1 + ((spike_count - 1) % 11)]
        LEVELS[map_index][11, 1 + (spike_count % 11)] = "*"
        LEVELS[map_index][11, 1 + ((spike_count + 1) % 11)] = LEVELS_START[map_index][11, 1 + ((spike_count + 1) % 11)]
        LEVELS[map_index][11, 1 + ((spike_count + 2) % 11)] = "*"
        LEVELS[map_index][9, 13 - ((spike_count + 2) % 13)] = LEVELS_START[map_index][9, 13 - ((spike_count + 2) % 13)]
        LEVELS[map_index][9, 13 - ((spike_count + 3) % 13)] = "*"
        LEVELS[map_index][9, 13 - ((spike_count + 4) % 13)] = LEVELS_START[map_index][9, 13 - ((spike_count + 4) % 13)]
        LEVELS[map_index][9, 13 - ((spike_count + 5) % 13)] = "*"
        LEVELS[map_index][7, 1 + ((spike_count + 3) % 13)] = LEVELS_START[map_index][7, 1 + ((spike_count + 3) % 13)]
        LEVELS[map_index][7, 1 + ((spike_count + 4) % 13)] = "*"
        LEVELS[map_index][7, 1 + ((spike_count + 5) % 13)] = LEVELS_START[map_index][7, 1 + ((spike_count + 5) % 13)]
        LEVELS[map_index][7, 1 + ((spike_count + 6) % 13)] = "*"
        LEVELS[map_index][5, 13 - ((spike_count - 1) % 13)] = LEVELS_START[map_index][5, 13 - ((spike_count - 1) % 13)]
        LEVELS[map_index][5, 13 - (spike_count % 13)] = "*"
        LEVELS[map_index][5, 13 - ((spike_count + 1) % 13)] = LEVELS_START[map_index][5, 13 - ((spike_count + 1) % 13)]
        LEVELS[map_index][5, 13 - ((spike_count + 2) % 13)] = "*"
        LEVELS[map_index][3, 1 + ((spike_count + 7) % 13)] = LEVELS_START[map_index][3, 1 + ((spike_count + 7) % 13)]
        LEVELS[map_index][3, 1 + ((spike_count + 8) % 13)] = "*"
        LEVELS[map_index][3, 1 + ((spike_count + 9) % 13)] = LEVELS_START[map_index][3, 1 + ((spike_count + 9) % 13)]
        LEVELS[map_index][3, 1 + ((spike_count + 10) % 13)] = "*"
        if LEVELS[map_index][0, 1] == "*" and latch_arr[0] == 0:
            LEVELS[map_index][12, 1] = "B"
            latch_arr[0] = 1
            print_level(L)
        elif LEVELS[map_index][14, 1] == "*" and latch_arr[1] == 0:
            LEVELS[map_index][12, 3] = "B"
            latch_arr[1] = 1
            print_level()
        elif LEVELS[map_index][0, 3] == "*" and latch_arr[2] == 0:
            LEVELS[map_index][2, 5] = "B"
            latch_arr[2] = 1
            print_level()
        elif LEVELS[map_index][14, 5] == "*" and latch_arr[3] == 0:
            LEVELS[map_index][12, 7] = "B"
            latch_arr[3] = 1
            print_level()
        elif LEVELS[map_index][0, 7] == "*" and latch_arr[4] == 0:
            LEVELS[map_index][2, 9] = "B"
            latch_arr[4] = 1
            print_level()
        elif LEVELS[map_index][14, 9] == "*" and latch_arr[5] == 0:
            LEVELS[map_index][12, 11] = "B"
            latch_arr[5] = 1
            print_level()
        elif LEVELS[map_index][0, 11] == "*" and latch_arr[6] == 0:
            LEVELS[map_index][2, 13] = "B"
            latch_arr[6] = 1
            print_level()
        spike_count += 1
    elif map_index == 8:
        LEVELS[map_index][13, 4 + ((spike_count - 2) % 9)] = "."
        LEVELS[map_index][13, 4 + (spike_count % 9)] = "*"
        LEVELS[map_index][13 - ((spike_count + 6) % 13), 13] = "."
        LEVELS[map_index][13 - ((spike_count + 8) % 13), 13] = "*"
        LEVELS[map_index][1, 13 - ((spike_count + 5) % 13)] = "."
        LEVELS[map_index][1, 13 - ((spike_count + 7) % 13)] = "*"
        LEVELS[map_index][1 + (spike_count % 11), 1] = "."
        LEVELS[map_index][1 + ((spike_count + 2) % 11), 1] = "*"
        LEVELS[map_index][11, 1 + ((spike_count + 4) % 11)] = "."
        LEVELS[map_index][11, 1 + ((spike_count + 6) % 11)] = "*"
        LEVELS[map_index][11 - ((spike_count + 4) % 9), 11] = "."
        LEVELS[map_index][11 - ((spike_count + 6) % 9), 11] = "*"
        LEVELS[map_index][3, 11 - ((spike_count + 2) % 9)] = "."
        LEVELS[map_index][3, 11 - ((spike_count + 4) % 9)] = "*"
        LEVELS[map_index][3 + ((spike_count + 4) % 7), 3] = "."
        LEVELS[map_index][3 + ((spike_count + 6) % 7), 3] = "*"
        LEVELS[map_index][9, 3 + ((spike_count + 2) % 7)] = "."
        LEVELS[map_index][9, 3 + ((spike_count + 4) % 7)] = "*"
        spike_count += 2
    elif map_index == 9:
        if LEVELS[map_index][7, 8] == "@":
            input('Demo made by Rea "Tuxware"')
            print_level()

clear_screen()
print("  .,-::::: :::::::..    :::.  .::    .   .::::::    .,:::::: :::::::..   ")
print(",;;;'````' ;;;;``;;;;   ;;`;; ';;,  ;;  ;;;' ;;;    ;;;;'''' ;;;;``;;;;  ")
print("[[[         [[[,/[[['  ,[[ '[[,'[[, [[, [['  [[[     [[cccc   [[[,/[[['  ")
print("$$$         $$$$$$c   c$$$cc$$$c Y$c$$$c$P   $$'     $$\"\"\"\"   $$$$$$c    ")
print("`88bo,__,o, 888b \"88bo,888   888, \"88\"888   o88oo,.__888oo,__ 888b \"88bo,")
print('  "YUMMMMMP"MMMM   "W" YMM   ""`   "M "M"   """"YUMMM""""YUMMMMMMM   "W" ')
print("1. Easy")
print("2. Medium")
print("3. Hard")
print("4. Impossible")
print("Select difficulty: ")

try:
    mode = int(getch.getch())
except ValueError:
    mode = 1
except OverflowError:
    pass

try:
    while True:
        if tic == True:
            print_level()
            map_specific_events()
        try:
            character_input()
        except OverflowError:
            pass
except KeyboardInterrupt:
    clear_screen()
    sys.exit()
