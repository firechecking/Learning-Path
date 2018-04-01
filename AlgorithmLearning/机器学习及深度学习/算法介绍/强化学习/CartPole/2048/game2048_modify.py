# -*- coding: utf-8 -*-
# @Time    : 2017/11/30 下午2:07
# @Author  : ZZZ
# @Email   : zuxinxing531@pingan.com.cn
# @File    : game2048_ori.py
# @Software: CartPole
# @Descript: game2048_ori

import random
from sys import exit
from copy import deepcopy
import pygame
from pygame.locals import *

board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
newboard = []
pygame.init()

box_size = 50
box_gap  = 5
top_of_screen = 100
bottom_of_screen = 30
left_of_screen = 20
screen_width  = box_size * 4 + box_gap * 5 + left_of_screen * 2
screen_height = top_of_screen + box_gap * 5 + box_size * 4 + left_of_screen + bottom_of_screen
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
pygame.display.set_caption("2048")
background = pygame.image.load('background.png').convert()
score = 0

OLDLACE    = pygame.color.THECOLORS["oldlace"]
IVORY   = pygame.color.THECOLORS["ivory3"]
BLACK   = pygame.color.THECOLORS["black"]
RED     = pygame.color.THECOLORS["red"]
RED2    = pygame.color.THECOLORS["red2"]
DARKGOLD  = pygame.color.THECOLORS["darkgoldenrod1"]
GOLD    =  pygame.color.THECOLORS["gold"]
GRAY    = pygame.color.THECOLORS["gray41"]
CHOCOLATE = pygame.color.THECOLORS["chocolate"]
CHOCOLATE1 = pygame.color.THECOLORS["chocolate1"]
CORAL   = pygame.color.THECOLORS["coral"]
CORAL2  = pygame.color.THECOLORS["coral2"]
ORANGED = pygame.color.THECOLORS["orangered"]
ORANGED2 = pygame.color.THECOLORS["orangered2"]
DARKORANGE = pygame.color.THECOLORS["darkorange"]
DARKORANGE2 = pygame.color.THECOLORS["darkorange2"]
FORESTGREEN = pygame.color.THECOLORS['forestgreen']


class Box:
    def __init__(self, topleft, text, color):
        self.topleft = topleft
        self.text = text
        self.color = color
    def render(self, surface):
        x, y = self.topleft
        pygame.draw.rect(surface, self.color, (x, y, box_size, box_size))
        text_height  = int(box_size * 0.35)
        font_obj     = pygame.font.Font(None, text_height)
        text_surface = font_obj.render(self.text, True, BLACK)
        text_rect    = text_surface.get_rect()
        text_rect.center = (x + box_size / 2, y + box_size / 2)
        surface.blit(text_surface, text_rect)


def draw_box():
    global board
    # colors = {0:GRAY, 2:(239, 233, 182), 4:(239, 228, 151), 8:(243, 212, 77), 16:(239, 206, 25),
    #           32:(242, 157, 12), 64:(214, 214, 42), 128:(239, 207, 108), 256:(239, 207, 99),
    #           512:(239, 203, 82), 1024:(239, 199, 57), 2048:(239, 195, 41), 4096:(255, 60, 57)}
    colors = {0:(192, 192, 192), 2:(176, 224, 230), 4:(127, 255, 212), 8:(135, 206, 235), 16:(64, 224, 208),
              32:(0, 255, 255), 64:(0, 201, 87), 128:(50, 205, 50), 256:(34, 139, 34),
              512:(0, 255, 127), 1024:(61, 145, 64), 2048:(48, 128, 20), 4096:(65, 105, 255),
              8192:(8, 46, 84), 16384:(11, 23, 70), 32768:(25, 25, 112), 65536:(0, 0, 255)}
    x, y = left_of_screen, top_of_screen
    size = box_size * 4 + box_gap * 5
    pygame.draw.rect(screen, BLACK, (x, y, size, size))
    x, y = x + box_gap, y + box_gap
    for i in range(4):
        for j in range(4):
            idx = board[i][j]
            if idx == 0:
                text = ""
            else:
                text = str(idx)
            if idx > 65536: idx = 65536
            color = colors[idx]
            box = Box((x, y), text, color)
            box.render(screen)
            x += box_size + box_gap
        x = left_of_screen + box_gap
        y += box_size + box_gap


def set_random_number():
    pool = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                pool.append((i, j))
    m = random.choice(pool)
    pool.remove(m)
    value = random.uniform(0, 1)
    if value < 0.1:
        value = 4
    else:
        value = 2
    board[m[0]][m[1]] = value

def init_board():
    for i in range(2):
        set_random_number()

def combinate(L):
    global score
    ans = [0, 0, 0, 0]
    num = []
    for i in L:
        if i != 0:
            num.append(i)
    length = len(num)
    if length == 4:
        if num[0] == num[1]:
            ans[0] = num[0] + num[1]
            score += ans[0]
            if num[2] == num[3]:
                ans[1] = num[2] + num[3]
                score += ans[1]
            else:
                ans[1] = num[2]
                ans[2] = num[3]
        elif num[1] == num[2]:
            ans[0] = num[0]
            ans[1] = num[1] + num[2]
            ans[2] = num[3]
            score += ans[1]
        elif num[2] == num[3]:
            ans[0] = num[0]
            ans[1] = num[1]
            ans[2] = num[2] + num[3]
            score += ans[2]
        else:
            for i in range(length):
                ans[i] = num[i]
    elif length == 3:
        if num[0] == num[1]:
            ans[0] = num[0] + num[1]
            ans[1] = num[2]
            score += ans[0]
        elif num[1] == num[2]:
            ans[0] = num[0]
            ans[1] = num[1] + num[2]
            score += ans[1]
        else:
            for i in range(length):
                ans[i] = num[i]
    elif length == 2:
        if num[0] == num[1]:
            ans[0] = num[0] + num[1]
            score += ans[0]
        else:
            for i in range(length):
                ans[i] = num[i]
    elif length == 1:
        ans[0] = num[0]
    else:
        pass
    return ans

def left():
    # global score
    for i in range(4):
        temp = combinate(board[i])
        for j in range(4):
            board[i][j] = temp[j]
            # score += temp[1]
    # return score


def right():
    # global score
    for i in range(4):
        temp = combinate(board[i][::-1])
        for j in range(4):
            board[i][3-j] = temp[j]
            # score += temp[1]
    # return score

def up():
    for i in range(4):
        to_comb = []
        for j in range(4):
            to_comb.append(board[j][i])
        temp = combinate(to_comb)
        for k in range(4):
            board[k][i] = temp[k]
            # score += temp[1]
    # return score

def down():
    for i in range(4):
        to_comb = []
        for j in range(4):
            to_comb.append(board[3-j][i])
        temp = combinate(to_comb)
        for k in range(4):
            board[3-k][i] = temp[k]
            # score += temp[1]
    # return score

def write(msg="pygame is cool", color= BLACK, height = 14):
    #myfont = pygame.font.SysFont("None", 32) #To avoid py2exe error
    myfont = pygame.font.Font(None, height)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    return mytext

def is_over():
    ### if 0 in board
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False

    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j+1]:
                return False

    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i+1][j]:
                return False

    return True

def read_best():
    try:
        f = open('best.rec', 'r')
        best = int(f.read())
        f.close()
    except:
        best = 0
    return best

def write_best(best):
    try:
        f = open('best.rec', 'w')
        f.write(str(best))
        f.close()
    except IOError:
        pass

def main():
    global score
    global board
    global newboard
    screen.blit(background, (0, 0))
    init_board()
    newboard = deepcopy(board)
    gameover = is_over()

    #### test text and color in box
    # for i in range(4):
    #     for j in range(4):
    #         board[i][j] = 2 ** (i+4*j)
    # board[0][0] = 0
    ### end test text and color

    draw_box()
    screen.blit(write("2048", height = 40, color = GOLD), (left_of_screen, left_of_screen // 2))

    screen.blit(write("SCORE", height=14, color=FORESTGREEN), (left_of_screen+105, left_of_screen//2 + 5))
    rect1 = pygame.draw.rect(screen, FORESTGREEN, (left_of_screen+100, left_of_screen//2 + 30, 60, 20))
    text1 = write(str(score), height=14, color=GOLD)
    text1_rect = text1.get_rect()
    text1_rect.center = (left_of_screen+100+30, left_of_screen//2 + 40)
    screen.blit(text1, text1_rect)

    screen.blit(write("BEST", height=14, color=FORESTGREEN), (left_of_screen+175, left_of_screen//2 + 5))
    rect2 = pygame.draw.rect(screen, FORESTGREEN, (left_of_screen+165, left_of_screen//2 + 30, 60, 20))
    best = read_best()
    if best < score:
        best = score
    text2 = write(str(best), height=14, color=GOLD)
    text2_rect = text2.get_rect()
    text2_rect.center = (left_of_screen+165+30, left_of_screen//2 + 40)
    screen.blit(text2, text2_rect)


    screen.blit(write("Use LEFT, RIGHT, UP, DOWN", height=16, color=GRAY), (left_of_screen, screen_height - bottom_of_screen))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                restart()
                gameover = is_over()
            if not gameover:
                if event.type == KEYUP and event.key == K_UP:
                    up()
                elif event.type == KEYUP and event.key == K_DOWN:
                    down()
                elif event.type == KEYUP and event.key == K_LEFT:
                    left()
                elif event.type == KEYUP and event.key == K_RIGHT:
                    right()
                if newboard != board:
                    set_random_number()
                    newboard = deepcopy(board)
                    draw_box()
                gameover = is_over()
                if gameover == True:
                    restart()
                    gameover = is_over()

                rect1 = pygame.draw.rect(screen, FORESTGREEN, (left_of_screen+100, left_of_screen//2 + 30, 60, 20))
                text1 = write(str(score), height=14, color=GOLD)
                text_rect = text1.get_rect()
                text_rect.center = (left_of_screen+100+30, left_of_screen//2 + 40)
                screen.blit(text1, text_rect)

                rect2 = pygame.draw.rect(screen, FORESTGREEN, (left_of_screen+165, left_of_screen//2 + 30, 60, 20))
                if best < score:
                    best = score
                text2 = write(str(best), height=14, color=GOLD)
                text2_rect = text2.get_rect()
                text2_rect.center = (left_of_screen+165+30, left_of_screen//2 + 40)
                screen.blit(text2, text2_rect)

            else:
                write_best(best)
                screen.blit(write("Game Over!", height = 40, color = FORESTGREEN), (left_of_screen, screen_height // 2))

        pygame.display.update()
def restart():
    global board
    global score
    global newboard
    print "restart"
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    init_board()
    newboard = deepcopy(board)
    score = 0
    print board

if __name__ == "__main__":
    main()
    # test()
    # print(combinate([4,2,2,2]))