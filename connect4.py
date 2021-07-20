#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## d
## File description:
## d
##

def print_table(TABLE):
    for r in TABLE:
        for c in r:
            print(c,end = "   ")
        print()
    pass

def print_board(list):
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[0],list[1],list[2],list[3],list[4],list[5],list[6]))
    print("|-----|-----|-----|-----|-----|-----|-----|")
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[7],list[8],list[9],list[10],list[11],list[12],list[13]))
    print("|-----|-----|-----|-----|-----|-----|-----|")
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[14],list[15],list[16],list[17],list[18],list[19],list[20]))
    print("|-----|-----|-----|-----|-----|-----|-----|")
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[21],list[22],list[23],list[24],list[25],list[26],list[27]))
    print("|-----|-----|-----|-----|-----|-----|-----|")
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[28],list[29],list[30],list[31],list[32],list[33],list[34]))
    print("|-----|-----|-----|-----|-----|-----|-----|")
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[35],list[36],list[37],list[38],list[39],list[40],list[41]))
    print("   1     2     3     4     5     6     7   ")

#T = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
board = []
j = 0
for i in range(42):
    board.append(" ")
empty_list = [" "," "," "," "," "," "]
p1 = ["X","X","X","X"]
p2win_list = ["O","O","O","O"]
#p1win = [board[35],board[36],board[37],board[38]]
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
print_board(board)
while True:
    #p1win = [board[35],board[36],board[37],board[38]]
    #print_board(board)
    val = input("J1 choisi une colonne: ")
    if val == "1":
        for i in b1:
            if b1 == empty_list:
                board[35 - check1] = "X"
        check1 = check1 + 7
    if val == "2":
        for i in b2:
            if b2 == empty_list:
                board[36 - check2] = "X"
        check2 = check2 + 7
    if val == "3":
        for i in b3:
            if b3 == empty_list:
                board[37 - check3] = "X"
        check3 = check3 + 7
    if val == "4":
        for i in b4:
            if b4 == empty_list:
                board[38 - check4] = "X"
        check4 = check4 + 7
    if val == "5":
        for i in b5:
            if b5 == empty_list:
                board[39 - check5] = "X"
        check5 = check5 + 7
    if val == "6":
        for i in b6:
            if b6 == empty_list:
                board[40 - check6] = "X"
        check6 = check6 + 7
    if val == "7":
        for i in b7:
            if b7 == empty_list:
                board[41 - check7] = "X"
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
    w44 = [board[23],board[17],board[11],board[4]]
    w45 = [board[36],board[30],board[24],board[18]]
    w46 = [board[30],board[24],board[18],board[12]]
    w47 = [board[24],board[18],board[12],board[6]]
    w48 = [board[37],board[31],board[25],board[19]]
    w49 = [board[31],board[25],board[19],board[13]]
    w50 = [board[38],board[32],board[26],board[20]]
    w51 = [board[28],board[22],board[16],board[10]]
    w52 = [board[22],board[16],board[10],board[4]]
    w53 = [board[21],board[15],board[9],board[3]]
    
    #print(w33)
    if w == p1 or w2 == p1 or w3 == p1 or w4 == p1 or w5 == p1 or w6 == p1 or w7 == p1 or w8 == p1 or w9 == p1 or w10 == p1 or w11 == p1 or w12 == p1 or w13 == p1 or w14 == p1 or w15 == p1 or w16 == p1 or w17 == p1 or w18 == p1 or w19 == p1 or w20 == p1 or w21 == p1 or w22 == p1  or w23 == p1 or w24 == p1 or w25 == p1 or w26 == p1 or w27 == p1 or w28 == p1 or w29 == p1 or w30 == p1 or w31 == p1 or w32 == p1 or w33 == p1 or w34 == p1 or w35 == p1 or w36 == p1 or w37 == p1 or w38 == p1 or w39 == p1 or w40 == p1 or w41 == p1 or w42 == p1 or w43 == p1 or w44 == p1 or w45 == p1 or w46 == p1 or w47 == p1 or w48 == p1 or w49 == p1 or w50 == p1 or w51 == p1 or w52 == p1 or w53 == p1:
        print_board(board)
        print("You win")
        quit() 
    print_board(board)
    val2 = input("J2 choisi une colonne: ")
    if val2 == "1":
        for i in b1:
            if b1 == empty_list:
                board[35 - check1] = "O"
        check1 = check1 + 7
    if val2 == "2":
        for i in b2:
            if b2 == empty_list:
                board[36 - check2] = "O"
        check2 = check2 + 7
    if val2 == "3":
        for i in b3:
            if b3 == empty_list:
                board[37 - check3] = "O"
        check3 = check3 + 7
    if val2 == "4":
        for i in b4:
            if b4 == empty_list:
                board[38 - check4] = "O"
        check4 = check4 + 7
    if val2 == "5":
        for i in b5:
            if b5 == empty_list:
                board[39 - check5] = "O"
        check5 = check5 + 7
    if val2 == "6":
        for i in b6:
            if b6 == empty_list:
                board[40 - check6] = "O"
        check6 = check6 + 7
    if val2 == "7":
        for i in b7:
            if b7 == empty_list:
                board[41 - check7] = "O"
        check7 = check7 + 7
    print_board(board)
