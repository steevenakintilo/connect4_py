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
b1 =  [board[35],board[28],board[21],board[14],board[7],board[0]]
b2 =  [board[36],board[29],board[22],board[15],board[8],board[1]]
b3 =  [board[37],board[30],board[23],board[16],board[9],board[2]]
b4 =  [board[38],board[31],board[24],board[17],board[10],board[3]]
b5 =  [board[39],board[32],board[25],board[18],board[11],board[4]]
b6 =  [board[40],board[33],board[26],board[19],board[12],board[5]]
b7 =  [board[41],board[34],board[27],board[20],board[13],board[6]]
print(b1[0])
i = 0
check1 = 0
check2 = 0
check3 = 0
check4 = 0
check5 = 0
check6 = 0
check7 = 0
print_board(board)
while True:
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
