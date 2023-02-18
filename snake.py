import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass
        
    def move(self, dirnx, dirny):
        pass
    
    def draw(self, surface, eyes=False):
        pass
        

class snake(object):

    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()

        for key in keys:
            if keys[pygame.K_a]:
                self.dirnx = -1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            
            elif keys[pygame.K_d]:
                self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_w]:
                self.dirnx = 0
                self.dirny = -1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_s]:
                self.dirnx = 0
                self.dirny = 1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i,c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)

            else:
                


    def reset(self, pos):
        pass

    def addCube(self):
        pass
        

    def draw(self, surface):
        pass


def drawGrid(width, rows, surface):
    sizeDiff = width // rows
    x = 0
    y = 0
    for l in range(rows):

        x = x + sizeDiff
        y = y + sizeDiff

        pygame.draw.line(surface, (255,255,255), (x,0), (x,width))
        pygame.draw.line(surface,(255,255,255),(0,y),(width,y))

def redrawWindow(surface):
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()
    

def randomSnack(rows, item):
    pass


def message_box(subject, content):
    pass


def main():
    global height,width,rows
    height = 500
    width = 500
    rows = 20
    frame = pygame.display.set_mode((width, height))
    s = snake((255,0,0), (10,10))
    clock = pygame.time.Clock()

    flag = True
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(frame)
        pass 

main()