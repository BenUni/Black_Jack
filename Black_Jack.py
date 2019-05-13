#from IPython.display import clear_output
import pygame
from pygame.locals import *
import os


def draw_jack_board_pygame(board):
    '''
    #Draw the game board
    '''
    buttons = []
    color = (0,0,0)
    for x in range(0,64):
        if board[x] == 'White':
            color = (255,255,255)
        elif board[x] == 'Brown':
           color = (139,69,19)
        elif board[x] == 'Black':
            color = (0,0,0)
        elif board[x] == 'Red':
            color = (255,0,0)
        elif board[x] == 'Green':
            color = (0,255,0)
        elif board[x] == 'Blue':
            color = (47,149,153)
        c = pygame.draw.rect(screen, color, pygame.Rect(square_location[x][1], square_location[x][0],60, 60))
        buttons.append(c)


while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
                done = True

        # If there is a click on the game
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pass