# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 21:49:19 2021

@author: Stephanie Kaes
"""
import time

import numpy as np
import pygame
from pygame.locals import *

import Backgammon_game
import Backgammon_game as bg
import Backgammon

             
#-------------The user Agent -----------------------------------------    

startpos = -1
endpos = -1
valid=False
def handleInput(pos, board, player, dice):
    Backgammon_game.pretty_print(board)
    global startpos
    global endpos
    global valid
    #startposition setzen
    if player == 1:
        if startpos == -1 and board[pos] >= 1:
            startpos = pos
            print("startpos gesetzt ", startpos)
        elif pos == startpos - dice[0] or pos == startpos - dice[1]:
            if board[pos] >= -1 and board[pos+24] != 1:
                endpos = pos
                valid = True
                print("endpos gesetzt ", endpos)
            else:
                print("deleting positions")
                startpos = -1
                endpos = -1
        else:
            print("deleting positions")
            startpos = -1
            endpos = -1

    elif player == -1:
        if startpos == -1 and board[pos] <= -1: startpos = pos
        elif pos == startpos + dice[0] or pos == startpos + dice[1]:
            if board[pos] <= 1 and board[pos+24] != -1:
                endpos = pos
                valid = True
            else:
                print("deleting positions")
                startpos = -1
                endpos = -1
        else:
            print("deleting positions")
            startpos = -1
            endpos = -1

def user_action(board_copy,dice,player,i):
    global startpos
    global endpos
    global valid
    startpos = -1
    endpos = -1
    valid = False
    # user agent
    # inputs are the board, the dice and which player is to move
    # outputs the chosen move accordingly to mouse input

    #eventloop(user_exists)
    # check out the legal moves available for the throw
    possible_moves, possible_boards = bg.legal_moves(board_copy, dice, player)
    print(possible_moves)
    # if there are no moves available
    if len(possible_moves) == 0:
        return []

    while not valid:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            position = Backgammon.gui.getPosition(x, y)
            handleInput(position, board_copy, player, dice)

    #for possible_move in possible_moves:
    #    print(possible_move)

    #if np.array([np.array((possible_move[0] == [startpos1, endpos1])).all() for possible_move in possible_moves]).any():
    #    if not np.array([np.array((len(possible_move) == 2 and possible_move[0] == [startpos1, endpos1])).all() for possible_move in possible_moves]).any():
    #        return [[startpos1, endpos1]]
    #    else:
    #        print("ist drin")
    #        event_happened = False
    #        while not event_happened:
    #            event = pygame.event.wait()
    #            if event.type == pygame.MOUSEBUTTONDOWN:
    #                x, y = pygame.mouse.get_pos()
    #                position = Backgammon.gui.getPosition(x, y)
    #                startpos2 = position
    #                print(startpos2)
    #                event_happened = True
#
    #        event_happened = False
    #        while not event_happened:
    #            event = pygame.event.wait()
    #            if event.type == pygame.MOUSEBUTTONDOWN:
    #                x, y = pygame.mouse.get_pos()
    #                position = Backgammon.gui.getPosition(x, y)
    #                endpos2 = position
    #                print(endpos2)
    #                event_happened = True

    return [startpos, endpos]