#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## ...
## File description:
## ...
##

import sys
from termcolor import colored, cprint
from os import system
from random import randint
import vs
import ia
def random_nbr(nb,res):
    if nb == 1:
         return(randint(res, res + 1))
    if nb == 89:
         return(randint(1,2))
    if nb != 1 and nb != 89:
        return(randint(1, 7))
pass

def print_empty_board(list,name1,name2,play):
    n1 = colored(name1, 'red')
    n2 = colored(name2, 'yellow')
    p = colored(play, 'blue')
    if play == 4:
        board[38 - check4] = "O"
        board[38] = colored(board[38], 'yellow') 
        play = 1
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

def restart(mod,name1,name2):
    board = []
    for i in range(42):
        board.append(" ")
    n3 = colored("L'IA", 'yellow')
    empty_board = []
    rdm = random_nbr(89,0)
    for i in range(42):
        empty_board.append(" ")
    r = input("Appuie sur O pour rejouer et Q pour quitter: ")
    if r == "Q":
        print("Bye")
        quit()
    if r == "O" and mod == 1:
        system("clear")
        print_empty_board(empty_board, name1, name2, 0)
        vs.connect4_vs(name1,name2)
    print(rdm)
    if r == "O" and mod == 2 and rdm == 2:
        system("clear")
        print_empty_board(empty_board, name1, name2, 0)
        ia.connect4_ia(rdm,name1,name2)
    if r == "O" and mod == 2 and rdm == 1:
        system("clear")
        print("%s a choisi la colonne: 4" %(n3))
        nprint_board(board,name1,"L'IA",0)
        ia.connect4_ia(rdm,name1,name2)
    
def print_table(TABLE):
    for r in TABLE:
        for c in r:
            print(c,end = "   ")
        print()
    pass


def nprint_board(list,name1,name2,play):
    n1 = colored(name1, 'red')
    n2 = colored(name2, 'yellow')
    p = colored(play, 'blue')
    play = 4
    nn = colored('O', 'yellow')
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
    print("|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |" % (list[35],list[36],list[37],nn,list[39],list[40],list[41]))
    print("   1     2     3     4     5     6     7   ")

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
