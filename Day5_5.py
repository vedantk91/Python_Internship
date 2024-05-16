# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 08:55:17 2021

@author: kelka
"""

tic_tac_toe_Board = {'1': ' ', '2': ' ', '3': ' ',
                    '4': ' ', '5': ' ', '6': ' ',
                    '7': ' ', '8': ' ', '9': ' '}

board_keys = []

for key in tic_tac_toe_Board:
    board_keys.append(key)



def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(tic_tac_toe_Board)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        if tic_tac_toe_Board[move] == ' ':
            tic_tac_toe_Board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue


        if count >= 5:
            if tic_tac_toe_Board['7'] == tic_tac_toe_Board['8'] == tic_tac_toe_Board['9'] != ' ':
                printBoard(tic_tac_toe_Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif tic_tac_toe_Board['4'] == tic_tac_toe_Board['5'] == tic_tac_toe_Board['6'] != ' ':
                printBoard(tic_tac_toe_Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif tic_tac_toe_Board['1'] == tic_tac_toe_Board['2'] == tic_tac_toe_Board['3'] != ' ':
                printBoard(tic_tac_toe_Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif tic_tac_toe_Board['1'] == tic_tac_toe_Board['4'] == tic_tac_toe_Board['7'] != ' ':
                printBoard(tic_tac_toe_Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif tic_tac_toe_Board['2'] == tic_tac_toe_Board['5'] == tic_tac_toe_Board['8'] != ' ':
                printBoard(tic_tac_toe_Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif tic_tac_toe_Board['3'] == tic_tac_toe_Board['6'] == tic_tac_toe_Board['9'] != ' ':
                printBoard(tic_tac_toe_Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif tic_tac_toe_Board['7'] == tic_tac_toe_Board['5'] == tic_tac_toe_Board['3'] != ' ':
                printBoard(tic_tac_toe_Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif tic_tac_toe_Board['1'] == tic_tac_toe_Board['5'] == tic_tac_toe_Board['9'] != ' ':
                printBoard(tic_tac_toe_Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break


        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")


        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            tic_tac_toe_Board[key] = " "

        game()


game()