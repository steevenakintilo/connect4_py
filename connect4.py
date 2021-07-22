#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## d
## File description:
## d
##

import sys
from termcolor import colored, cprint
from os import system
from random import randint

system("clear")
def print_blue(c):
    print("\033[1;34;40m%s  \n" % (c))

def random_nbr(nb,res):
    if nb == 1:
         return(randint(res, res + 1))
    if nb != 1:
        return(randint(1, 7))
pass

def print_empty_board(list,name1,name2,play):
    n1 = colored(name1, 'red')
    n2 = colored(name2, 'yellow')
    p = colored(play, 'blue')
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[0],list[1],list[2],list[3],list[4],list[5],list[6]))
    print("|-----|-----|-----|-----|-----|-----|-----|")
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[7],list[8],list[9],list[10],list[11],list[12],list[13]))
    print("|-----|-----|-----|-----|-----|-----|-----|")
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[14],list[15],list[16],list[17],list[18],list[19],list[20]))
    print("|-----|-----|-----|-----|-----|-----|-----|                %s VS %s" % (n1,n2))
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[21],list[22],list[23],list[24],list[25],list[26],list[27]))
    print("|-----|-----|-----|-----|-----|-----|-----|")
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[28],list[29],list[30],list[31],list[32],list[33],list[34]))
    print("|-----|-----|-----|-----|-----|-----|-----|                Nombre de coups joué %s" % (p))
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[35],list[36],list[37],list[38],list[39],list[40],list[41]))
    print("   1     2     3     4     5     6     7   ")

def restart(mod):
    empty_board = []
    for i in range(42):
        empty_board.append(" ")
    r = input("Appuie sur O pour rejouer et Q pour quitter: ")
    if r == "Q":
        quit()
    if r == "O" and mod == 1:
        system("clear")
        print_empty_board(empty_board, name1, name2, 0)
        connect4_vs()
    if r == "O" and mod == 2:
        system("clear")
        print_empty_board(empty_board, name1, name2, 0)
        connect4_ia()

def print_table(TABLE):
    for r in TABLE:
        for c in r:
            print(c,end = "   ")
        print()
    pass

def print_board(list,name1,name2,play):
    n1 = colored(name1, 'red')
    n2 = colored(name2, 'yellow')
    p = colored(play, 'blue')
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[0],list[1],list[2],list[3],list[4],list[5],list[6]))
    print("|-----|-----|-----|-----|-----|-----|-----|")
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[7],list[8],list[9],list[10],list[11],list[12],list[13]))
    print("|-----|-----|-----|-----|-----|-----|-----|")
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[14],list[15],list[16],list[17],list[18],list[19],list[20]))
    print("|-----|-----|-----|-----|-----|-----|-----|                %s VS %s" % (n1,n2))
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[21],list[22],list[23],list[24],list[25],list[26],list[27]))
    print("|-----|-----|-----|-----|-----|-----|-----|")
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[28],list[29],list[30],list[31],list[32],list[33],list[34]))
    print("|-----|-----|-----|-----|-----|-----|-----|                Nombre de coups joué %s" % (p))
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[35],list[36],list[37],list[38],list[39],list[40],list[41]))
    print("   1     2     3     4     5     6     7   ")

def connect4_vs():
    board = []
    j = 0
    for i in range(42):
        board.append(" ")
    empty_list = [" "," "," "," "," "," "]
    p1 = ["\x1b[31mX\x1b[0m","\x1b[31mX\x1b[0m","\x1b[31mX\x1b[0m","\x1b[31mX\x1b[0m"]
    p2 = ["\x1b[33mO\x1b[0m","\x1b[33mO\x1b[0m","\x1b[33mO\x1b[0m","\x1b[33mO\x1b[0m"]
    b1 =  [board[35],board[28],board[21],board[14],board[7],board[0]]
    b2 =  [board[36],board[29],board[22],board[15],board[8],board[1]]
    b3 =  [board[37],board[30],board[23],board[16],board[9],board[2]]
    b4 =  [board[38],board[31],board[24],board[17],board[10],board[3]]
    b5 =  [board[39],board[32],board[25],board[18],board[11],board[4]]
    b6 =  [board[40],board[33],board[26],board[19],board[12],board[5]]
    b7 =  [board[41],board[34],board[27],board[20],board[13],board[6]]
    print(b1[0])
    i = 0
    idx = 0
    check1 = 0
    check2 = 0
    check3 = 0
    check4 = 0
    check5 = 0
    check6 = 0
    check7 = 0
    draw = 0
    play = 0
    while True:
        val = input("%s choisi une colonne: " % (n1))
        if  check1 >= 42 and val == "1" or check2 >= 42 and val == "2" or check3 >= 42 and val == "3" or check4 >= 42 and val == "4" or check5 >= 42 and val == "5" or check6 >= 42 and val == "6" or check7 >= 42 and val == "7" :
            print("Erreur la colonne est pleine")
            val = input("%s choisi une colonne: " % (n1))
        if int(val) < 1 or int(val) > 7:
            print("Erreur tu dois choisir entre parmis les colonnes 1 à 7")
            val = input("%s choisi une colonne: " % (n1))
        if val == "1" and check1 <= 42:
            for i in b1:
                if b1 == empty_list:
                    board[35 - check1] = "X"
                    board[35 - check1] = colored(board[35 - check1], 'red')
                    play = play + 1
            check1 = check1 + 7
        if val == "2" and check2 <= 42:
            for i in b2:
                if b2 == empty_list:
                    board[36 - check2] = "X"
                    board[36 - check2] = colored(board[36 - check2], 'red')
                    play = play + 1
            check2 = check2 + 7
        if val == "3" and check3 <= 42:
            for i in b3:
                if b3 == empty_list:
                    board[37 - check3] = "X"
                    board[37 - check3] = colored(board[37 - check3], 'red')
                    play = play + 1
            check3 = check3 + 7
        if val == "4":
            for i in b4:
                if b4 == empty_list:
                    board[38 - check4] = "X"
                    board[38 - check4] = colored(board[38 - check4], 'red')
                    play = play + 1
            check4 = check4 + 7
        if val == "5":
            for i in b5:
                if b5 == empty_list:
                    board[39 - check5] = "X"
                    board[39 - check5] = colored(board[39 - check5], 'red')
                    play = play + 1
            check5 = check5 + 7
        if val == "6":
            for i in b6:
                if b6 == empty_list:
                    board[40 - check6] = "X"
                    board[40 - check6] = colored(board[40 - check6], 'red')
                    play = play + 1
            check6 = check6 + 7
        if val == "7":
            for i in b7:
                if b7 == empty_list:
                    board[41 - check7] = "X"
                    board[41 - check7] = colored(board[41 - check7], 'red')
                    play = play + 1
            check7 = check7 + 7
        w = [board[35],board[36],board[37],board[38]]
        w2 = [board[36],board[37],board[38],board[39]]
        w3 = [board[37],board[38],board[39],board[40]]
        w4 = [board[38],board[39],board[40],board[41]]
        w5 = [board[28],board[29],board[30],board[31]]
        w6 = [board[29],board[30],board[31],board[32]]
        w7 = [board[30],board[31],board[32],board[33]]
        w8 = [board[31],board[32],board[33],board[34]]
        w9 = [board[21],board[22],board[23],board[24]]
        w10 = [board[22],board[23],board[24],board[25]]
        w11 = [board[23],board[24],board[25],board[26]]
        w12 = [board[24],board[25],board[26],board[27]]
        w13 = [board[14],board[15],board[16],board[17]]
        w14 = [board[15],board[16],board[17],board[18]]
        w15 = [board[16],board[17],board[18],board[19]]
        w16 = [board[17],board[18],board[19],board[20]]
        w17 = [board[7],board[8],board[9],board[10]]
        w18 = [board[8],board[9],board[10],board[11]]
        w19 = [board[9],board[10],board[11],board[12]]
        w20 = [board[10],board[11],board[12],board[13]]
        w21 = [board[35],board[28],board[21],board[14]]
        w22 = [board[36],board[29],board[22],board[15]]
        w23 = [board[37],board[30],board[23],board[16]]
        w24 = [board[38],board[31],board[24],board[17]]
        w25 = [board[28],board[21],board[14],board[7]]
        w26 = [board[29],board[22],board[15],board[8]]
        w27 = [board[30],board[23],board[16],board[9]]
        w28 = [board[31],board[24],board[17],board[10]]
        w29 = [board[21],board[14],board[7],board[0]]
        w30 = [board[22],board[15],board[8],board[1]]
        w31 = [board[23],board[16],board[9],board[2]]
        w32 = [board[24],board[17],board[10],board[3]]
        w33 = [board[39],board[32],board[25],board[18]]
        w34 = [board[40],board[33],board[26],board[19]]
        w35 = [board[41],board[34],board[27],board[20]]
        w36 = [board[32],board[25],board[18],board[11]]
        w37 = [board[33],board[26],board[19],board[12]]
        w38 = [board[34],board[27],board[20],board[13]]
        w39 = [board[25],board[18],board[11],board[4]]
        w40 = [board[26],board[19],board[12],board[5]]
        w41 = [board[27],board[20],board[13],board[6]]
        w42 = [board[35],board[29],board[23],board[17]]
        w43 = [board[29],board[23],board[17],board[11]]
        w44 = [board[23],board[17],board[11],board[5]]
        w45 = [board[36],board[30],board[24],board[18]]
        w46 = [board[30],board[24],board[18],board[12]]
        w47 = [board[24],board[18],board[12],board[6]]
        w48 = [board[37],board[31],board[25],board[19]]
        w49 = [board[31],board[25],board[19],board[13]]
        w50 = [board[38],board[32],board[26],board[20]]
        w51 = [board[28],board[22],board[16],board[10]]
        w52 = [board[22],board[16],board[10],board[4]]
        w53 = [board[21],board[15],board[9],board[3]]
        w54 = [board[41],board[33],board[25],board[17]]
        w55 = [board[33],board[25],board[17],board[9]]
        w56 = [board[25],board[17],board[9],board[1]]
        w57 = [board[40],board[32],board[24],board[16]]
        w58 = [board[32],board[24],board[16],board[8]]
        w59 = [board[24],board[16],board[8],board[0]]
        w60 = [board[39],board[31],board[23],board[15]]
        w61 = [board[31],board[23],board[15],board[7]]
        w62 = [board[38],board[30],board[22],board[14]]
        w63 = [board[34],board[26],board[18],board[10]]
        w64 = [board[26],board[18],board[10],board[2]]
        w65 = [board[27],board[19],board[11],board[3]]
        w66 = [board[6],board[12],board[18],board[24]]
        w67 = [board[12],board[18],board[24],board[30]]
        w68 = [board[18],board[24],board[30],board[36]]
        w69 = [board[5],board[11],board[17],board[23]]
        w70 = [board[11],board[17],board[23],board[29]]
        w71 = [board[17],board[23],board[29],board[35]]
        w72 = [board[4],board[10],board[16],board[22]]
        w73 = [board[10],board[16],board[22],board[28]]
        w74 = [board[3],board[9],board[15],board[21]]
        w75 = [board[13],board[19],board[25],board[31]]
        w76 = [board[19],board[25],board[31],board[37]]
        w77 = [board[35],board[36],board[37],board[38]]
        w78 = [board[0],board[8],board[16],board[24]]
        w79 = [board[8],board[16],board[24],board[32]]
        w80 = [board[16],board[24],board[32],board[40]]
        w81 = [board[1],board[9],board[17],board[25]]
        w82 = [board[9],board[17],board[25],board[33]]
        w83 = [board[17],board[25],board[33],board[41]]
        w84 = [board[2],board[10],board[18],board[26]]
        w85 = [board[10],board[18],board[26],board[34]]
        w86 = [board[3],board[11],board[19],board[27]]
        w87 = [board[7],board[15],board[23],board[31]]
        w88 = [board[15],board[23],board[31],board[39]]
        w89 = [board[14],board[22],board[30],board[38]]
        if w == p1 or w2 == p1 or w3 == p1 or w4 == p1 or w5 == p1 or w6 == p1 or w7 == p1 or w8 == p1 or w9 == p1 or w10 == p1 or w11 == p1 or w12 == p1 or w13 == p1 or w14 == p1 or w15 == p1 or w16 == p1 or w17 == p1 or w18 == p1 or w19 == p1 or w20 == p1 or w21 == p1 or w22 == p1  or w23 == p1 or w24 == p1 or w25 == p1 or w26 == p1 or w27 == p1 or w28 == p1 or w29 == p1 or w30 == p1 or w31 == p1 or w32 == p1 or w33 == p1 or w34 == p1 or w35 == p1 or w36 == p1 or w37 == p1 or w38 == p1 or w39 == p1 or w40 == p1 or w41 == p1 or w42 == p1 or w43 == p1 or w44 == p1 or w45 == p1 or w46 == p1 or w47 == p1 or w48 == p1 or w49 == p1 or w50 == p1 or w51 == p1 or w52 == p1 or w53 == p1 or w54 == p1 or w55 == p1 or w56 == p1 or w57 == p1 or w58 == p1 or w59 == p1 or w60 == p1 or w61 == p1 or w62 == p1 or w63 == p1 or w64 == p1 or w65 == p1 or w66 == p1 or w67 == p1 or w68 == p1 or w69 == p1 or w70 == p1 or w71 == p1 or w72 == p1 or w73 == p1 or w74 == p1 or w75 == p1 or w76 == p1 or w77 == p1 or w78 == p1 or w79 == p1 or w80 == p1 or w81 == p1 or w82 == p1 or w83 == p1 or w84 == p1 or w85 == p1 or w86 == p1 or w87 == p1 or w88 == p1 or w89 == p1:
            print_board(board,name1,name2,play/6)
            print("%s tu as gagnes!!!" % (n1))
            restart(1)
        if play == 252:
            print_board(board,name1,name2,play/6)
            print("Egalite")
            restart(1)
        print_board(board,name1,name2,play/6)
        val2 = input("%s choisi une colonne: " % (n2))    
        if int(val2) < 1 or int(val2) > 7:
            print("Erreur tu dois choisir entre parmis les colonnes 1 à 7")
            val2 = input("%s choisi une colonne: " % (n2))
        if  check1 >= 42 and val2 == "1" or check2 >= 42 and val2 == "2" or check3 >= 42 and val2 == "3" or check4 >= 42 and val2 == "4" or check5 >= 42 and val2 == "5" or check6 >= 42 and val2 == "6" or check7 >= 42 and val2 == "7" :
            print("Erreur la colonne est pleine")
            val2 = input("%s choisi une colonne: " % (n2))
        if val2 == "1" and check1 <= 42:
            for i in b1:
                if b1 == empty_list:
                    board[35 - check1] = "O"
                    board[35 - check1] = colored(board[35 - check1], 'yellow')
                    play = play + 1
            check1 = check1 + 7
        if val2 == "2":
            for i in b2:
                if b2 == empty_list:
                    board[36 - check2] = "O"
                    board[36 - check2] = colored(board[36 - check2], 'yellow')
                    play = play + 1
            check2 = check2 + 7
        if val2 == "3":
            for i in b3:
                if b3 == empty_list:
                    board[37 - check3] = "O"
                    board[37 - check3] = colored(board[37 - check3], 'yellow')
                    play = play + 1
            check3 = check3 + 7
        if val2 == "4":
            for i in b4:
                if b4 == empty_list:
                    board[38 - check4] = "O"
                    board[38 - check4] = colored(board[38 - check4], 'yellow')
                    play = play + 1
            check4 = check4 + 7
        if val2 == "5":
            for i in b5:
                if b5 == empty_list:
                    board[39 - check5] = "O"
                    board[39 - check5] = colored(board[39 - check5], 'yellow')
                    play = play + 1
            check5 = check5 + 7
        if val2 == "6":
            for i in b6:
                if b6 == empty_list:
                    board[40 - check6] = "O"
                    board[40 - check6] = colored(board[40 - check6], 'yellow')
                    play = play + 1
            check6 = check6 + 7
        if val2 == "7":
            for i in b7:
                if b7 == empty_list:
                    board[41 - check7] = "O"
                    board[41 - check7] = colored(board[41 - check7], 'yellow')
                    play = play + 1
            check7 = check7 + 7
        w = [board[35],board[36],board[37],board[38]]
        w2 = [board[36],board[37],board[38],board[39]]
        w3 = [board[37],board[38],board[39],board[40]]
        w4 = [board[38],board[39],board[40],board[41]]
        w5 = [board[28],board[29],board[30],board[31]]
        w6 = [board[29],board[30],board[31],board[32]]
        w7 = [board[30],board[31],board[32],board[33]]
        w8 = [board[31],board[32],board[33],board[34]]
        w9 = [board[21],board[22],board[23],board[24]]
        w10 = [board[22],board[23],board[24],board[25]]
        w11 = [board[23],board[24],board[25],board[26]]
        w12 = [board[24],board[25],board[26],board[27]]
        w13 = [board[14],board[15],board[16],board[17]]
        w14 = [board[15],board[16],board[17],board[18]]
        w15 = [board[16],board[17],board[18],board[19]]
        w16 = [board[17],board[18],board[19],board[20]]
        w17 = [board[7],board[8],board[9],board[10]]
        w18 = [board[8],board[9],board[10],board[11]]
        w19 = [board[9],board[10],board[11],board[12]]
        w20 = [board[10],board[11],board[12],board[13]]
        w21 = [board[35],board[28],board[21],board[14]]
        w22 = [board[36],board[29],board[22],board[15]]
        w23 = [board[37],board[30],board[23],board[16]]
        w24 = [board[38],board[31],board[24],board[17]]
        w25 = [board[28],board[21],board[14],board[7]]
        w26 = [board[29],board[22],board[15],board[8]]
        w27 = [board[30],board[23],board[16],board[9]]
        w28 = [board[31],board[24],board[17],board[10]]
        w29 = [board[21],board[14],board[7],board[0]]
        w30 = [board[22],board[15],board[8],board[1]]
        w31 = [board[23],board[16],board[9],board[2]]
        w32 = [board[24],board[17],board[10],board[3]]
        w33 = [board[39],board[32],board[25],board[18]]
        w34 = [board[40],board[33],board[26],board[19]]
        w35 = [board[41],board[34],board[27],board[20]]
        w36 = [board[32],board[25],board[18],board[11]]
        w37 = [board[33],board[26],board[19],board[12]]
        w38 = [board[34],board[27],board[20],board[13]]
        w39 = [board[25],board[18],board[11],board[4]]
        w40 = [board[26],board[19],board[12],board[5]]
        w41 = [board[27],board[20],board[13],board[6]]
        w42 = [board[35],board[29],board[23],board[17]]
        w43 = [board[29],board[23],board[17],board[11]]
        w44 = [board[23],board[17],board[11],board[5]]
        w45 = [board[36],board[30],board[24],board[18]]
        w46 = [board[30],board[24],board[18],board[12]]
        w47 = [board[24],board[18],board[12],board[6]]
        w48 = [board[37],board[31],board[25],board[19]]
        w49 = [board[31],board[25],board[19],board[13]]
        w50 = [board[38],board[32],board[26],board[20]]
        w51 = [board[28],board[22],board[16],board[10]]
        w52 = [board[22],board[16],board[10],board[4]]
        w53 = [board[21],board[15],board[9],board[3]]
        w54 = [board[41],board[33],board[25],board[17]]
        w55 = [board[33],board[25],board[17],board[9]]
        w56 = [board[25],board[17],board[9],board[1]]
        w57 = [board[40],board[32],board[24],board[16]]
        w58 = [board[32],board[24],board[16],board[8]]
        w59 = [board[24],board[16],board[8],board[0]]
        w60 = [board[39],board[31],board[23],board[15]]
        w61 = [board[31],board[23],board[15],board[7]]
        w62 = [board[38],board[30],board[22],board[14]]
        w63 = [board[34],board[26],board[18],board[10]]
        w64 = [board[26],board[18],board[10],board[2]]
        w65 = [board[27],board[19],board[11],board[3]]
        w66 = [board[6],board[12],board[18],board[24]]
        w67 = [board[12],board[18],board[24],board[30]]
        w68 = [board[18],board[24],board[30],board[36]]
        w69 = [board[5],board[11],board[17],board[23]]
        w70 = [board[11],board[17],board[23],board[29]]
        w71 = [board[17],board[23],board[29],board[35]]
        w72 = [board[4],board[10],board[16],board[22]]
        w73 = [board[10],board[16],board[22],board[28]]
        w74 = [board[3],board[9],board[15],board[21]]
        w75 = [board[13],board[19],board[25],board[31]]
        w76 = [board[19],board[25],board[31],board[37]]
        w77 = [board[35],board[36],board[37],board[38]]
        w78 = [board[0],board[8],board[16],board[24]]
        w79 = [board[8],board[16],board[24],board[32]]
        w80 = [board[16],board[24],board[32],board[40]]
        w81 = [board[1],board[9],board[17],board[25]]
        w82 = [board[9],board[17],board[25],board[33]]
        w83 = [board[17],board[25],board[33],board[41]]
        w84 = [board[2],board[10],board[18],board[26]]
        w85 = [board[10],board[18],board[26],board[34]]
        w86 = [board[3],board[11],board[19],board[27]]
        w87 = [board[7],board[15],board[23],board[31]]
        w88 = [board[15],board[23],board[31],board[39]]
        w89 = [board[14],board[22],board[30],board[38]]    
        if w == p2 or w2 == p2 or w3 == p2 or w4 == p2 or w5 == p2 or w6 == p2 or w7 == p2 or w8 == p2 or w9 == p2 or w10 == p2 or w11 == p2 or w12 == p2 or w13 == p2 or w14 == p2 or w15 == p2 or w16 == p2 or w17 == p2 or w18 == p2 or w19 == p2 or w20 == p2 or w21 == p2 or w22 == p2  or w23 == p2 or w24 == p2 or w25 == p2 or w26 == p2 or w27 == p2 or w28 == p2 or w29 == p2 or w30 == p2 or w31 == p2 or w32 == p2 or w33 == p2 or w34 == p2 or w35 == p2 or w36 == p2 or w37 == p2 or w38 == p2 or w39 == p2 or w40 == p2 or w41 == p2 or w42 == p2 or w43 == p2 or w44 == p2 or w45 == p2 or w46 == p2 or w47 == p2 or w48 == p2 or w49 == p2 or w50 == p2 or w51 == p2 or w52 == p2 or w53 == p2 or w54 == p2 or w55 == p2 or w56 == p2 or w57 == p2 or w58 == p2 or w59 == p2 or w60 == p2 or w61 == p2 or w62 == p2 or w63 == p2 or w64 == p2 or w65 == p2 or w66 == p2 or w67 == p2 or w68 == p2 or w69 == p2 or w70 == p2 or w71 == p2 or w72 == p2 or w73 == p2 or w74 == p2 or w75 == p2 or w76 == p2 or w77 == p2 or w78 == p2 or w79 == p2 or w80 == p2 or w81 == p2 or w82 == p2 or w83 == p2 or w84 == p2 or w85 == p2 or w86 == p2 or w87 == p2 or w88 == p2 or w89 == p2:
            print_board(board,name1,name2,play/6)
            print("%s tu as gagnes!!!" % (n2))
            restart(1)
        if play == 252:
            print_board(board,name1,name2,play/6)
            print("Egalite")
            restart(1)
        print_board(board,name1,name2,play/6)
def connect4_ia():
    board = []
    j = 0
    for i in range(42):
        board.append(" ")
    empty_list = [" "," "," "," "," "," "]
    p1 = ["\x1b[31mX\x1b[0m","\x1b[31mX\x1b[0m","\x1b[31mX\x1b[0m","\x1b[31mX\x1b[0m"]
    p3 = ["\x1b[31mX\x1b[0m","\x1b[31mX\x1b[0m","\x1b[31mX\x1b[0m"]
    p21 = ["\x1b[31mX\x1b[0m","\x1b[31mX\x1b[0m"]
    p2 = ["\x1b[33mO\x1b[0m","\x1b[33mO\x1b[0m","\x1b[33mO\x1b[0m","\x1b[33mO\x1b[0m"]
    b1 =  [board[35],board[28],board[21],board[14],board[7],board[0]]
    b2 =  [board[36],board[29],board[22],board[15],board[8],board[1]]
    b3 =  [board[37],board[30],board[23],board[16],board[9],board[2]]
    b4 =  [board[38],board[31],board[24],board[17],board[10],board[3]]
    b5 =  [board[39],board[32],board[25],board[18],board[11],board[4]]
    b6 =  [board[40],board[33],board[26],board[19],board[12],board[5]]
    b7 =  [board[41],board[34],board[27],board[20],board[13],board[6]]
    print(b1[0])
    i = 0
    idx = 0
    check1 = 0
    check2 = 0
    check3 = 0
    check4 = 0
    check5 = 0
    check6 = 0
    check7 = 0
    draw = 0
    play = 0
    while True:
        val = input("%s choisi une colonne: " % (n1))
        if  check1 >= 42 and val == "1" or check2 >= 42 and val == "2" or check3 >= 42 and val == "3" or check4 >= 42 and val == "4" or check5 >= 42 and val == "5" or check6 >= 42 and val == "6" or check7 >= 42 and val == "7" :
            print("Erreur la colonne est pleine")
            val = input("%s choisi une colonne: " % (n1))
        if int(val) < 1 or int(val) > 7:
            print("Erreur tu dois choisir entre parmis les colonnes 1 à 7")
            val = input("%s choisi une colonne: " % (n1))    
        if val == "1":
            for i in b1:
                if b1 == empty_list:
                    board[35 - check1] = "X"
                    board[35 - check1] = colored(board[35 - check1], 'red')
                    play = play + 1
                    draw = draw + 1
            check1 = check1 + 7
        if val == "2":
            for i in b2:
                if b2 == empty_list:
                    board[36 - check2] = "X"
                    board[36 - check2] = colored(board[36 - check2], 'red')
                    play = play + 1
                    draw = draw + 1
            check2 = check2 + 7
        if val == "3":
            for i in b3:
                if b3 == empty_list:
                    board[37 - check3] = "X"
                    board[37 - check3] = colored(board[37 - check3], 'red')
                    play = play + 1
                    draw = draw + 1
            check3 = check3 + 7
        if val == "4":
            for i in b4:
                if b4 == empty_list:
                    board[38 - check4] = "X"
                    board[38 - check4] = colored(board[38 - check4], 'red')
                    play = play + 1
                    draw = draw + 1
            check4 = check4 + 7
        if val == "5":
            for i in b5:
                if b5 == empty_list:
                    board[39 - check5] = "X"
                    board[39 - check5] = colored(board[39 - check5], 'red')
                    play = play + 1
                    draw = draw + 1
            check5 = check5 + 7
        if val == "6":
            for i in b6:
                if b6 == empty_list:
                    board[40 - check6] = "X"
                    board[40 - check6] = colored(board[40 - check6], 'red')
                    play = play + 1
                    draw = draw + 1
            check6 = check6 + 7
        if val == "7":
            for i in b7:
                if b7 == empty_list:
                    board[41 - check7] = "X"
                    board[41 - check7] = colored(board[41 - check7], 'red')
                    play = play + 1
                    draw = draw + 1
            check7 = check7 + 7
        w = [board[35],board[36],board[37],board[38]]
        w2 = [board[36],board[37],board[38],board[39]]
        w3 = [board[37],board[38],board[39],board[40]]
        w4 = [board[38],board[39],board[40],board[41]]
        w5 = [board[28],board[29],board[30],board[31]]
        w6 = [board[29],board[30],board[31],board[32]]
        w7 = [board[30],board[31],board[32],board[33]]
        w8 = [board[31],board[32],board[33],board[34]]
        w9 = [board[21],board[22],board[23],board[24]]
        w10 = [board[22],board[23],board[24],board[25]]
        w11 = [board[23],board[24],board[25],board[26]]
        w12 = [board[24],board[25],board[26],board[27]]
        w13 = [board[14],board[15],board[16],board[17]]
        w14 = [board[15],board[16],board[17],board[18]]
        w15 = [board[16],board[17],board[18],board[19]]
        w16 = [board[17],board[18],board[19],board[20]]
        w17 = [board[7],board[8],board[9],board[10]]
        w18 = [board[8],board[9],board[10],board[11]]
        w19 = [board[9],board[10],board[11],board[12]]
        w20 = [board[10],board[11],board[12],board[13]]
        w21 = [board[35],board[28],board[21],board[14]]
        w22 = [board[36],board[29],board[22],board[15]]
        w23 = [board[37],board[30],board[23],board[16]]
        w24 = [board[38],board[31],board[24],board[17]]
        w25 = [board[28],board[21],board[14],board[7]]
        w26 = [board[29],board[22],board[15],board[8]]
        w27 = [board[30],board[23],board[16],board[9]]
        w28 = [board[31],board[24],board[17],board[10]]
        w29 = [board[21],board[14],board[7],board[0]]
        w30 = [board[22],board[15],board[8],board[1]]
        w31 = [board[23],board[16],board[9],board[2]]
        w32 = [board[24],board[17],board[10],board[3]]
        w33 = [board[39],board[32],board[25],board[18]]
        w34 = [board[40],board[33],board[26],board[19]]
        w35 = [board[41],board[34],board[27],board[20]]
        w36 = [board[32],board[25],board[18],board[11]]
        w37 = [board[33],board[26],board[19],board[12]]
        w38 = [board[34],board[27],board[20],board[13]]
        w39 = [board[25],board[18],board[11],board[4]]
        w40 = [board[26],board[19],board[12],board[5]]
        w41 = [board[27],board[20],board[13],board[6]]
        w42 = [board[35],board[29],board[23],board[17]]
        w43 = [board[29],board[23],board[17],board[11]]
        w44 = [board[23],board[17],board[11],board[5]]
        w45 = [board[36],board[30],board[24],board[18]]
        w46 = [board[30],board[24],board[18],board[12]]
        w47 = [board[24],board[18],board[12],board[6]]
        w48 = [board[37],board[31],board[25],board[19]]
        w49 = [board[31],board[25],board[19],board[13]]
        w50 = [board[38],board[32],board[26],board[20]]
        w51 = [board[28],board[22],board[16],board[10]]
        w52 = [board[22],board[16],board[10],board[4]]
        w53 = [board[21],board[15],board[9],board[3]]
        w54 = [board[41],board[33],board[25],board[17]]
        w55 = [board[33],board[25],board[17],board[9]]
        w56 = [board[25],board[17],board[9],board[1]]
        w57 = [board[40],board[32],board[24],board[16]]
        w58 = [board[32],board[24],board[16],board[8]]
        w59 = [board[24],board[16],board[8],board[0]]
        w60 = [board[39],board[31],board[23],board[15]]
        w61 = [board[31],board[23],board[15],board[7]]
        w62 = [board[38],board[30],board[22],board[14]]
        w63 = [board[34],board[26],board[18],board[10]]
        w64 = [board[26],board[18],board[10],board[2]]
        w65 = [board[27],board[19],board[11],board[3]]
        w66 = [board[6],board[12],board[18],board[24]]
        w67 = [board[12],board[18],board[24],board[30]]
        w68 = [board[18],board[24],board[30],board[36]]
        w69 = [board[5],board[11],board[17],board[23]]
        w70 = [board[11],board[17],board[23],board[29]]
        w71 = [board[17],board[23],board[29],board[35]]
        w72 = [board[4],board[10],board[16],board[22]]
        w73 = [board[10],board[16],board[22],board[28]]
        w74 = [board[3],board[9],board[15],board[21]]
        w75 = [board[13],board[19],board[25],board[31]]
        w76 = [board[19],board[25],board[31],board[37]]
        w77 = [board[35],board[36],board[37],board[38]]
        w78 = [board[0],board[8],board[16],board[24]]
        w79 = [board[8],board[16],board[24],board[32]]
        w80 = [board[16],board[24],board[32],board[40]]
        w81 = [board[1],board[9],board[17],board[25]]
        w82 = [board[9],board[17],board[25],board[33]]
        w83 = [board[17],board[25],board[33],board[41]]
        w84 = [board[2],board[10],board[18],board[26]]
        w85 = [board[10],board[18],board[26],board[34]]
        w86 = [board[3],board[11],board[19],board[27]]
        w87 = [board[7],board[15],board[23],board[31]]
        w88 = [board[15],board[23],board[31],board[39]]
        w89 = [board[14],board[22],board[30],board[38]]
        if w == p1 or w2 == p1 or w3 == p1 or w4 == p1 or w5 == p1 or w6 == p1 or w7 == p1 or w8 == p1 or w9 == p1 or w10 == p1 or w11 == p1 or w12 == p1 or w13 == p1 or w14 == p1 or w15 == p1 or w16 == p1 or w17 == p1 or w18 == p1 or w19 == p1 or w20 == p1 or w21 == p1 or w22 == p1  or w23 == p1 or w24 == p1 or w25 == p1 or w26 == p1 or w27 == p1 or w28 == p1 or w29 == p1 or w30 == p1 or w31 == p1 or w32 == p1 or w33 == p1 or w34 == p1 or w35 == p1 or w36 == p1 or w37 == p1 or w38 == p1 or w39 == p1 or w40 == p1 or w41 == p1 or w42 == p1 or w43 == p1 or w44 == p1 or w45 == p1 or w46 == p1 or w47 == p1 or w48 == p1 or w49 == p1 or w50 == p1 or w51 == p1 or w52 == p1 or w53 == p1 or w54 == p1 or w55 == p1 or w56 == p1 or w57 == p1 or w58 == p1 or w59 == p1 or w60 == p1 or w61 == p1 or w62 == p1 or w63 == p1 or w64 == p1 or w65 == p1 or w66 == p1 or w67 == p1 or w68 == p1 or w69 == p1 or w70 == p1 or w71 == p1 or w72 == p1 or w73 == p1 or w74 == p1 or w75 == p1 or w76 == p1 or w77 == p1 or w78 == p1 or w79 == p1 or w80 == p1 or w81 == p1 or w82 == p1 or w83 == p1 or w84 == p1 or w85 == p1 or w86 == p1 or w87 == p1 or w88 == p1 or w89 == p1:
            print_board(board,name1,name2,play/12)
            print("%s tu as gagné!!!" % (n1))
            restart(2)
        if play == 252:
            print_board(board,name1,name2,play/12)
            print("Egalite")
            restart(2)
            print_board(board,name1,name2,play/12)
        val2 = 0
        #if int(val) != 7:
        #    val2 = random_nbr(1,int(val))
        #if int(val) == 7:
        #    val2 = 7
        #1
        z10 = [board[35],board[28],board[21]]
        z11 = [board[28],board[21],board[14]]
        z12 = [board[21],board[14],board[7]]

        #2
        z20 = [board[36],board[29],board[22]]
        z21 = [board[29],board[22],board[15]]
        z22 = [board[22],board[15],board[8]]
       
        #3
        z30 = [board[37],board[30],board[23]]
        z31 = [board[30],board[23],board[16]]
        z32 = [board[23],board[16],board[9]]
       
        #4
        z40 = [board[35],board[36],board[37]]
        z41 = [board[28],board[29],board[30]]
        z42 = [board[21],board[22],board[23]]
        z43 = [board[14],board[15],board[16]]
        z44 = [board[7],board[8],board[9]]
        z45 = [board[38],board[31],board[24]]
        z46 = [board[31],board[24],board[17]]
        z47 = [board[24],board[17],board[10]]

        #5
        z50 = [board[36],board[37],board[38]]
        z51 = [board[29],board[30],board[31]]
        z52 = [board[22],board[23],board[24]]
        z53 = [board[15],board[16],board[17]]
        z54 = [board[8],board[9],board[10]]
        z55 = [board[39],board[32],board[25]]
        z56 = [board[32],board[25],board[18]]
        z57 = [board[25],board[18],board[11]]
        
        #6
        z60 = [board[37],board[38],board[39]]
        z61 = [board[30],board[31],board[32]]
        z62 = [board[23],board[24],board[25]]
        z63 = [board[16],board[17],board[18]]
        z64 = [board[9],board[10],board[11]]
        z65 = [board[40],board[33],board[26]]
        z66 = [board[33],board[26],board[19]]
        z67 = [board[26],board[19],board[12]]
       
        #7
        z70 = [board[38],board[39],board[40]]
        z71 = [board[31],board[32],board[33]]
        z72 = [board[24],board[25],board[26]]
        z73 = [board[17],board[18],board[19]]
        z74 = [board[10],board[11],board[12]]
        z75 = [board[41],board[34],board[27]]
        z76 = [board[34],board[27],board[20]]
        z77 = [board[27],board[20],board[13]]
        
        #1
        y10 = [board[35],board[28]]
        y11 = [board[28],board[21]]
        y12 = [board[21],board[14]]

        #2
        y20 = [board[36],board[29]]
        y21 = [board[29],board[22]]
        y22 = [board[22],board[15]]
       
        #3
        y30 = [board[37],board[30]]
        y31 = [board[30],board[23]]
        y32 = [board[23],board[16]]
        y33 = [board[35],board[36]]
        y34 = [board[28],board[29]]
        y35 = [board[21],board[22]]
        y36 = [board[14],board[15]]
        y37 = [board[7],board[8]]
        
        #4
        y40 = [board[38],board[31]]
        y41 = [board[31],board[24]]
        y42 = [board[24],board[17]]
        y43 = [board[36],board[37]]
        y44 = [board[29],board[30]]
        y45 = [board[22],board[23]]
        y46 = [board[15],board[16]]
        y47 = [board[8],board[9]]
        
        #5
        y50 = [board[39],board[32]]
        y51 = [board[32],board[25]]
        y52 = [board[25],board[18]]
        y53 = [board[40],board[41]]
        y54 = [board[37],board[38]]
        y55 = [board[30],board[31]]
        y56 = [board[23],board[24]]
        y57 = [board[16],board[17]]
        y58 = [board[9],board[10]]
        
        #6
        y60 = [board[40],board[33]]
        y61 = [board[33],board[26]]
        y62 = [board[26],board[19]]
        y63 = [board[38],board[39]]
        y64 = [board[31],board[32]]
        y65 = [board[24],board[25]]
        y66 = [board[17],board[18]]
        y67 = [board[10],board[11]]
        
        #7
        y70 = [board[41],board[34]]
        y71 = [board[34],board[27]]
        y72 = [board[27],board[20]]

        ival = int(val)
        #print(ival)
        if ival == 1 and (z10 == p3 or z11 == p3 or z12 == p3):
            val2 = 1
            print("CONDITION 1!")
        elif ival == 2 and (z20 == p3 or z21 == p3 or z22 == p3):
            val2 = 2
            print("CONDITION 2!")
        elif ival == 3 and (z30 == p3 or z31 == p3 or z32 == p3):
            val2 = 3
            print("CONDITION 3!")
        elif ival == 4 and (z40 == p3 or z41 == p3 or z42 == p3 or z43 == p3 or z44 == p3 or z45 == p3 or z46 == p3 or z47 == p3):
            val2 = 4
            print("CONDITION 4!")
        elif check5 <= 42 and (z50 == p3 or z51 == p3 or z52 == p3 or z53 == p3 or z54 == p3 or z55 == p3 or z56 == p3 or z57 == p3) and ival == 5:
            val2 = 5
            print("CONDITION 5!")
        elif check6 <= 42 and (z60 == p3 or z61 == p3 or z62 == p3 or z63 == p3 or z64 == p3 or z65 == p3 or z66 == p3 or z67 == p3) and ival == 6:
            val2 = 6
            print("CONDITION 6!")
        elif check7 <= 42 and (z70 == p3 or z71 == p3 or z72 == p3 or z73 == p3 or z74 == p3 or z75 == p3 or z76 == p3 or z77 == p3) and ival == 7:
            val2 = 7
            print("CONDITION 6!")
        elif check1 >= 42 and (z50 == p3 or z51 == p3 or z52 == p3 or z53 == p3 or z54 == p3 or z55 == p3 or z56 == p3 or z57 == p3) and ival == 1:
            val2 = 1
            print("CONDITION 7!")
        elif check2 <= 42 and (z60 == p3 or z61 == p3 or z62 == p3 or z63 == p3 or z64 == p3 or z65 == p3 or z66 == p3 or z67 == p3) and ival == 2:
            val2 = 2
            print("CONDITION 8!")
        elif check3 <= 42 and (z70 == p3 or z71 == p3 or z72 == p3 or z73 == p3 or z74 == p3 or z75 == p3 or z76 == p3 or z77 == p3) and ival == 3:
            val2 = 3
            print("CONDITION 9!")
        elif check4 <= 42 and (y44 == p21 or y45 == p21 or y46 == p21 or y47 == p21):
            val2 = 4
            print("CONDITION 10!")
        elif check1 <= 42 and (y44 == p21 or y45 == p21 or y46 == p21 or y47 == p21):
            val2 = 1
            print("CONDITION 11!")
        elif check2 <= 42 and (y54 == p21 or y55 == p21 or y56 == p21 or y57 == p21 or y58 == p21):
            val2 = 2
            print("CONDITION 12!")
        elif check5 <= 42 and (y54 == p21 or y55 == p21 or y56 == p21 or y57 == p21 or y58 == p21):
            val2 = 5
            print("CONDITION 13!")
        elif check6 <= 42 and (y63 == p21 or y64 == p21 or y65 == p21 or y66 == p21 or y67 == p21):
            val2 = 6
            print("CONDITION 14!")
        elif check3 <= 42 and (y63 == p21 or y64 == p21 or y65 == p21 or y66 == p21 or y67 == p21):
            val2 = 3
            print("CONDITION 15!")
        elif y30 == p21 or y31 == p21 or y32 == p21 or y33 == p21 or y34 == p21 or y35 == p21 or y36 == p21 or y37 == p21:
             val2 = 3
             print("CONDITION 16!")
        elif y10 == p21 or y11 == p21 or y12 == p21:
             val2 = 1
             print("CONDITION 17!")
        elif y20 == p21 or y21 == p21 or y22 == p21:
             val2 = 2
             print("CONDITION 18!")
        elif y40 == p21 or y41 == p21 or y42 == p21 or y44 == p21:
             val2 = 4
             print("CONDITION 19!")
        elif y50 == p21 or y51 == p21 or y52 == p21 or y53 == p21:
             val2 = 5
             print("CONDITION 20!")
        elif y60 == p21 or y61 == p21 or y62 == p21:
             val2 = 6
             print("CONDITION 21!")
        elif y70 == p21 or y71 == p21 or y72 == p21:
             val2 = 7
             print("CONDITION 22!")
        else:
            print("OK")
            val2 = random_nbr(2,0)
        while  check1 >= 42 and val2 == 1 or check2 >= 42 and val2 == 2 or check3 >= 42 and val2 == 3 or check4 >= 42 and val2 == 4 or check5 >= 42 and val2 == 5 or check6 >= 42 and val2 == 6 or check7 >= 42 and val2 == 7 :
            val2 = random_nbr(2,0)
        print("%s a choisi la colonne %d" %(n2,val2))
        #print(check1,check2,check3,check4,check5,check6,check7)
        if val2 == 1:
            for i in b1:
                if b1 == empty_list:
                    board[35 - check1] = "O"
                    board[35 - check1] = colored(board[35 - check1], 'yellow')
                    play = play + 3
                    draw = draw + 1
            check1 = check1 + 7
        if val2 == 2:
            for i in b2:
                if b2 == empty_list:
                    board[36 - check2] = "O"
                    board[36 - check2] = colored(board[36 - check2], 'yellow')
                    play = play + 3
                    draw = draw + 1
            check2 = check2 + 7
        if val2 == 3:
            for i in b3:
                if b3 == empty_list:
                    board[37 - check3] = "O"
                    board[37 - check3] = colored(board[37 - check3], 'yellow')
                    play = play + 3
                    draw = draw + 1
            check3 = check3 + 7
        if val2 == 4:
            for i in b4:
                if b4 == empty_list:
                    board[38 - check4] = "O"
                    board[38 - check4] = colored(board[38 - check4], 'yellow')
                    play = play + 3
                    draw = draw + 1
            check4 = check4 + 7
        if val2 == 5:
            for i in b5:
                if b5 == empty_list:
                    board[39 - check5] = "O"
                    board[39 - check5] = colored(board[39 - check5], 'yellow')
                    play = play + 3
                    draw = draw + 1
            check5 = check5 + 7
        if val2 == 6:
            for i in b6:
                if b6 == empty_list:
                    board[40 - check6] = "O"
                    board[40 - check6] = colored(board[40 - check6], 'yellow')
                    play = play + 3
                    draw = draw + 1
            check6 = check6 + 7
        if val2 == 7:
            for i in b7:
                if b7 == empty_list:
                    board[41 - check7] = "O"
                    board[41 - check7] = colored(board[41 - check7], 'yellow')
                    play = play + 3
                    draw = draw + 1
            check7 = check7 + 7
        
        w = [board[35],board[36],board[37],board[38]]
        w2 = [board[36],board[37],board[38],board[39]]
        w3 = [board[37],board[38],board[39],board[40]]
        w4 = [board[38],board[39],board[40],board[41]]
        w5 = [board[28],board[29],board[30],board[31]]
        w6 = [board[29],board[30],board[31],board[32]]
        w7 = [board[30],board[31],board[32],board[33]]
        w8 = [board[31],board[32],board[33],board[34]]
        w9 = [board[21],board[22],board[23],board[24]]
        w10 = [board[22],board[23],board[24],board[25]]
        w11 = [board[23],board[24],board[25],board[26]]
        w12 = [board[24],board[25],board[26],board[27]]
        w13 = [board[14],board[15],board[16],board[17]]
        w14 = [board[15],board[16],board[17],board[18]]
        w15 = [board[16],board[17],board[18],board[19]]
        w16 = [board[17],board[18],board[19],board[20]]
        w17 = [board[7],board[8],board[9],board[10]]
        w18 = [board[8],board[9],board[10],board[11]]
        w19 = [board[9],board[10],board[11],board[12]]
        w20 = [board[10],board[11],board[12],board[13]]
        w21 = [board[35],board[28],board[21],board[14]]
        w22 = [board[36],board[29],board[22],board[15]]
        w23 = [board[37],board[30],board[23],board[16]]
        w24 = [board[38],board[31],board[24],board[17]]
        w25 = [board[28],board[21],board[14],board[7]]
        w26 = [board[29],board[22],board[15],board[8]]
        w27 = [board[30],board[23],board[16],board[9]]
        w28 = [board[31],board[24],board[17],board[10]]
        w29 = [board[21],board[14],board[7],board[0]]
        w30 = [board[22],board[15],board[8],board[1]]
        w31 = [board[23],board[16],board[9],board[2]]
        w32 = [board[24],board[17],board[10],board[3]]
        w33 = [board[39],board[32],board[25],board[18]]
        w34 = [board[40],board[33],board[26],board[19]]
        w35 = [board[41],board[34],board[27],board[20]]
        w36 = [board[32],board[25],board[18],board[11]]
        w37 = [board[33],board[26],board[19],board[12]]
        w38 = [board[34],board[27],board[20],board[13]]
        w39 = [board[25],board[18],board[11],board[4]]
        w40 = [board[26],board[19],board[12],board[5]]
        w41 = [board[27],board[20],board[13],board[6]]
        w42 = [board[35],board[29],board[23],board[17]]
        w43 = [board[29],board[23],board[17],board[11]]
        w44 = [board[23],board[17],board[11],board[5]]
        w45 = [board[36],board[30],board[24],board[18]]
        w46 = [board[30],board[24],board[18],board[12]]
        w47 = [board[24],board[18],board[12],board[6]]
        w48 = [board[37],board[31],board[25],board[19]]
        w49 = [board[31],board[25],board[19],board[13]]
        w50 = [board[38],board[32],board[26],board[20]]
        w51 = [board[28],board[22],board[16],board[10]]
        w52 = [board[22],board[16],board[10],board[4]]
        w53 = [board[21],board[15],board[9],board[3]]
        w54 = [board[41],board[33],board[25],board[17]]
        w55 = [board[33],board[25],board[17],board[9]]
        w56 = [board[25],board[17],board[9],board[1]]
        w57 = [board[40],board[32],board[24],board[16]]
        w58 = [board[32],board[24],board[16],board[8]]
        w59 = [board[24],board[16],board[8],board[0]]
        w60 = [board[39],board[31],board[23],board[15]]
        w61 = [board[31],board[23],board[15],board[7]]
        w62 = [board[38],board[30],board[22],board[14]]
        w63 = [board[34],board[26],board[18],board[10]]
        w64 = [board[26],board[18],board[10],board[2]]
        w65 = [board[27],board[19],board[11],board[3]]
        w66 = [board[6],board[12],board[18],board[24]]
        w67 = [board[12],board[18],board[24],board[30]]
        w68 = [board[18],board[24],board[30],board[36]]
        w69 = [board[5],board[11],board[17],board[23]]
        w70 = [board[11],board[17],board[23],board[29]]
        w71 = [board[17],board[23],board[29],board[35]]
        w72 = [board[4],board[10],board[16],board[22]]
        w73 = [board[10],board[16],board[22],board[28]]
        w74 = [board[3],board[9],board[15],board[21]]
        w75 = [board[13],board[19],board[25],board[31]]
        w76 = [board[19],board[25],board[31],board[37]]
        w77 = [board[35],board[36],board[37],board[38]]
        w78 = [board[0],board[8],board[16],board[24]]
        w79 = [board[8],board[16],board[24],board[32]]
        w80 = [board[16],board[24],board[32],board[40]]
        w81 = [board[1],board[9],board[17],board[25]]
        w82 = [board[9],board[17],board[25],board[33]]
        w83 = [board[17],board[25],board[33],board[41]]
        w84 = [board[2],board[10],board[18],board[26]]
        w85 = [board[10],board[18],board[26],board[34]]
        w86 = [board[3],board[11],board[19],board[27]]
        w87 = [board[7],board[15],board[23],board[31]]
        w88 = [board[15],board[23],board[31],board[39]]
        w89 = [board[14],board[22],board[30],board[38]]
        if w == p2 or w2 == p2 or w3 == p2 or w4 == p2 or w5 == p2 or w6 == p2 or w7 == p2 or w8 == p2 or w9 == p2 or w10 == p2 or w11 == p2 or w12 == p2 or w13 == p2 or w14 == p2 or w15 == p2 or w16 == p2 or w17 == p2 or w18 == p2 or w19 == p2 or w20 == p2 or w21 == p2 or w22 == p2  or w23 == p2 or w24 == p2 or w25 == p2 or w26 == p2 or w27 == p2 or w28 == p2 or w29 == p2 or w30 == p2 or w31 == p2 or w32 == p2 or w33 == p2 or w34 == p2 or w35 == p2 or w36 == p2 or w37 == p2 or w38 == p2 or w39 == p2 or w40 == p2 or w41 == p2 or w42 == p2 or w43 == p2 or w44 == p2 or w45 == p2 or w46 == p2 or w47 == p2 or w48 == p2 or w49 == p2 or w50 == p2 or w51 == p2 or w52 == p2 or w53 == p2 or w54 == p2 or w55 == p2 or w56 == p2 or w57 == p2 or w58 == p2 or w59 == p2 or w60 == p2 or w61 == p2 or w62 == p2 or w63 == p2 or w64 == p2 or w65 == p2 or w66 == p2 or w67 == p2 or w68 == p2 or w69 == p2 or w70 == p2 or w71 == p2 or w72 == p2 or w73 == p2 or w74 == p2 or w75 == p2 or w76 == p2 or w77 == p2 or w78 == p2 or w79 == p2 or w80 == p2 or w81 == p2 or w82 == p2 or w83 == p2 or w84 == p2 or w85 == p2 or w86 == p2 or w87 == p2 or w88 == p2 or w89 == p2:
            print_board(board,name1,name2,play/12)
            print("%s as gagnes!!!" % (n2))
            restart(2)
        if draw == 252:
            print_board(board,name1,name2,play/12)
            print("Egalite")
            restart(2)
        print_board(board,name1,name2,play/12)

board = []
for i in range(42):
    board.append(" ")
print("=====  Connect%s  =====" % (colored('4', 'red')))
print("                       ")
print("1. 1V1")
print("2. VS L'IA")
print("3. QUITTER")
print("                       ")
print("                       ")
choice = input("Choix:  ")
chx = int(choice)
if chx == 1:
    system("clear")
    name1 = input("J1 choisi ton nom: ")
    name2 = input("J2 choisi une nom: ")
    n1 = colored(name1, 'red')
    n2 = colored(name2, 'yellow')
    system("clear")
if chx == 2:
    system("clear")
    name1 = input("J1 choisi ton nom: ")
    name2 = "L'IA"
    n1 = colored(name1, 'red')
    n2 = colored(name2, 'yellow')
    system("clear")
if chx == 1:
    print_board(board,name1,name2,0)
if chx == 2:
    print_board(board,name1,"L'IA",0)
if chx == 2:
    connect4_ia()
if chx == 1:
    connect4_vs()
if chx == 3:
    quit()