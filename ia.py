#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## s
## File description:
## s
##

import sys
from termcolor import colored, cprint
from os import system
from random import randint
import map_nbr

def connect4_ia(r,n1,n2):
    board = []
    j = 0
    for i in range(42):
        board.append(" ")
    empty_list = [" "," "," "," "," "," "]
    p1 = ["\x1b[31mX\x1b[0m","\x1b[31mX\x1b[0m","\x1b[31mX\x1b[0m","\x1b[31mX\x1b[0m"]
    p3 = ["\x1b[31mX\x1b[0m","\x1b[31mX\x1b[0m","\x1b[31mX\x1b[0m"]
    p21 = ["\x1b[31mX\x1b[0m","\x1b[31mX\x1b[0m"]
    p2 = ["\x1b[33mO\x1b[0m","\x1b[33mO\x1b[0m","\x1b[33mO\x1b[0m","\x1b[33mO\x1b[0m"]
    p31 = ["\x1b[33mO\x1b[0m","\x1b[33mO\x1b[0m","\x1b[33mO\x1b[0m"]
    db1 = [board[35],board[29],board[23],board[17],board[11],board[5]]
    b1 =  [board[35],board[28],board[21],board[14],board[7],board[0]]
    b2 =  [board[36],board[29],board[22],board[15],board[8],board[1]]
    b3 =  [board[37],board[30],board[23],board[16],board[9],board[2]]
    b4 =  [board[38],board[31],board[24],board[17],board[10],board[3]]
    b5 =  [board[39],board[32],board[25],board[18],board[11],board[4]]
    b6 =  [board[40],board[33],board[26],board[19],board[12],board[5]]
    b7 =  [board[41],board[34],board[27],board[20],board[13],board[6]]
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
    dx = 0
    if r == 1:
        board[38 - check4] = "O"
        board[38 - check4] = colored(board[38 - check4], 'yellow')
        play = -12
        check4 = 7               
    while True:
        val = input("%s choisi une colonne: " % (n1))
        if  check1 >= 42 and val == "1" or check2 >= 42 and val == "2" or check3 >= 42 and val == "3" or check4 >= 42 and val == "4" or check5 >= 42 and val == "5" or check6 >= 42 and val == "6" or check7 >= 42 and val == "7" :
            print("Erreur la colonne est pleine")
            val = input("%s choisi une colonne: " % (n1))
        if int(val) < 1 or int(val) > 7:
            print("Erreur tu dois choisir entre parmis les colonnes 1 ?? 7")
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
            map_nbr.print_board(board,n1,n2,play/12)
            print("%s tu as gagn??!!!" % (n1))
            map_nbr.restart(2,n1,n2)
        if play == 252:
            map_nbr.print_board(board,n1,n2,play/12)
            print("Egalite")
            map_nbr.restart(2,n1,n2)
            map_nbr.print_board(board,n1,n2,play/12)
        val2 = 0
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
        #8 DIAG2
        d0 = [board[35],board[29],board[23]]
        d1 = [board[29],board[23],board[17]]
        d2 = [board[23],board[17],board[11]]
        d3 = [board[36],board[30],board[24]]
        d4 = [board[30],board[24],board[18]]
        d5 = [board[24],board[18],board[12]]
        d6 = [board[37],board[31],board[25]]
        d7 = [board[31],board[25],board[19]]
        d8 = [board[38],board[32],board[26]]
        d9 = [board[28],board[22],board[16]]
        d10 = [board[22],board[16],board[10]]
        d11 = [board[21],board[15],board[9]]
        d12 = [board[41],board[33],board[25]]
        d13 = [board[33],board[25],board[17]]
        d14 = [board[25],board[17],board[9]]
        d15 = [board[40],board[32],board[24]]
        d16 = [board[32],board[24],board[16]]
        d17 = [board[24],board[16],board[8]]
        d18 = [board[39],board[31],board[23]]
        d19 = [board[31],board[23],board[15]]
        d20 = [board[38],board[30],board[22]]
        d21 = [board[34],board[26],board[18]]
        d22 = [board[26],board[18],board[10]]
        d23 = [board[27],board[19],board[11]]
        d24 = [board[6],board[12],board[18]]
        d25 = [board[12],board[18],board[24]]
        d26 = [board[18],board[24],board[30]]
        d27 = [board[5],board[11],board[17]]
        d28 = [board[11],board[17],board[23]]
        d29 = [board[17],board[23],board[29]]
        d30 = [board[4],board[10],board[16]]
        d31 = [board[10],board[16],board[22]]
        d32 = [board[3],board[9],board[15]]
        d33 = [board[13],board[19],board[25]]
        d34 = [board[19],board[25],board[31]]
        d35 = [board[35],board[36],board[37]]
        d36 = [board[0],board[8],board[16]]
        d37 = [board[8],board[16],board[24]]
        d39 = [board[16],board[24],board[32]]
        d40 = [board[1],board[9],board[17]]
        d41 = [board[9],board[17],board[25]]
        d42 = [board[17],board[25],board[33]]
        d43 = [board[2],board[10],board[18]]
        d45 = [board[10],board[18],board[26]]
        d46 = [board[3],board[11],board[19]]
        d47 = [board[7],board[15],board[23]]
        d48 = [board[15],board[23],board[31]]
        d49 = [board[14],board[22],board[30]]

        ival = int(val)
        if ival == 1 and (z10 == p3 or z11 == p3 or z12 == p3):
            val2 = 1
        elif ival == 2 and (z20 == p3 or z21 == p3 or z22 == p3):
            val2 = 2
        elif ival == 3 and (z30 == p3 or z31 == p3 or z32 == p3):
            val2 = 3
        elif ival == 4 and (z40 == p3 or z41 == p3 or z42 == p3 or z43 == p3 or z44 == p3 or z45 == p3 or z46 == p3 or z47 == p3):
            val2 = 4
        elif check5 <= 42 and (z50 == p3 or z51 == p3 or z52 == p3 or z53 == p3 or z54 == p3 or z55 == p3 or z56 == p3 or z57 == p3) and ival == 5:
            val2 = 5
        elif check6 <= 42 and (z60 == p3 or z61 == p3 or z62 == p3 or z63 == p3 or z64 == p3 or z65 == p3 or z66 == p3 or z67 == p3) and ival == 6:
            val2 = 6
        elif check7 <= 42 and (z70 == p3 or z71 == p3 or z72 == p3 or z73 == p3 or z74 == p3 or z75 == p3 or z76 == p3 or z77 == p3) and ival == 7:
            val2 = 7
        elif check1 >= 42 and (z50 == p3 or z51 == p3 or z52 == p3 or z53 == p3 or z54 == p3 or z55 == p3 or z56 == p3 or z57 == p3) and ival == 1:
            val2 = 1
        elif check2 <= 42 and (z60 == p3 or z61 == p3 or z62 == p3 or z63 == p3 or z64 == p3 or z65 == p3 or z66 == p3 or z67 == p3) and ival == 2:
            val2 = 2
        elif check3 <= 42 and (z70 == p3 or z71 == p3 or z72 == p3 or z73 == p3 or z74 == p3 or z75 == p3 or z76 == p3 or z77 == p3) and ival == 3:
            val2 = 3
        elif check4 <= 42 and (y44 == p21 or y45 == p21 or y46 == p21 or y47 == p21):
            val2 = 4
        elif check1 <= 42 and (y44 == p21 or y45 == p21 or y46 == p21 or y47 == p21):
            val2 = 1
        elif check2 <= 42 and (y54 == p21 or y55 == p21 or y56 == p21 or y57 == p21 or y58 == p21):
            val2 = 2
        elif check5 <= 42 and (y54 == p21 or y55 == p21 or y56 == p21 or y57 == p21 or y58 == p21):
            val2 = 5
        elif check6 <= 42 and (y63 == p21 or y64 == p21 or y65 == p21 or y66 == p21 or y67 == p21):
            val2 = 6
        elif check3 <= 42 and (y63 == p21 or y64 == p21 or y65 == p21 or y66 == p21 or y67 == p21):
            val2 = 3
        elif y30 == p21 or y31 == p21 or y32 == p21 or y33 == p21 or y34 == p21 or y35 == p21 or y36 == p21 or y37 == p21:
             val2 = 3
        elif y10 == p21 or y11 == p21 or y12 == p21:
             val2 = 1
        elif y20 == p21 or y21 == p21 or y22 == p21:
             val2 = 2
        elif y40 == p21 or y41 == p21 or y42 == p21 or y44 == p21:
             val2 = 4
        elif y50 == p21 or y51 == p21 or y52 == p21 or y53 == p21:
             val2 = 5
        elif y60 == p21 or y61 == p21 or y62 == p21:
             val2 = 6
        elif y70 == p21 or y71 == p21 or y72 == p21:
             val2 = 7
        elif d0 == p3 and check4 >= 21:
             val2 = 4
        elif d1 == p3 and check5 >= 28:
             val2 = 5
        elif d2 == p3 and check6 >= 35:
             val2 = 6
        elif d3 == p3 and check5 >= 21:
             val2 = 5
        elif d4 == p3 and check5 >= 28:
             val2 = 6
        elif d5 == p3 and check6 >= 35:
             val2 = 7
        elif d6 == p3 and check6 >= 21:
             val2 = 6
        elif d7 == p3 and check7 >= 28:
             val2 = 7
        elif d8 == p3 and check7 >= 28:
             val2 = 7
        elif d9 == p3 and check4 >= 28:
             val2 = 4
        elif d10 == p3 and check5 >= 35:
             val2 = 5
        elif d11 == p3 and check4 >= 35:
             val2 = 4
        elif d12 == p3 and check4 >= 21:
             val2 = 4
        elif d13 == p3 and check3 >= 28:
             val2 = 3
        elif d14 == p3 and check2 >= 35:
             val2 = 2
        elif d15 == p3 and check3 >= 21:
             val2 = 3
        elif d16 == p3 and check2 >= 28:
             val2 = 2
        elif d17 == p3 and check1 >= 35:
             val2 = 1
        elif d18 == p3 and check2 >= 28:
             val2 = 2
        elif d19 == p3 and check1 >= 35:
             val2 = 1
        elif d20 == p3 and check1 >= 21:
             val2 = 1
        elif d21 == p3 and check4 >= 28:
             val2 = 5
        elif d22 == p3 and check3 >= 35:
             val2 = 3
        elif d23 == p3 and check4 >= 35:
             val2 = 7
        elif ival == 1 and (z10 == p31 or z11 == p31 or z12 == p31):
            val2 = 1
        elif ival == 2 and (z20 == p31 or z21 == p31 or z22 == p31):
            val2 = 2
        elif ival == 3 and (z30 == p31 or z31 == p31 or z32 == p31):
            val2 = 3
        elif ival == 4 and (z40 == p31 or z41 == p31 or z42 == p31 or z43 == p31 or z44 == p31 or z45 == p31 or z46 == p31 or z47 == p31):
            val2 = 4
        elif check5 <= 42 and (z50 == p31 or z51 == p31 or z52 == p31 or z53 == p31 or z54 == p31 or z55 == p31 or z56 == p31 or z57 == p31):
            val2 = 5
        elif check6 <= 42 and (z60 == p31 or z61 == p31 or z62 == p31 or z63 == p31 or z64 == p31 or z65 == p31 or z66 == p31 or z67 == p31):
            val2 = 6
        elif check7 <= 42 and (z70 == p31 or z71 == p31 or z72 == p31 or z73 == p31 or z74 == p31 or z75 == p31 or z76 == p31 or z77 == p31):
            val2 = 7
        elif check1 >= 42 and (z50 == p31 or z51 == p31 or z52 == p31 or z53 == p31 or z54 == p31 or z55 == p31 or z56 == p31 or z57 == p31):
            val2 = 1
        elif check2 <= 42 and (z60 == p31 or z61 == p31 or z62 == p31 or z63 == p31 or z64 == p31 or z65 == p31 or z66 == p31 or z67 == p31):
            val2 = 2
        elif check3 <= 42 and (z70 == p31 or z71 == p31 or z72 == p31 or z73 == p31 or z74 == p31 or z75 == p31 or z76 == p31 or z77 == p31):
            val2 = 3
        elif y30 == p31 or y31 == p31 or y32 == p31 or y33 == p31 or y34 == p31 or y35 == p31 or y36 == p31 or y37 == p31:
             val2 = 3
        elif y10 == p31 or y11 == p31 or y12 == p31:
             val2 = 1
        elif y20 == p31 or y21 == p31 or y22 == p31:
             val2 = 2
        elif y40 == p31 or y41 == p31 or y42 == p31 or y44 == p31:
             val2 = 4
        elif y50 == p31 or y51 == p31 or y52 == p31 or y53 == p31:
             val2 = 5
        elif y60 == p31 or y61 == p31 or y62 == p31:
             val2 = 6
        elif y70 == p31 or y71 == p31 or y72 == p31:
             val2 = 7
        elif d0 == p31 and check4 >= 21:
             val2 = 4
        elif d1 == p31 and check5 >= 28:
             val2 = 5
        elif d2 == p31 and check6 >= 35:
             val2 = 6
        elif d3 == p31 and check5 >= 21:
             val2 = 5
        elif d4 == p31 and check5 >= 28:
             val2 = 6
        elif d5 == p31 and check6 >= 35:
             val2 = 7
        elif d6 == p31 and check6 >= 21:
             val2 = 6
        elif d7 == p31 and check7 >= 28:
             val2 = 7
        elif d8 == p31 and check7 >= 28:
             val2 = 7
        elif d9 == p31 and check4 >= 28:
             val2 = 4
        elif d10 == p31 and check5 >= 35:
             val2 = 5
        elif d11 == p31 and check4 >= 35:
             val2 = 4
        elif d12 == p31 and check4 >= 21:
             val2 = 4
        elif d13 == p31 and check3 >= 28:
             val2 = 3
        elif d14 == p31 and check2 >= 35:
             val2 = 2
        elif d15 == p31 and check3 >= 21:
             val2 = 3
        elif d16 == p31 and check2 >= 28:
             val2 = 2
        elif d17 == p31 and check1 >= 35:
             val2 = 1
        elif d18 == p31 and check2 >= 28:
             val2 = 2
        elif d19 == p31 and check1 >= 35:
             val2 = 1
        elif d20 == p31 and check1 >= 21:
             val2 = 1
        elif d21 == p31 and check4 >= 28:
             val2 = 5
        elif d22 == p31 and check3 >= 35:
             val2 = 3
        elif d23 == p31 and check4 >= 35:
             val2 = 7
        else:
            val2 = map_nbr.random_nbr(2,0)
        while  check1 >= 42 and val2 == 1 or check2 >= 42 and val2 == 2 or check3 >= 42 and val2 == 3 or check4 >= 42 and val2 == 4 or check5 >= 42 and val2 == 5 or check6 >= 42 and val2 == 6 or check7 >= 42 and val2 == 7 :
            val2 = map_nbr.random_nbr(2,0)
        print("%s a choisi la colonne %d" %(n2,val2))
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
            map_nbr.print_board(board,n1,n2,play/12)
            print("%s as gagnes!!!" % (n2))
            map_nbr.restart(2,n1,n2)
        if draw == 252:
            map_nbr.print_board(board,n1,n2,play/12)
            print("Egalite")
            map_nbr.restart(2,n1,n2)
        map_nbr.print_board(board,n1,n2,play/12)
