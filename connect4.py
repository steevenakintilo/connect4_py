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
import ia
import map_nbr
import vs

system("clear")

board = []
for i in range(42):
    board.append(" ")
print("=====  Puissance%s  =====" % (colored('4', 'red')))
print("                       ")
print("1. 1V1")
print("2. VS L'IA")
print("3. QUITTER")
print("                       ")
print("                       ")
choice = input("Choix:  ")
chx = int(choice)
rdm = map_nbr.random_nbr(89,0)
n3 = colored("L'IA", 'yellow')
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
    map_nbr.print_board(board,name1,name2,0)
if chx == 2 and rdm == 2:
    map_nbr.print_board(board,name1,"L'IA",0)
if chx == 2 and rdm == 1:
    print("%s a choisi la colonne: 4" %(n3))
    map_nbr.nprint_board(board,name1,"L'IA",0)
if chx == 2:
    ia.connect4_ia(rdm,n1,n2)
if chx == 1:
    vs.connect4_vs(n1,n2)
if chx == 3:
    print("Bye")
    quit()
if chx != 1 and chx !=2 and chx != 3:
    quit()
