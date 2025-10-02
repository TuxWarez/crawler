import numpy as np
import copy, os, getch, sys

key_ammount = 0; move_count = 0; map_index = 0
barrel_spawned = 0; deadly_floor = [0, 1, 2]; pure_deadly_floor = 2; pure_deadly_floor_plus = 3
x_coord = 12; y_coord = 11
coords = np.array([[12, 11], [10, 10], [4, 13], [4, 15], [5, 13], [10, 14], [9, 11]])
mode = 0; tic = True; space = " "
showpos = 0; noclip = 0; god = 0
WALLS = np.array(['═', '║', '╚', '╝', '╔', '╗', '╠', '╣', '╩', '╦'])
LEVEL_TITLECARD = np.array(["LVL01: Introduction", "LVL02: Four way", "LVL03: Boxes", "LVL04: Buttons", "LVL05: Barb Wire", "LVL06: Teleportation", "THX: Thanks for playing!"])

lvl01 = np.array([['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '╔', '═', '╗', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║', 'E', '║', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║', 'D', '║', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '╔', '═', '═', '╝', '.', '║', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '║', 'K', '.', '.', '@', '║', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '╚', '═', '═', '═', '═', '╝', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']])
lvl01_start = copy.deepcopy(lvl01)

lvl02 = np.array([['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '╔', '═', '═', '═', '═', '═', '╗', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '║', 'D', '.', '.', '.', '.', '║', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '║', 'K', '╦', '.', '╦', 'D', '║', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '║', 'K', '║', '.', '║', '.', '║', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '╔', '═', '═', '═', '╬', '═', '╣', '.', '╠', '═', '╬', '═', '═', '═', '╗', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', 'K', '║', '█', '║', '.', '║', '█', '║', 'E', 'D', '.', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '╠', '═', '╩', '═', '╝', '.', '╚', '═', '╩', '═', '╣', '.', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', 'K', 'K', 'D', 'D', '.', '@', '.', '.', '.', 'D', 'D', '.', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '╠', '═', '╦', '═', '╗', '.', '╔', '═', '╦', '═', '╣', '.', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', 'K', '║', '█', '║', '.', '║', '█', '║', 'E', 'D', '.', '║', '.', '.', '.'],
                  ['.', '.', '.', '╚', '═', '═', '═', '╬', '═', '╣', '.', '╠', '═', '╬', '═', '═', '═', '╝', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '║', '.', '║', '.', '║', 'K', '║', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '║', 'D', '╩', '.', '╩', '.', '║', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '║', '.', '.', '.', '.', '.', '║', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '╚', '═', '═', '═', '═', '═', '╝', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],])
lvl02_start = copy.deepcopy(lvl02)

lvl03 = np.array([['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '╔', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╗', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '║', '.', '.', '.', '.', '.', '.', '.', '.', 'H', '.', 'E', '║', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '║', '.', '╔', '╗', '.', '╔', '╗', '.', '╔', '═', '═', '═', '╝', '.', '.', '.'],
                  ['.', '.', '.', '.', '╔', '╝', '.', '╚', '╝', '.', '╚', '╝', '.', '║', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '║', '.', 'B', '.', '.', 'B', '.', '.', 'B', '║', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '╚', '╗', '.', '╔', '╗', '.', '╔', '╗', '.', '║', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '╔', '═', '╝', '.', '╚', '╝', '.', '╚', '╝', '.', '║', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '║', '@', '.', '.', '.', '.', '.', '.', '.', '.', '║', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '╚', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╝', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']])
lvl03_start = copy.deepcopy(lvl03)

lvl04 = np.array([['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '╔', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╗', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', 'E', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '╔', '═', '╝', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '╔', '═', '╗', '.', '╔', '═', '╗', '.', '.', '║', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '║', '.', '.', '.', '.', '.', '║', '.', '.', '║', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '╚', '.', '.', '.', '.', '.', '╝', '.', '.', '║', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '.', '.', '.', 'o', '.', '.', '.', 'B', '.', '║', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '╔', '.', '.', '.', '.', '.', '╗', '.', '.', '║', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '║', '.', '.', '.', '.', '.', '║', '.', '.', '║', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '╚', '═', '╝', '.', '╚', '═', '╝', '.', '.', '║', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '║', '@', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '╚', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╝', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']])
lvl04_start = copy.deepcopy(lvl04)

lvl05 = np.array([['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '*', '*', '*', '*', '*', '.', '.', '.', '*', '*', '*', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '*', '.', '.', '.', '*', '.', '.', '.', '*', 'o', '*', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '*', '.', '*', '.', '*', '*', '*', '*', '*', '.', '*', '*', '*', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '.', '║', '.', '║', '.', '*', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '*', '.', '*', '*', '*', '*', '.', '*', '*', '.', '*', '.', '*', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '*', '.', '*', '.', '.', '*', '.', '*', '*', '.', '║', '.', '*', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '*', '.', '*', '.', '.', '*', '*', '*', '*', '.', '*', '*', '*', '.', '.', '.'],
                  ['.', '.', '.', '.', '*', '*', '.', '*', '.', '.', '.', '*', '*', '*', '.', '*', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '*', 'E', 'H', '*', '.', '.', '.', '*', '.', '.', '.', '*', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '.', '*', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '*', '@', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '*', '*', '*', '*', '*', '*', '*', '*', '.', '*', '.', '*', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '*', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '*', '*', '*', '*', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']])
lvl05_start = copy.deepcopy(lvl05)

lvl06 = np.array([['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '╔', '═', '╗', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '╔', '═', '╗', '.', '║', 'T', '║', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '║', 'T', '╠', '═', '╝', '.', '╚', '═', '╦', '═', '╗', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '║', '.', '║', '.', '.', '.', '.', '.', '║', 'K', '║', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '║', '.', '╩', '.', '.', '.', '.', '.', '╠', '═', '╣', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '║', '.', 'B', '.', '.', '.', '.', '.', '.', 'o', '║', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '╠', '═', '╣', '.', '.', '.', '.', '.', '╔', '═', '╝', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '║', 'E', 'D', '.', '.', '.', '.', '.', '║', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '╚', '═', '═', '═', '╗', '.', '╔', '═', '╝', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '║', '@', '║', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '╚', '═', '╝', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']])
lvl06_start = copy.deepcopy(lvl06)

lvl07 = np.array([['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '╔', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╗', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '═', '═', '╦', '═', '═', '.', '.', '.', '.', '.', '.', '.', '.', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '║', '.', '.', '.', '║', '.', '║', '.', '║', '.', '║', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '║', '.', '.', '.', '║', '.', '║', '.', '║', '.', '║', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '║', '.', '.', '.', '║', 'C', '║', '.', '║', '.', '║', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '║', '.', '.', '@', '╠', '═', '╣', '.', '╚', '╦', '╝', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '║', '.', '.', '.', '║', '.', '║', '.', '╔', '╩', '╗', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '║', '.', '.', '.', '║', '.', '║', '.', '║', '.', '║', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '║', '.', '.', '.', '║', '.', '║', '.', '║', '.', '║', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '║', '.', '.', '.', '║', '.', '║', '.', '║', '.', '║', '║', '.', '.', '.'],
                  ['.', '.', '.', '║', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '║', '.', '.', '.'],
                  ['.', '.', '.', '╚', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╝', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']])
lvl07_start = copy.deepcopy(lvl07)

LEVELS = np.array([lvl01, lvl02, lvl03, lvl04, lvl05, lvl06, lvl07])
LEVELS_START = np.array([lvl01_start, lvl02_start, lvl03_start, lvl04_start, lvl05_start, lvl06_start, lvl07_start])

def clear_screen():
    if sys.platform == "win32":
        os.system("cls")
        return
    os.system("clear")

def print_level(level):
    global mode, showpos, space
    clear_screen()
    if mode == 1:
        for i in range(3, 18):
            for j in range(3, 18):
                print(LEVELS[map_index][i, j], end=space)
            print()
    elif mode == 3:
        for i in range(y_coord - 2, y_coord + 3):
            for j in range(x_coord - 2, x_coord + 3):
                print(LEVELS[map_index][i, j], end=space)
            print()
    elif mode == 4:
        for i in range(y_coord - 1, y_coord + 2):
            for j in range(x_coord - 1, x_coord + 2):
                print(LEVELS[map_index][i, j], end=space)
            print()
    else:
        for i in range(y_coord - 4, y_coord + 5):
            for j in range(x_coord - 4, x_coord + 5):
                print(LEVELS[map_index][i, j], end=space)
            print()
    print(LEVEL_TITLECARD[map_index])
    print(f"KEYS={key_ammount} MOVES={move_count}")
    if showpos == 1:
        print(f"{x_coord}, {y_coord}")

def character_movement(x_dir, y_dir):
    global key_ammount, map_index, y_coord, x_coord, move_count, barrel_spawned, tic, noclip, god
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
            elif LEVELS[map_index][y_coord + y_dir + y_dir, x_coord + x_dir + x_dir] == "*" or LEVELS[map_index][y_coord + y_dir + y_dir, x_coord + x_dir + x_dir] == "o":
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
        print_level(LEVELS[map_index])
        input("You fell down a hole...")
        move_count = 0
        key_ammount = 0
        barrel_spawned = 0
        x_coord, y_coord = coords[map_index, 0], coords[map_index, 1]
        LEVELS[map_index] = copy.deepcopy(LEVELS_START[map_index])
        return
    elif LEVELS[map_index][y_coord + y_dir, x_coord + x_dir] == "*" and god == 0:
        LEVELS[map_index][y_coord, x_coord] = "X"
        print_level(LEVELS[map_index])
        input("You Died...")
        move_count = 0
        key_ammount = 0
        barrel_spawned = 0
        x_coord, y_coord = coords[map_index, 0], coords[map_index, 1]
        LEVELS[map_index] = copy.deepcopy(LEVELS_START[map_index])
        return
    elif LEVELS[map_index][y_coord + y_dir, x_coord + x_dir] == "E" and noclip == 0:
        LEVELS[map_index] = copy.deepcopy(LEVELS_START[map_index])
        map_index += 1
        x_coord, y_coord = coords[map_index, 0], coords[map_index, 1]
        move_count = 0
        barrel_spawned = 0
        key_ammount = 0
        return
    x_coord += x_dir; y_coord += y_dir
    LEVELS[map_index][y_coord, x_coord] = "@"
    if LEVELS[map_index][y_coord - y_dir, x_coord - x_dir] != "*":
        LEVELS[map_index][y_coord - y_dir, x_coord - x_dir] = "."
    if noclip == 1:
         LEVELS[map_index][y_coord - y_dir, x_coord - x_dir] = LEVELS_START[map_index][y_coord - y_dir, x_coord - x_dir]
    tic = True

def character_input():
    global key_ammount, map_index, y_coord, x_coord, move_count, tic, showpos, noclip, god, mode, space
    action = getch.getch()
    if action == "r" or action == "R":
        move_count = 0
        key_ammount = 0
        x_coord, y_coord = coords[map_index, 0], coords[map_index, 1]
        LEVELS[map_index] = copy.deepcopy(LEVELS_START[map_index])
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
        print("H - Hole: Kills the player, can be filled by a box")
        print("o/O - Ground button: Can be pushed by a box")
        print("D - Door: Needs a key to open it and takes one from you")
        print("B - Box: Used for filling holes and pressing buttons")
        print("* - Deadly tile: Kills the player and destroys boxes")
        print("Controls:")
        print("WASD for movement of the player")
        print("R to restart level")
        print("C for the console, for which you can find instructions on the github page")
        input("Press Enter to exit this screen")
    elif action == "c" or action == "C":
        print("Input a command:")
        try:
            command = input().split(" ")
            if command[0] == "changelvl":
                if len(command) < 2:
                    input("No arguments present")
                    return
                elif int(command[1]) > len(LEVELS):
                    input("Map of that index doesnt exist")
                    return
                map_index = int(command[1]) - 1
                key_ammount = 0
                x_coord, y_coord = coords[map_index, 0], coords[map_index, 1]
                move_count = 0
            elif command[0] == "setpos":
                if len(command) < 3:
                    input("Not enough arguments present")
                    return
                elif int(command[1]) >= 17 or int(command[2]) >= 17 or int(command[1]) <= -18 or int(command[2]) <= -18:
                    input("This coordinate is beyond reach")
                    return
                LEVELS[map_index][y_coord, x_coord] = "."
                x_coord, y_coord = int(command[1]), int(command[2])
                LEVELS[map_index][y_coord, x_coord] = "@"
            elif command[0] == "startpos":
                LEVELS[map_index][y_coord, x_coord] = "."
                x_coord, y_coord = coords[map_index, 0], coords[map_index, 1]
                LEVELS[map_index][y_coord, x_coord] = "@"
            elif command[0] == "showpos":
                if len(command) < 2:
                    input("No arguments present")
                    return
                showpos = int(command[1])
            elif command[0] == "noclip":
                if len(command) < 2:
                    input("No arguments present")
                    return
                noclip = int(command[1])
            elif command[0] == "god":
                if len(command) < 2:
                    input("No arguments present")
                    return
                god = int(command[1])
            elif command[0] == "summon":
                if len(command) < 2 or len(command) == 3:
                    input("No arguments present")
                    return
                elif len(command) == 4:
                    if int(command[2]) >= 17 or int(command[3]) >= 17 or int(command[2]) <= -18 or int(command[3]) <= -18:
                        input("This coordinate is beyond reach")
                        return
                    LEVELS[map_index][int(command[3]), int(command[2])] = command[1]
                    return
                LEVELS[map_index][y_coord + 1, x_coord] = command[1]
            elif command[0] == "setkey":
                if len(command) < 2:
                    input("No arguments present")
                    return
                key_ammount = int(command[1])
            elif command[0] == "changedif":
                if len(command) < 2:
                    input("No arguments present")
                    return
                mode = int(command[1])
            elif command[0] == "setmove":
                if len(command) < 2:
                    input("No arguments present")
                    return
                move_count = int(command[1])
            elif command[0] == "space":
                if len(command) < 2:
                    input("No arguments present")
                    return
                if command[1] == "1":
                    space = " "
                    return
                space = ""
        except ValueError:
                input("There is no digit")
    tic = False

def map_specific_events():
    global map_index, move_count, barrel_spawned, deadly_floor, absolute_deadly_floor, pure_deadly_floor, absolute_deadly_floor_plus, pure_deadly_floor_plus, x_coord, y_coord, tic
    if map_index == 3:
        absolute_deadly_floor = abs(pure_deadly_floor - 2)
        absolute_deadly_floor_plus = abs(pure_deadly_floor_plus - 2)
        LEVELS[map_index][11 - absolute_deadly_floor_plus, 9 + absolute_deadly_floor - 1] = "."
        pure_deadly_floor = (pure_deadly_floor + 1) % 4
        absolute_deadly_floor = abs(pure_deadly_floor - 2)
        pure_deadly_floor_plus = (pure_deadly_floor_plus + 1) % 4
        absolute_deadly_floor_plus = abs(pure_deadly_floor_plus - 2)
        LEVELS[map_index][11 - absolute_deadly_floor_plus, 9 + absolute_deadly_floor - 1] = "*"
        if LEVELS[map_index][10, 9] == "*":
            if barrel_spawned == 0:
                LEVELS[map_index][11, 8] = "B"
                LEVELS[map_index][9, 8] = "B"
                LEVELS[map_index][9, 10] = "B"
                LEVELS[map_index][11, 10] = "B"
                barrel_spawned = 1
            for i in range(2):
                for j in range(2):
                    if LEVELS[map_index][8 + (i*4), 7 + (j*4)] != "B":
                        LEVELS[map_index][8 + (i*4), 7 + (j*4)] = "O"
            if np.count_nonzero(LEVELS[map_index] == "O") == 0:
                if LEVELS[map_index][5, 15] != "@":
                    LEVELS[map_index][5, 15] = "."
    elif map_index == 4:
        if LEVELS[map_index][4, 14] == "*":
            if barrel_spawned == 0:
                LEVELS[map_index][14, 14] = "B"
                barrel_spawned = 1
            if LEVELS[map_index][6, 13] != "B":
                LEVELS[map_index][6, 13] = "."
            LEVELS[map_index][6, 15] = "."
            LEVELS[map_index][8, 15] = "."
        absolute_deadly_floor = abs(pure_deadly_floor - 2)
        LEVELS[map_index][11, 13 + absolute_deadly_floor - 1] = "."
        LEVELS[map_index][7 + absolute_deadly_floor - 1, 11] = "."
        pure_deadly_floor = (pure_deadly_floor + 1) % 4
        absolute_deadly_floor = abs(pure_deadly_floor - 2)
        LEVELS[map_index][7 + absolute_deadly_floor - 1, 11] = "*"
        LEVELS[map_index][11, 13 + absolute_deadly_floor - 1] = "*"
    elif map_index == 5:
        LEVELS[map_index][6, 10] = "T"
        LEVELS[map_index][7, 6] = "T"
        if x_coord == 6 and y_coord == 7:
            x_coord = 10; y_coord = 6
            LEVELS[map_index][6, 10] = "@"
            print_level(LEVELS[map_index])
            return
        elif x_coord == 10 and y_coord == 6:
            x_coord = 6; y_coord = 7
            LEVELS[map_index][7, 6] = "@"
            print_level(LEVELS[map_index])
            return
        pure_deadly_floor += 1
        if LEVELS[map_index][10, 14] == "*":
            LEVELS[map_index][8, 13] = "."
        # Moving killing floors
        LEVELS[map_index][12 - (pure_deadly_floor % 5), 9] = "*"
        LEVELS[map_index][12 - ((pure_deadly_floor - 1) % 5), 9] = "."
        LEVELS[map_index][12 - ((pure_deadly_floor + 1) % 5), 11] = "*"
        LEVELS[map_index][12 - (pure_deadly_floor % 5), 11] = "."
        LEVELS[map_index][9, 12 - ((pure_deadly_floor + 1) % 5)] = "*"
        LEVELS[map_index][9, 12 - (pure_deadly_floor % 5)] = "."
        LEVELS[map_index][11, 12 - (pure_deadly_floor % 5)] = "*"
        LEVELS[map_index][11, 12 - ((pure_deadly_floor - 1) % 5)] = "."
    elif map_index == 6:
        if LEVELS[map_index][10, 11] == "@":
            input('Game made by Rhea "Tuxware"')
            print_level(LEVELS[map_index])

clear_screen()
print("1. Easy")
print("2. Medium")
print("3. Hard")
print("4. Impossible")
dif = input("Select difficulty: ")

if dif == "1":
    mode = 1
elif dif == "3":
    mode = 3
elif dif == "4":
    mode = 4

while True:
    print_level(LEVELS[map_index])
    if tic == True:
        map_specific_events()
    character_input()
